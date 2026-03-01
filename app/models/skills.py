from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    proficiency = db.Column(db.Integer, default=0)
    icon = db.Column(db.Text, default='')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'proficiency': self.proficiency,
            'icon': self.icon
        }
