from projecteval import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from projecteval.controllers.helpers import parse_fields

class Base(db.Model):
	__abstract__ = True

 	id = db.Column(db.Integer, primary_key=True)

 	def jsonify_object(self):
 		return {}

 	def toJSON(self, fields=None):
		if fields is None or fields == '':
			return self.jsonify_object()

		parsed = parse_fields(fields)
		json = {}
		for field, subfields in parsed.items():
			v = getattr(self,field)
			if v is not None:
				if subfields == '':
					json[field] = v
				elif isinstance(v, list):
					json[field] = [item.toJSON(subfields) for item in v]
				else:
					json[field] = v.toJSON(subfields)

		return json

class Gameplatform(Base):
	__tablename__ = "gameplatform"
    
	game_id = db.Column(db.Integer, ForeignKey('game.id'))
	platform_id = db.Column(db.Integer, ForeignKey('platform.id'))
	platform = relationship('Platform', backref='game_assocs')

	def __repr__(self):
		return "<Gameplatform('%s')" % self.id

	def toJSON(self, fields=None):
		return self.platform.toJSON(fields)

class Game(Base):
	__tablename__ = 'game'

 	title = db.Column(db.String(128), nullable=False)
 	release_date = db.Column(db.DateTime)
 	desc = db.Column(db.String(1000), nullable=False)
 	developer = db.Column(db.String(128))
 	publisher = db.Column(db.String(128))
 	trailer_url = db.Column(db.String(128))
 	esrb_id = db.Column(db.Integer, ForeignKey('esrb.id'))
 	genre_id = db.Column(db.Integer)
 	added_by = db.Column(db.String(128), nullable=False)
 	date_added = db.Column(db.DateTime, default=db.func.current_timestamp())
 	last_modified_by = db.Column(db.String(128), nullable=False)
 	last_modified = db.Column(db.DateTime, default=db.func.current_timestamp())
	platforms = relationship('Gameplatform', backref='games')
	esrb = relationship('ESRB', backref='games')

	def __repr__(self):
		return '<Game %s>' % (self.title)

	def jsonify_object(self):
		platforms = []
		for gameplatform in self.platforms:
			platforms.append(gameplatform.toJSON())

		return {
    		'id': self.id,
    		'title':self.title,
    		'release_date':self.release_date,
    		'desc':self.desc,
    		'developer':self.developer,
    		'publisher':self.publisher,
    		'trailer_url':self.trailer_url,
    		'esrb_id':self.esrb_id,
    		'genre_id':self.genre_id,
    		'added_by':self.added_by,
    		'date_added':self.date_added,
    		'last_modified_by':self.last_modified_by,
    		'last_modified':self.last_modified,
    		'platforms': platforms,
    		'esrb_url': self.esrb.image_url
    	}


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

	def __repr__(self):
		return '<Platform %s>' % (self.name)

	def jsonify_object(self):
		return {
        	'id':self.id,
        	'name':self.name,
        	'release_date':self.release_date,
        	'desc':self.desc,
        	'developer':self.developer,
        	'manufacturer':self.manufacturer,
        	'cpu':self.cpu,
        	'memory':self.memory,
        	'graphics':self.graphics,
        	'storage':self.storage,
        	'added_by':self.added_by,
        	'date_added':self.date_added,
        	'last_modified_by':self.last_modified_by,
        	'last_modified':self.last_modified
    	}

class ESRB(Base):
	__tablename__ = 'esrb'	

	short_desc = db.Column(db.String(128))
	full_desc = db.Column(db.String(600))
	image_url = db.Column(db.String(128))

	def __repr__(self):
		return '<ESRB %s>' % (self.short_desc)		

class User(Base):
    __tablename__ = 'user'

    username = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    date_registered = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime, default=db.func.current_timestamp())
    session_id = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % (self.username)

    def __init__(self, username, email, password):
    	self.username = username
    	self.email = email
    	self.password = password