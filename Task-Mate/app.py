from flask import Flask, jsonify, render_template, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secure_secret_key'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100))
    priority = db.Column(db.String(10))
    status = db.Column(db.String(50), default='Pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

CATEGORIES = [
    "Work",
    "Personal",
    "Shopping",
    "Health",
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            flash("Missing username or password", "danger")
            return redirect("/register")  
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Try a different one.", "danger")
            return render_template("register.html")  

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash("Registration successful! Please log in.", "success")
        return render_template("tasks.html")  
    return render_template("register.html")  




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            flash("Login successful!", "success")
            return redirect("/tasks")  # Redirect to tasks.html
        else:
            flash("Invalid username or password", "danger")
    
    return render_template("login.html")


@app.route("/add_task", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name")
    category = request.form.get("category")
    priority = request.form.get("priority")
    
    if not task_name or not category or not priority:
        flash("Missing task details", "danger")
        return redirect("/tasks")  # Redirect to tasks if details are missing
    
    user_id = session.get("user_id")
    if not user_id:
        flash("You must be logged in to add tasks", "danger")
        return redirect("/login")
    
    new_task = Task(task_name=task_name, category=category, priority=priority, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    
    flash("Task added successfully!", "success")
    return redirect("/tasks")

@app.route("/tasks")
def tasks():
    if "user_id" not in session:
        flash("Please log in first.", "warning")
        return redirect("/login")  # Redirect if not logged in
    
    # Here, fetch tasks for the logged-in user from the database
    user_id = session["user_id"]
    tasks = Task.query.filter_by(user_id=user_id).all()  # Get user's tasks
    return render_template("tasks.html", tasks=tasks)  # Render the tasks page with tasks


@app.route("/complete_task/<int:task_id>")
def complete_task(task_id):
    user_id = session.get("user_id")
    if not user_id:
        flash("You must be logged in to complete tasks", "danger")
        return redirect("/login")

    task = Task.query.get(task_id)
    if task and task.user_id == user_id:
        task.status = "Complete"
        db.session.commit()
        flash("Task marked as complete!", "success")
    else:
        flash("Task not found or you're not authorized to complete it.", "danger")

    return redirect("/tasks")

@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    user_id = session.get("user_id")
    if not user_id:
        flash("You must be logged in to delete tasks", "danger")
        return redirect("/login")

    task = Task.query.get(task_id)
    if task and task.user_id == user_id:
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!", "success")
    else:
        flash("Task not found or you're not authorized to delete it.", "danger")

    return redirect("/tasks")

@app.route("/check_username")
def check_username():
    username = request.args.get("username")
    user = User.query.filter_by(username=username).first()

    if user:
        return {"exists": True}
    else:
        return {"exists": False}


@app.route("/logout")
def logout():
    session.clear()  # Clear the session
    flash("Logged out successfully.", "success")
    return redirect("/")  # Redirect to the index page

@app.errorhandler(500)
def internal_error(error):
    return render_template("error.html", message="Internal Server Error"), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the tables if they don't exist
    app.run(debug=True)
