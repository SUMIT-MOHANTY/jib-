import pytest
import json
from app.models.contact import db
from app.models.skills import Skill

@pytest.fixture
def sample_skill(app):
    with app.app_context():
        skill = Skill(name="Python", category="backend", proficiency=90)
        db.session.add(skill)
        db.session.commit()
        return skill.id

class TestSkillsAPI:
    def test_get_all_skills_empty(self, client):
        response = client.get("/api/skills")
        assert response.status_code == 200
        assert response.json == []

    def test_get_all_skills_with_data(self, client, app, sample_skill):
        with app.app_context():
            response = client.get("/api/skills")
            assert response.status_code == 200
            assert len(response.json) == 1

    def test_get_single_skill(self, client, app, sample_skill):
        with app.app_context():
            response = client.get(f"/api/skills/{sample_skill}")
            assert response.status_code == 200
            assert response.json["name"] == "Python"

    def test_get_single_skill_not_found(self, client):
        response = client.get("/api/skills/999")
        assert response.status_code == 404

    def test_create_skill_success(self, client, app):
        payload = {"name": "JavaScript", "category": "frontend", "proficiency": 85}
        response = client.post("/api/skills", json=payload)
        assert response.status_code == 201
        with app.app_context():
            assert Skill.query.first().name == "JavaScript"

    def test_create_skill_validation_error(self, client):
        payload = {"name": ""}
        response = client.post("/api/skills", json=payload)
        assert response.status_code == 400

    def test_create_skill_proficiency_bounds(self, client, app):
        payload = {"name": "Test", "category": "test", "proficiency": 150}
        response = client.post("/api/skills", json=payload)
        assert response.status_code == 400

    def test_update_skill_success(self, client, app, sample_skill):
        payload = {"name": "Updated Python", "proficiency": 95}
        response = client.put(f"/api/skills/{sample_skill}", json=payload)
        assert response.status_code == 200
        with app.app_context():
            assert Skill.query.get(sample_skill).name == "Updated Python"

    def test_update_skill_not_found(self, client):
        response = client.put("/api/skills/999", json={"name": "Test"})
        assert response.status_code == 404

    def test_delete_skill_success(self, client, app, sample_skill):
        response = client.delete(f"/api/skills/{sample_skill}")
        assert response.status_code == 204
        with app.app_context():
            assert Skill.query.get(sample_skill) is None

    def test_delete_skill_not_found(self, client):
        response = client.delete("/api/skills/999")
        assert response.status_code == 404
