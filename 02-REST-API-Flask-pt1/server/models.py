
from flask_sqlalchemy import SQLAlchemy
# 6. ✅ Import `SerializerMixin` from `sqlalchemy_serializer`

from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# 7. ✅ Pass `SerializerMixin` to `Productions`
class Production(db.Model, SerializerMixin):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    budget = db.Column(db.Float)
    image = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)
    ongoing = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # multiple crew members
    crew_members = db.relationship('CrewMember', backref = 'production')

    # 7.1 ✅ Create a serialize rule that will help add our `crew_members` to the response.
    serialize_only = ('id', 'title', 'director', 'ongoing', 'crew_members')
    serialize_rules = ('-crew_members.production',) 
    

    def __repr__(self):
        return f'<Production Title:{self.title}, Genre:{self.genre}, Budget:{self.budget}, Image:{self.image}, Director:{self.director},ongoing:{self.ongoing}>'

# 8. ✅ Pass `SerializerMixin` to `CrewMember`
class CrewMember(db.Model, SerializerMixin):
    __tablename__ = 'crew_members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    # foreign key
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    # 8.1 ✅ Create a serialize rule that will help add our `production` to the response.
      
    def __repr__(self):
        return f'<Production Name:{self.name}, Role:{self.role}'
    
    serialize_only = ('id', 'name', 'role')
    # serialize_rules = ('-production.crew_members',) 

 # 9. ✅ Navigate back to `app.py` for further steps.