from typing import Any

from sqlalchemy.orm import Session

from ..database import get_engine
from ..schemas import SubmissionDetails
from ..models.models import Users, TransactionSchedule, SubmissionSchedule


def get_sessions() -> Session:
    """
    FastAPI dependency that yields a database session.
    """
    with Session(get_engine()) as session:
        yield session


class UserSubmission:
    """
    Coordinates the creation of users, transactions, and submissions
    for a given submission payload.
    """

    def __init__(self, session: Session, data: SubmissionDetails):
        self.session = session
        self.data = data

    def add_user(self) -> Users:
        existing_user = (
            self.session.query(Users)
            .filter(Users.email == self.data.email)
            .first()
        )

        if not existing_user:
            new_user = Users(name=self.data.name, email=self.data.email)
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)
            return new_user

        return existing_user

    def add_transaction(self) -> TransactionSchedule:
        user = self.add_user()

        new_transaction = TransactionSchedule(
            user_id=user.id,
            transaction_id=self.data.transaction_id,
            start_time=self.data.start_datetime,
            end_time=self.data.end_datetime,
        )
        self.session.add(new_transaction)
        self.session.commit()
        self.session.refresh(new_transaction)

        return new_transaction

    def add_submission(self) -> None:
        transaction = self.add_transaction()
        documents = self.data.documents

        for docu in documents:
            add_docu = SubmissionSchedule(
                transaction_id=transaction.transaction_id,
                user_id=transaction.user_id,
                department_id=docu.department_id,
                submission_id=docu.submission_id,
            )
            self.session.add(add_docu)

        self.session.commit()
