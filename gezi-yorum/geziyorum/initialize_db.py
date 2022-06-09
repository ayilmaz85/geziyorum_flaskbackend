from geziyorum.models import db
from geziyorum import createApp


def createDB():
    db.create_all(app=createApp())


