# backend/tests/conftest.py

import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.connection import Base, get_db
from app.main import app


# -----------------------------------
# Test Database Configuration
# -----------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# -----------------------------------
# Override Database Dependency
# -----------------------------------

def override_get_db():

    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()



# -----------------------------------
# Database Setup / Cleanup
# -----------------------------------

@pytest.fixture(
    scope="function",
    autouse=True
)
def setup_database():

    # Create test tables
    Base.metadata.create_all(
        bind=engine
    )


    # Replace production DB
    app.dependency_overrides[get_db] = override_get_db


    yield


    # Remove overrides
    app.dependency_overrides.clear()


    # Drop test tables
    Base.metadata.drop_all(
        bind=engine
    )



# -----------------------------------
# API Test Client
# -----------------------------------

@pytest.fixture(
    scope="function"
)
def client():

    with TestClient(app) as test_client:

        yield test_client