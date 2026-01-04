from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text, select
from sqlalchemy.orm import Session

from app.database import engine
from app.models.models import Users, Departments
from app.schemas import SubmissionDetails
from app.repositories.crud import UserSubmission

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.on_event("startup")
def startup_event():
    """
    Simple connectivity check on startup.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful!")
    except Exception as e:
        print(f"Failed to connect to database: {e}")


def get_session() -> Session:
    """
    Dependency that yields a SQLAlchemy ORM session.
    """
    with Session(engine) as session:
        yield session


@app.get("/developer", response_class=FileResponse)
def developer_page():

  return FileResponse("frontend/author.html")


@app.get("/schedule_submission", response_class=FileResponse)
def schedule_submission_page():
    """
    Render the frontend application for scheduling submissions.
    """
    return FileResponse("frontend/index.html")


@app.get("/users")
def list_users(session: Session = Depends(get_session)):
    """
    Example query endpoint that returns all rows from the users table.
    """
    stmt = select(Departments)
    result = session.execute(stmt).scalars().all()
    return result


@app.post("/schedule_submission")
def scheduler(
    data: SubmissionDetails,
    session: Session = Depends(get_session),
):
    """
    Accept a schedule submission payload, validate it via Pydantic,
    inject a DB session, and delegate to the CRUD class.
    """
    submission = UserSubmission(session=session, data=data)
    submission.add_submission()
    return {"status": "scheduled"}
