from datetime import datetime, date

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pytz

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://satoki:password@localhost:8080/mydatabase"
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    due = db.Column(db.String(30))

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template("test.html", posts=posts)
    else:
        return redirect('/')

@app.route('/create', methods=("GET", "POST"))
def create():
    if request.method == 'POST':
        text = request.form.get("text")
        due = datetime.now(pytz.timezone('Asia/Tokyo'))

        due = due.strftime("%Y-%m-%d %H:%M")

        new_post = Post(text=text, due=due)
        
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("create.html")

if __name__ == '__main__' :
    app.run()