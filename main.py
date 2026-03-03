from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from prometheus_client import Counter, generate_latest
import requests


app = FastAPI(title="Digital Banking API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


REQUEST_COUNT = Counter("gateway_requests_total", "Total Gateway Requests")

@app.middleware("http")
async def count_requests(request: Request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")



@app.get("/health")
def health():
    return {"status": "ok"}


async def forward_request(service_url: str, path: str, request: Request):
    url = f"{service_url}/{path}"

    body = None
    if request.method in ["POST", "PUT", "PATCH"]:
        body = await request.json()

    try:
        response = requests.request(
            method=request.method,
            url=url,
            json=body,
            headers={key: value for key, value in request.headers.items() if key != "host"},
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )

    except requests.exceptions.RequestException:
        return JSONResponse(
            status_code=503,
            content={"error": "Service unavailable"}
        )



@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_auth(path: str, request: Request):
    return await forward_request("http://auth-service:8000", path, request)


@app.api_route("/accounts/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_accounts(path: str, request: Request):
    return await forward_request("http://account-service:8000", path, request)


@app.api_route("/transactions/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_transactions(path: str, request: Request):
    return await forward_request("http://transaction-service:8000", path, request)


@app.api_route("/loans/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_loans(path: str, request: Request):
    return await forward_request("http://loan-service:8000", path, request)


@app.api_route("/reports/{path:path}", methods=["GET"])
async def proxy_reports(path: str, request: Request):
    return await forward_request("http://reporting-service:8000", path, request)