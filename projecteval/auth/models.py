from projecteval import db

class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)

class User(Base):
	__tablename__ = 'user'

	username = db.Column(db.String(128), nullable=False, unique=True)
	email = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(128), nullable=False)
	date_registered = db.Column(db.DateTime, default=db.func.current_timestamp())
	last_login = db.Column(db.DateTime, default=db.func.current_timestamp())
	session_id = db.Column(db.String(128))

def __init__(self, username, email, password):
	self.username = username
	self.email = email
	self.password = password

def __repr__(self):
	return '<User %r>' % (self.username)
