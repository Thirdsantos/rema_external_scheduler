from datetime import datetime
from typing import List
from pydantic import BaseModel


class DocumentDetails(BaseModel):
    department_id: int
    submission_id: str


class SubmissionDetails(BaseModel):
    name: str
    email: str
    transaction_id: str
    start_datetime: datetime
    end_datetime: datetime
    documents: List[DocumentDetails]