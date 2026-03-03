from starlette.middleware.base import BaseHTTPMiddleware
from models import AuditLog
from database import SessionLocal
from datetime import datetime

class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        db = SessionLocal()

        user_id = getattr(request.state, "user_id", None)

        log = AuditLog(
            user_id=user_id,
            action=request.method,
            endpoint=request.url.path,
            timestamp=datetime.utcnow(),
            ip_address=request.client.host
        )

        db.add(log)
        db.commit()
        db.close()

        return response