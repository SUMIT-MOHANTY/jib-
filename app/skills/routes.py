from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import db, Skill

skills_bp = Blueprint('skills', __name__)

@skills_bp.route('')
@login_required
def list():
    skills = Skill.query.all()
    return render_template('skills/list.html', skills=skills)

@skills_bp.route('', methods=['POST'])
@login_required
def create():
    skill = Skill(
        name=request.form['name'],
        category=request.form.get('category', 'general'),
        proficiency=int(request.form.get('proficiency', 50))
    )
    db.session.add(skill)
    db.session.commit()
    flash('Skill created successfully', 'success')
    return redirect(url_for('skills.list'))

@skills_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    flash('Skill deleted successfully', 'success')
    return redirect(url_for('skills.list'))
