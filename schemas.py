from flask_marshmallow import Marshmallow
from models import db, Project
from marshmallow import Schema, fields, post_load

ma = Marshmallow()

class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'image_url', 'tech_tags', 'created_at', 'updated_at')
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ProjectCreateSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    image_url = fields.Str(allow_none=True)
    tech_tags = fields.List(fields.Str(), allow_none=True)

class ProjectUpdateSchema(Schema):
    title = fields.Str()
    description = fields.Str(allow_none=True)
    image_url = fields.Str(allow_none=True)
    tech_tags = fields.List(fields.Str(), allow_none=True)

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
project_create_schema = ProjectCreateSchema()
project_update_schema = ProjectUpdateSchema()
