from fastapi import APIRouter

from ..schemas import SubmissionDetails
from ..services.schedule_service import schedule_submission


router = APIRouter()


@router.get("/")
def index():
    return {"Message": "Hello World"}


@router.post("/schedule_submission")
def scheduler(data: SubmissionDetails):
    """
    Accept a schedule submission payload and delegate to the service layer.
    """
    result = schedule_submission(data)
    return result

















