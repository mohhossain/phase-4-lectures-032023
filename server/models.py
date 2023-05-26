# 1. install and import flask_sqlalchemy 

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
db = SQLAlchemy()

# student/teacher/review
# Student has many review

# Teacher has many review

# Each review belongs to a student and a teacher

# student -> id, name, phase, email, superhero_partner, created_at, updated_at
# teacher -> id, name, favorite_language, email, favorite_food, created_at, updated_at

# review -> id, content, rating, student_id, teacher_id, created_at, updated_at

class Student(db.Model):
    __tablename__ = "students"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    phase = db.Column(db.Integer)
    email = db.Column(db.String)
    superhero_partner = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    reviews = db.relationship("Review", backref = "student")
    
    def __repr__(self):
        print(f"<Student name={self.name} phase={self.phase}>")
        
class Teacher(db.Model):
    __tablename__ = "teachers"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    favorite_language = db.Column(db.String)
    email = db.Column(db.String)
    favorite_food = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    reviews = db.relationship("Review", backref = "teacher")
    
    
    def __repr__(self):
        print(f"<Teacher name={self.name} favorite_language={self.favorite_language}>")
        
class Review(db.Model):
    
    __tablename__ = "reviews"
    
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    rating = db.Column(db.Float)
    
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    
    def __repr__(self):
        print(f"<Teacher content={self.content} rating={self.rating} student_id={self.student_id} teacher_id={self.teacher_id}>")