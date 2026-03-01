from flask import Blueprint, request, jsonify
from app.models import db, Project

projects_bp = Blueprint('projects', __name__)


@projects_bp.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([p.to_dict() for p in projects]), 200


@projects_bp.route('/api/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Project(
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        tech_stack=data.get('tech_stack'),
        github_url=data.get('github_url'),
        live_url=data.get('live_url')
    )
    db.session.add(project)
    db.session.commit()
    return jsonify(project.to_dict()), 201


@projects_bp.route('/api/projects/<int:id>', methods=['GET'])
def get_project(id):
    project = Project.query.get_or_404(id)
    return jsonify(project.to_dict()), 200


@projects_bp.route('/api/projects/<int:id>', methods=['PUT'])
def update_project(id):
    project = Project.query.get_or_404(id)
    data = request.get_json()
    project.title = data.get('title', project.title)
    project.description = data.get('description', project.description)
    project.image_url = data.get('image_url', project.image_url)
    project.tech_stack = data.get('tech_stack', project.tech_stack)
    project.github_url = data.get('github_url', project.github_url)
    project.live_url = data.get('live_url', project.live_url)
    db.session.commit()
    return jsonify(project.to_dict()), 200


@projects_bp.route('/api/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return '', 204
