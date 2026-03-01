from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from app.models import Project, Skill, ContactMessage, db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    stats = {
        'total_projects': Project.query.count(),
        'total_skills': Skill.query.count(),
        'unread_messages': ContactMessage.query.count()
    }
    return render_template('dashboard/index.html', stats=stats)
