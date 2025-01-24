from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    images = db.relationship('Image', backref='category', lazy=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String(50))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
            
        user = User(username=username,
                   password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        return redirect(url_for('gallery'))
        
    return render_template('register.html')

@app.route('/admin/upload', methods=['GET', 'POST'])
@login_required
def admin_upload():
    if not current_user.is_admin:
        return redirect(url_for('gallery'))
        
    if request.method == 'POST':
        category_id = request.form['category']
        number = request.form['number']
        file = request.files['image']
        
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            image = Image(filename=filename,
                         number=number,
                         category_id=category_id,
                         uploaded_by=current_user.id)
            db.session.add(image)
            db.session.commit()
            
    categories = Category.query.all()
    return render_template('admin_upload.html', categories=categories)

@app.route('/gallery')
@login_required
def gallery():
    category_id = request.args.get('category')
    if category_id:
        images = Image.query.filter_by(category_id=category_id).all()
    else:
        images = Image.query.all()
    categories = Category.query.all()
    return render_template('gallery.html', images=images, categories=categories) 