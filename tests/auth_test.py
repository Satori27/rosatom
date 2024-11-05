import pytest
from httpx import AsyncClient

from app.main import app
from tests.models import TestUsersDAO

import pytest
from httpx import AsyncClient, ASGITransport
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_register_user():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test", follow_redirects=False) as client:
        registration_test_cases = [
            {
                "input": {
                    "email": "user@example.com",
                    "password": "string",
                    "password_check": "string",
                    "name": "John Doe"
                },
                "expected_status": 200,
            },
            {
                "input": {
                    "email": "user@example.com",
                    "password": "string",
                    "password_check": "different",
                    "name": "John Doe"
                },
                "expected_status": 409,
            },
            {
                "input": {
                    "email": "invalid-email",
                    "password": "string",
                    "password_check": "string",
                    "name": "John Doe"
                },
                "expected_status": 422,
            },
            {
                "input": {
                    "email": "user2@example.com",
                    "password": "short",
                    "password_check": "short",
                    "name": "Jane Doe"
                },
                "expected_status": 200,

            }
        ]
        for data in registration_test_cases:
            response = await client.post("/auth/register/", json=data["input"])

            assert response.status_code == data["expected_status"]

            if response.status_code == 200:
                await TestUsersDAO.delete_user(data["input"]["name"])
