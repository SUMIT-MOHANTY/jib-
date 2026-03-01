import pytest
import json
from app.models.contact import db
from app.models.about import About

@pytest.fixture
def sample_about(app):
    with app.app_context():
        about = About(content="Original content", profile_image="http://img.com/profile.png")
        db.session.add(about)
        db.session.commit()
        return about.id

class TestAboutAPI:
    def test_get_about_empty(self, client):
        response = client.get("/api/about")
        assert response.status_code == 404

    def test_get_about_with_data(self, client, app, sample_about):
        with app.app_context():
            response = client.get("/api/about")
            assert response.status_code == 200
            assert "content" in response.json

    def test_update_about_success(self, client, app, sample_about):
        payload = {"content": "Updated content"}
        response = client.put("/api/about", json=payload)
        assert response.status_code == 200
        with app.app_context():
            assert About.query.first().content == "Updated content"

    def test_update_about_validation_error(self, client):
        response = client.put("/api/about", json={"content": ""})
        assert response.status_code == 400

    def test_create_about_when_none_exists(self, client, app):
        payload = {"content": "New about", "profile_image": "http://img.com/new.png"}
        response = client.put("/api/about", json=payload)
        assert response.status_code == 200

    def test_method_not_allowed(self, client):
        response = client.post("/api/about", json={"content": "test"})
        assert response.status_code == 405
        response = client.delete("/api/about")
        assert response.status_code == 405
