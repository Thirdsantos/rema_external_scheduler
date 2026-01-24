from sqlalchemy import create_engine

from .config import DATABASE_URL


engine = create_engine(DATABASE_URL)


def get_engine():
    """
    Simple accessor for the SQLAlchemy engine.

    This keeps the rest of the code decoupled from how the engine is created.
    """
    return engine


