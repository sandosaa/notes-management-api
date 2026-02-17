from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

# --- TEACHING: DATABASE CONFIGURATION ---
# We use SQLite as our primary database because it is a file-based database
# No Server required
# sqlmodel is a Python library that provides a simple and intuitive way to interact with databases using SQLAlchemy.
# and it's shit.
# either sqlite or sqlmodel requires zero configuration, making it perfect for development phase.
# The URL "sqlite:///./database.db" tells SQLModel to create a file named
# 'database.db' in the current project directory.
DATABASE_URL = "sqlite:///./database.db"

# --- TIP: ENGINE CREATION ---
# The 'engine' is the bridge between Python and the database file.
# We set 'connect_args={"check_same_thread": False}' because SQLite by default
# prevents multiple threads from using the same connection. FastAPI handles
# requests in multiple threads, so we disable this check to allow concurrent access.
# we already had a deep conversation about this before.
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})


def init_db() -> None:
    """
    TIP: DATABASE INITIALIZATION
    This function uses SQLModel's metadata to look at all classes we've defined
    inheriting from 'SQLModel' and with 'table=True'. It then automatically
    generates the SQL 'CREATE TABLE' statements needed to build our schema.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    TEACHING: SESSION MANAGEMENT (DEPENDENCY INJECTION) "VIP CONCEPT" PLEASE UNDERSTAND DEEEEPLY!!.
    A 'Session' represents a single transaction or 'conversation' with the database.
    We use a 'Generator' here so FastAPI can use it as a 'Dependency'.
    1. The 'with' statement ensures the session starts.
    2. 'yield' provides the session to the service/controller that needs it.
    3. Once the request is finished, the code resumes and closes the
       session automatically.
    This pattern prevents memory leaks and ensures database connections
    are returned to the pool.
    and it's a very important concept in database management.
    """
    with Session(engine) as session:
        yield session
