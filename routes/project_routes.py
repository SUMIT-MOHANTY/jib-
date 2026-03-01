from flask import Blueprint, jsonify, request
from schemas import ma, project_schema, projects_schema, project_create_schema, project_update_schema
from services.project_service import ProjectService

project_bp = Blueprint('project_bp', __name__, url_prefix='/api/projects')

@project_bp.route('', methods=['GET'])
def get_projects():
    projects = ProjectService.get_all()
    return jsonify({'projects': projects_schema.dump(projects)}), 200

@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = ProjectService.get_by_id(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify({'project': project_schema.dump(project)}), 200

@project_bp.route('', methods=['POST'])
def create_project():
    data = request.get_json()
    errors = project_create_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400
    project = ProjectService.create(data)
    return jsonify({'project': project_schema.dump(project)}), 201

@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = ProjectService.get_by_id(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    data = request.get_json()
    errors = project_update_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400
    project = ProjectService.update(project, data)
    return jsonify({'project': project_schema.dump(project)}), 200

@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = ProjectService.get_by_id(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    ProjectService.delete(project)
    return jsonify({'message': 'Project deleted'}), 200
