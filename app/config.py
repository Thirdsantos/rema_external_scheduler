from dotenv import load_dotenv
import os

# Load environment variables from .env at startup
load_dotenv()


# Individual environment variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")


if not all([USER, PASSWORD, HOST, PORT, DBNAME]):
    # This is a soft warning; the app will still start, but DB may fail.
    # You can replace this with proper logging later.
    print("Warning: One or more database environment variables are not set.")


# Construct the SQLAlchemy connection string
DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
)


