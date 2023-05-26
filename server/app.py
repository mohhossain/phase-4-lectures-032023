# 1. install Flask library 
from flask import Flask
from flask_restful import Api, Resource, request

from flask_migrate import Migrate

from models import db, Student, Teacher, Review

# 2. creating the flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate(app, db)

db.init_app(app)


api = Api(app)

# student/teacher/review

@app.route("/")
def index():
    return {"message": "Hello World!"}

class Students(Resource):
    
    def get(self):
        students = [ {
            "name": s.name, 
            "phase": s.phase
        } for s in Student.query.all() ]
        
        
        return students, 200
    
    def post(self): 
        student = Student(
            name = request.json['name'],
            phase = request.json['phase'],
            email = request.json['email'],
            superhero_partner = request.json['superhero_partner'])
        
        
    
        db.session.add(student)
        db.session.commit()
        
        return {"name": student.name, "phase": student.phase}, 201
    
api.add_resource(Students, "/students")


