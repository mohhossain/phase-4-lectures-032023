#!/usr/bin/env python3

# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug

# 1. ✅ Navigate to `models.py`

# 2. ✅ Set Up Imports

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate 
from models import db, Production

# 3. ✅ Initialize the App

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  
    
    # Configure the database
    # ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'`
    # ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False` 
db.init_app(app)

 # 4. ✅ Migrate 
migrate = Migrate(app, db)


 # `cd` into the `server` folder
	
    # Run in Terminal
		# export FLASK_APP=app.py
		# export FLASK_RUN_PORT=5555
		# flask db init
		# flask db revision --autogenerate -m 'Create tables productions'
		# flask db upgrade


# 5. ✅ Navigate to `seed.py`

# 6. ✅ Routes
   

# 7. ✅ Run the server with `flask run` and verify your route in the browser at `http://localhost:5000/`

# 8. ✅ Create a dynamic route



# 9.✅ Update the route to find a `production` by its `title` and send it to our browser
    
   

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


@app.route('/')
def index():
    print("Hit the index")
    return '<h1> Welcome to our flask app </h1>'
    
@app.route('/greeting')
def greet():
    return '<h1> Good Afternoon! </h1>'


@app.route('/productions')
def get_productions():
    productions = db.session.query(Production).all()
    # serialized_productions = [production.to_dict() for production in productions ]
    # print(productions)
    
    # Define dictionary with ID and title from productions
    id_and_titles = {production.id: production.title for production in productions}
    # productions_table = {production.id: [production.title, production.genre, ...]}
    # print(id_and_titles)
    
    # response  = make_response(
    #     id_and_titles,
    #     200
    # )
    return id_and_titles, 200


