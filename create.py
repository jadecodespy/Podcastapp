from application import db
from application.models import Topics, Podcast 

db.drop_all()

db.create_all()
