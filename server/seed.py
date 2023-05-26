from app import app
from models import db, Student, Teacher, Review

with app.app_context(): 
    
    student1 = Student(name = "Yinson", phase= 4, email= "yson@gmail.com", superhero_partner = "Doomslayer")
    student2 = Student(name = "Sarah", phase=4, email="sarah@yahoo.com", superhero_partner = "Avatar")
    student3 = Student(name="Harrison", phase=3, email="hson@gmail.com", superhero_partner = "John Snow")
    db.session.add_all([student1, student2, student3])
    db.session.commit()
    
    teacher1 = Teacher(name="Mohammad", favorite_language = "JavaScript", email = "mohammad.hossain@flatironschool.com", favorite_food = "Coke zero")
    teacher2 = Teacher(name="Kash", favorite_language = "Python", email="kash@gmail.com", favorite_food = "Meal prep")
    teacher3 = Teacher(name="Ricardo", favorite_language = "JavaScript", email = "ricardo@gmail.com", favorite_food = "Pizza")
    db.session.add_all([teacher1, teacher2, teacher3])
    db.session.commit()
    
    review1 = Review(content= "Meh", rating=4.1, student_id = 1, teacher_id = 1)
    review2 = Review(content = "Superb", rating = 4.9, student_id = 1, teacher_id = 2)
    review3 = Review(content = "Learned a lot", rating = 4.5, student_id = 3, teacher_id = 3)
    db.session.add_all([review1, review2, review3])
    db.session.commit()