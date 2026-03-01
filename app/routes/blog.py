from flask import Blueprint, request, jsonify
from datetime import datetime
from app.models import db, BlogPost

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/api/blog', methods=['GET'])
def get_blog_posts():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return jsonify([p.to_dict() for p in posts]), 200


@blog_bp.route('/api/blog', methods=['POST'])
def create_blog_post():
    data = request.get_json()
    post = BlogPost(
        title=data.get('title'),
        slug=data.get('slug'),
        content=data.get('content'),
        excerpt=data.get('excerpt'),
        featured_image=data.get('featured_image'),
        author=data.get('author'),
        tags=data.get('tags'),
        published=data.get('published', False),
        published_at=datetime.utcnow() if data.get('published') else None
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201


@blog_bp.route('/api/blog/<slug>', methods=['GET'])
def get_blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return jsonify(post.to_dict()), 200


@blog_bp.route('/api/blog/<slug>', methods=['PUT'])
def update_blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.slug = data.get('slug', post.slug)
    post.content = data.get('content', post.content)
    post.excerpt = data.get('excerpt', post.excerpt)
    post.featured_image = data.get('featured_image', post.featured_image)
    post.author = data.get('author', post.author)
    post.tags = data.get('tags', post.tags)
    post.published = data.get('published', post.published)
    if data.get('published') and not post.published_at:
        post.published_at = datetime.utcnow()
    db.session.commit()
    return jsonify(post.to_dict()), 200


@blog_bp.route('/api/blog/<slug>', methods=['DELETE'])
def delete_blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return '', 204
