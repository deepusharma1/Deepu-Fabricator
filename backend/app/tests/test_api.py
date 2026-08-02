# backend/tests/test_api.py

from fastapi import status


# -----------------------------------
# Root API Health Check Test
# -----------------------------------

def test_read_root_endpoint(client):

    """
    Verify application health status.
    """

    response = client.get("/")


    assert response.status_code == status.HTTP_200_OK


    data = response.json()


    assert data["status"] == "online"



# -----------------------------------
# Contact API Test
# -----------------------------------

def test_contact_form_submission(client):

    """
    Verify customer contact form submission flow.
    """

    payload = {

        "fullName": "Test User",

        "mobileNumber": "9999999999",

        "emailAddress": "test@example.com",

        "requirementType": "Steel Gate / Grill",

        "message": "Automated unit test inquiry message."

    }


    response = client.post(
        "/api/contact/",
        json=payload
    )


    assert response.status_code in [
        status.HTTP_200_OK,
        status.HTTP_201_CREATED
    ]


    data = response.json()


    assert data["status"] == "success"



# -----------------------------------
# Authentication Security Test
# -----------------------------------

def test_admin_auth_security_barrier(client):

    """
    Verify invalid credentials are rejected.
    """

    invalid_payload = {

        "username": "unauthorized_user",

        "password": "wrong_password_xyz"

    }


    response = client.post(
        "/api/auth/login",
        json=invalid_payload
    )


    assert response.status_code == status.HTTP_401_UNAUTHORIZED