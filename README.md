Loan Service

This service handles loan applications, approvals, rejections, and provides loan data for the system.

Endpoints
POST /loans/apply - Apply for a new loan
GET /loans/pending - List all pending loans
PUT /loans/{loan_id}/approve - Approve a loan
PUT /loans/{loan_id}/reject - Reject a loan

Setup
1. Ensure docker and docker-compose are installed
2. Create .env file with DATABASE_URL and JWT settings
3. Run docker-compose up --build