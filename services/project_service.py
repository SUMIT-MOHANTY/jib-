from models import db, Project

class ProjectService:
    @staticmethod
    def get_all():
        return Project.query.order_by(Project.created_at.desc()).all()

    @staticmethod
    def get_by_id(project_id):
        return Project.query.get(project_id)

    @staticmethod
    def create(data):
        project = Project(
            title=data.get('title'),
            description=data.get('description'),
            image_url=data.get('image_url'),
            tech_tags=data.get('tech_tags')
        )
        db.session.add(project)
        db.session.commit()
        return project

    @staticmethod
    def update(project, data):
        if 'title' in data:
            project.title = data['title']
        if 'description' in data:
            project.description = data['description']
        if 'image_url' in data:
            project.image_url = data['image_url']
        if 'tech_tags' in data:
            project.tech_tags = data['tech_tags']
        db.session.commit()
        return project

    @staticmethod
    def delete(project):
        db.session.delete(project)
        db.session.commit()
