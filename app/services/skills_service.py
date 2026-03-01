from app.models.skills import db, Skill

def get_all_skills():
    skills = Skill.query.all()
    return [s.to_dict() for s in skills]

def get_skills_by_category(category):
    skills = Skill.query.filter_by(category=category).all()
    return [s.to_dict() for s in skills]

def create_skill(data):
    skill = Skill(
        name=data.get('name'),
        category=data.get('category'),
        proficiency=data.get('proficiency', 0),
        icon=data.get('icon', '')
    )
    db.session.add(skill)
    db.session.commit()
    return skill.to_dict()

def update_skill(skill_id, data):
    skill = Skill.query.get(skill_id)
    if not skill:
        return None
    
    if 'name' in data:
        skill.name = data['name']
    if 'category' in data:
        skill.category = data['category']
    if 'proficiency' in data:
        skill.proficiency = data['proficiency']
    if 'icon' in data:
        skill.icon = data['icon']
    
    db.session.commit()
    return skill.to_dict()
