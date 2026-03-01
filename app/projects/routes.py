from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import db, Project

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('')
@login_required
def list():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('projects/list.html', projects=projects)

@projects_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        project = Project(
            title=request.form['title'],
            description=request.form['description'],
            image_url=request.form.get('image_url'),
            technologies=request.form.get('technologies'),
            project_url=request.form.get('project_url')
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully', 'success')
        return redirect(url_for('projects.list'))
    return render_template('projects/form.html', project=None)

@projects_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    project = Project.query.get_or_404(id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.image_url = request.form.get('image_url')
        project.technologies = request.form.get('technologies')
        project.project_url = request.form.get('project_url')
        db.session.commit()
        flash('Project updated successfully', 'success')
        return redirect(url_for('projects.list'))
    return render_template('projects/form.html', project=project)

@projects_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully', 'success')
    return redirect(url_for('projects.list'))
