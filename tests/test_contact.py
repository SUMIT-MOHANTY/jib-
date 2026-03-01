import pytest
import json
from app.models.contact import db
from app.models.contact import ContactSubmission

class TestContactAPI:
    def test_submit_contact_success(self, client, app, mock_email_service):
        payload = {"name": "John Doe", "email": "john@test.com", "subject": "Hello", "message": "Test message"}
        response = client.post("/api/contact", json=payload)
        assert response.status_code == 201
        with app.app_context():
            assert ContactSubmission.query.first().name == "John Doe"
        mock_email_service.assert_called_once()

    def test_submit_contact_validation_error_name_empty(self, client):
        payload = {"name": "", "email": "john@test.com", "subject": "Hello", "message": "Test"}
        response = client.post("/api/contact", json=payload)
        assert response.status_code == 400

    def test_submit_contact_validation_error_invalid_email(self, client):
        payload = {"name": "John", "email": "invalid-email", "subject": "Hello", "message": "Test"}
        response = client.post("/api/contact", json=payload)
        assert response.status_code == 400

    def test_submit_contact_validation_error_message_too_long(self, client):
        payload = {"name": "John", "email": "john@test.com", "subject": "Hello", "message": "x" * 3000}
        response = client.post("/api/contact", json=payload)
        assert response.status_code == 400

    def test_submit_contact_missing_field(self, client):
        payload = {"name": "John"}
        response = client.post("/api/contact", json=payload)
        assert response.status_code == 400

    def test_method_not_allowed(self, client):
        response = client.get("/api/contact")
        assert response.status_code == 405

    def test_submit_contact_email_failure(self, client, app):
        with pytest.mock.patch("app.services.email_service.send_notification") as mock:
            mock.return_value = False
            payload = {"name": "John", "email": "john@test.com", "subject": "Hi", "message": "Hello"}
            response = client.post("/api/contact", json=payload)
            assert response.status_code == 500
