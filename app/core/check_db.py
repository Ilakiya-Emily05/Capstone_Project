from app.core.database import init_db, SessionLocal
from app.models.user import User

# Create tables
init_db()

# Test DB session
db = SessionLocal()
try:
    users = db.query(User).all()
    print("Users in DB:", users)
except Exception as e:
    print("Error querying users:", e)
finally:
    db.close()