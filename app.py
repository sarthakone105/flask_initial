from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from datetime import datetime

app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self) -> str:
        return f"Task {self.id}"



# # Home page
# @app.route("/", methods=["POST", "GET"])
# def index():
#     # add task
#     if request.method == "POST":
#         current_task = request.form['content']
#         new_task = MyTask(content=current_task)
        
#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect("/")
        
#         except Exception as e:
#             print(f"Error:{e}")
#             return f"Error:{e}"
    
    
#     else:
#         tasks = MyTask.query.order_by(MyTask.created).all()
#         return render_template('index.html', task=tasks)
    

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            print("Task added:", current_task)  # Debugging line
            return redirect("/")
        
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"
    
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        print("Tasks fetched:", tasks)  # Debugging line
        return render_template('index.html', tasks=tasks)

    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5353)
