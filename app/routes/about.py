from flask import Blueprint, request, jsonify
from app.models import db, About

about_bp = Blueprint('about', __name__)


@about_bp.route('/api/about', methods=['GET'])
def get_about():
    about = About.query.first()
    if not about:
        return jsonify({'error': 'About not found'}), 404
    return jsonify(about.to_dict()), 200


@about_bp.route('/api/about', methods=['PUT'])
def update_about():
    about = About.query.first()
    data = request.get_json()
    if not about:
        about = About(
            title=data.get('title'),
            bio=data.get('bio'),
            skills=data.get('skills'),
            avatar_url=data.get('avatar_url'),
            resume_url=data.get('resume_url')
        )
        db.session.add(about)
    else:
        about.title = data.get('title', about.title)
        about.bio = data.get('bio', about.bio)
        about.skills = data.get('skills', about.skills)
        about.avatar_url = data.get('avatar_url', about.avatar_url)
        about.resume_url = data.get('resume_url', about.resume_url)
    db.session.commit()
    return jsonify(about.to_dict()), 200
