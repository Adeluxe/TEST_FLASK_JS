from app import db
from app.models import Service

db.create_all()
one = Service(555,1,'Capital', 12523, 'Vault', 'Tier', 0, 100, 5, 200, 4, 300, 3, 400, 2)
one.save_to_db()
two = Service(555,2,'Market', 12543, 'HHmm', 'Flat', 55, 0, 0,0, 0, 0, 0, 0, 0)
two.save_to_db()