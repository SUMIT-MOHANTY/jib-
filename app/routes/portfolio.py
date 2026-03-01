from flask import Blueprint, request, jsonify
from app.services.portfolio_service import PortfolioService

portfolio_bp = Blueprint("portfolio", __name__)
service = PortfolioService()

@portfolio_bp.route("/projects", methods=["GET"])
def get_all_projects():
    projects = service.get_all()
    return jsonify([p.to_dict() for p in projects])

@portfolio_bp.route("/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    project = service.get_by_id(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project.to_dict())

@portfolio_bp.route("/projects", methods=["POST"])
def create_project():
    data = request.get_json()
    project = service.create(data)
    return jsonify(project.to_dict()), 201

@portfolio_bp.route("/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    data = request.get_json()
    project = service.update(project_id, data)
    if not project:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project.to_dict())

@portfolio_bp.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    success = service.delete(project_id)
    if not success:
        return jsonify({"error": "Project not found"}), 404
    return "", 204
