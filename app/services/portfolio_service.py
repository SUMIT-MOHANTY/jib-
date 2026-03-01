from app import db
from app.models.project import Project

class PortfolioService:
    def get_all(self):
        return Project.query.all()
    
    def get_by_id(self, project_id):
        return Project.query.get(project_id)
    
    def create(self, data):
        project = Project(
            title=data.get("title"),
            description=data.get("description"),
            image_url=data.get("image_url"),
            tech_tags=data.get("tech_tags", []),
            demo_url=data.get("demo_url"),
            github_url=data.get("github_url")
        )
        db.session.add(project)
        db.session.commit()
        return project
    
    def update(self, project_id, data):
        project = self.get_by_id(project_id)
        if not project:
            return None
        for key, value in data.items():
            if hasattr(project, key):
                setattr(project, key, value)
        db.session.commit()
        return project
    
    def delete(self, project_id):
        project = self.get_by_id(project_id)
        if not project:
            return False
        db.session.delete(project)
        db.session.commit()
        return True
