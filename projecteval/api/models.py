from projecteval import db

class Base(db.Model):
	__abstract__ = True

 	id = db.Column(db.Integer, primary_key=True)

class Game(Base):
	__tablename__ = 'game'

 	title = db.Column(db.String(128), nullable=False)
 	release_date = db.Column(db.DateTime)
 	desc = db.Column(db.String(1000), nullable=False)
 	developer = db.Column(db.String(128))
 	publisher = db.Column(db.String(128))
 	trailer_url = db.Column(db.String(128))
 	esrb_id = db.Column(db.Integer)
 	genre_id = db.Column(db.Integer)
 	added_by = db.Column(db.String(128), nullable=False)
 	date_added = db.Column(db.DateTime, default=db.func.current_timestamp())
 	last_modified_by = db.Column(db.String(128), nullable=False)
 	last_modified = db.Column(db.DateTime, default=db.func.current_timestamp())

def __init__(self, title, desc, developer, publisher, trailer_url, added_by, last_modified_by):
	self.title = title
	self.desc = desc
	self.developer = developer
	self.publisher = publisher
	self.trailer_url = trailer_url
	self.added_by = added_by
	self.last_modified_by = last_modified_by

def __repr__(self):
	return '<Game %s>' % (self.title)

class Platform(Base):
	__tablename__ = 'platform'

	name = db.Column(db.String(128), nullable=False)
	release_date = db.Column(db.DateTime)
	desc = db.Column(db.String(1000), nullable=False)
	developer = db.Column(db.String(128))
	manufacturer = db.Column(db.String(128))
	cpu = db.Column(db.String(128))
	memory = db.Column(db.String(128))
	graphics = db.Column(db.String(128))
	storage = db.Column(db.String(128))
	added_by = db.Column(db.String(128), nullable=False)
	date_added = db.Column(db.DateTime, default=db.func.current_timestamp())
	last_modified_by = db.Column(db.String(128), nullable=False)
	last_modified = db.Column(db.DateTime, default=db.func.current_timestamp())

	def __init__(self, name, desc, developer, manufacturer, cpu, memory, graphics, storage):
		self.name = name
		self.desc = desc
		self.developer = developer
		self.manufacturer = manufacturer
		self.cpu = cpu
		self.memory = memory
		self.graphics = graphics
		self.storage = storage

	def __repr__(self):
		return '<Platform %s>' % (self.name)		