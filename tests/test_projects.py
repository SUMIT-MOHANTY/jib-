import pytest
import json
from datetime import datetime
from app.models.contact import db
from app.models.projects import Project

@pytest.fixture
def sample_project(app):
    with app.app_context():
        project = Project(title="Test Project", description="Description", technologies=["Python"], url="http://test.com")
        db.session.add(project)
        db.session.commit()
        return project.id

class TestProjectsAPI:
    def test_get_all_projects_empty(self, client):
        response = client.get("/api/projects")
        assert response.status_code == 200
        assert response.json == []

    def test_get_all_projects_with_data(self, client, app, sample_project):
        with app.app_context():
            response = client.get("/api/projects")
            assert response.status_code == 200
            data = response.json
            assert len(data) == 1
            assert data[0]["title"] == "Test Project"

    def test_get_single_project(self, client, app, sample_project):
        with app.app_context():
            response = client.get(f"/api/projects/{sample_project}")
            assert response.status_code == 200
            assert response.json["title"] == "Test Project"

    def test_get_single_project_not_found(self, client):
        response = client.get("/api/projects/999")
        assert response.status_code == 404

    def test_create_project_success(self, client, app):
        payload = {"title": "New Project", "description": "New desc", "technologies": ["JS"], "url": "http://new.com"}
        response = client.post("/api/projects", json=payload)
        assert response.status_code == 201
        with app.app_context():
            assert Project.query.first().title == "New Project"

    def test_create_project_validation_error(self, client):
        response = client.post("/api/projects", json={"title": ""})
        assert response.status_code == 400

    def test_update_project_success(self, client, app, sample_project):
        payload = {"title": "Updated", "description": "Updated desc"}
        response = client.put(f"/api/projects/{sample_project}", json=payload)
        assert response.status_code == 200
        with app.app_context():
            assert Project.query.get(sample_project).title == "Updated"

    def test_update_project_not_found(self, client):
        response = client.put("/api/projects/999", json={"title": "Test"})
        assert response.status_code == 404

    def test_delete_project_success(self, client, app, sample_project):
        response = client.delete(f"/api/projects/{sample_project}")
        assert response.status_code == 204
        with app.app_context():
            assert Project.query.get(sample_project) is None

    def test_delete_project_not_found(self, client):
        response = client.delete("/api/projects/999")
        assert response.status_code == 404

    def test_method_not_allowed(self, client):
        response = client.delete("/api/projects")
        assert response.status_code == 405
