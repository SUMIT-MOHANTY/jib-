from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import db, About

about_bp = Blueprint('about', __name__)

@about_bp.route('')
@login_required
def edit():
    about = About.query.first()
    if not about:
        about = About(content='')
        db.session.add(about)
        db.session.commit()
    return render_template('about/edit.html', about=about)

@about_bp.route('', methods=['POST'])
@login_required
def update():
    about = About.query.first()
    if not about:
        about = About(content=request.form['content'])
        db.session.add(about)
    else:
        about.content = request.form['content']
    db.session.commit()
    flash('About content updated successfully', 'success')
    return redirect(url_for('about.edit'))
