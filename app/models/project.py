from app import db
import json

class Project(db.Model):
    __tablename__ = "projects"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)
    tech_tags = db.Column(db.Text, nullable=True)  # Stored as JSON string
    demo_url = db.Column(db.String(500), nullable=True)
    github_url = db.Column(db.String(500), nullable=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image_url": self.image_url,
            "tech_tags": json.loads(self.tech_tags) if self.tech_tags else [],
            "demo_url": self.demo_url,
            "github_url": self.github_url
        }
    
    # Property for getting/setting tech_tags as list
    @property
    def tags_list(self):
        return json.loads(self.tech_tags) if self.tech_tags else []
    
    @tags_list.setter
    def tags_list(self, value):
        self.tech_tags = json.dumps(value) if value else "[]"
