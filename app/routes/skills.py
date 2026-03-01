from flask import Blueprint, request, jsonify
from app.services import skills_service

skills_bp = Blueprint('skills', __name__)

@skills_bp.route('/api/skills', methods=['GET'])
def get_skills():
    skills = skills_service.get_all_skills()
    return jsonify({
        'success': True,
        'data': skills,
        'count': len(skills)
    })

@skills_bp.route('/api/skills/<category>', methods=['GET'])
def get_skills_by_category(category):
    skills = skills_service.get_skills_by_category(category)
    return jsonify({
        'success': True,
        'data': skills,
        'count': len(skills)
    })

@skills_bp.route('/api/skills', methods=['POST'])
def create_skill():
    data = request.get_json()
    
    if not data or 'name' not in data or 'category' not in data:
        return jsonify({
            'success': False,
            'error': 'name and category are required'
        }), 400
    
    skill = skills_service.create_skill(data)
    return jsonify({
        'success': True,
        'data': skill
    }), 201

@skills_bp.route('/api/skills/<int:skill_id>', methods=['PUT'])
def update_skill(skill_id):
    data = request.get_json()
    
    if not data:
        return jsonify({
            'success': False,
            'error': 'No data provided'
        }), 400
    
    skill = skills_service.update_skill(skill_id, data)
    
    if not skill:
        return jsonify({
            'success': False,
            'error': 'Skill not found'
        }), 404
    
    return jsonify({
        'success': True,
        'data': skill
    })

def register_routes(app):
    app.register_blueprint(skills_bp)
