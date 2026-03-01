from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


from .project import Project
from .about import About
from .blog import BlogPost
from .contact import ContactSubmission

__all__ = ['db', 'Project', 'About', 'BlogPost', 'ContactSubmission']
