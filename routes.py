# routes.py
from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import User, Recipe, Comment
from forms import LoginForm, SignupForm, CommentForm, RatingForm
from flask_login import login_user, current_user, logout_user, login_required

# Home page route
@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

# Recipe detail route
@app.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(content=comment_form.content.data, recipe_id=recipe_id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
        return redirect(url_for('recipe_detail', recipe_id=recipe_id))
    return render_template('recipe.html', recipe=recipe, comment_form=comment_form)

# Recipes route
@app.route('/recipes')
def recipes():
    recipes = Recipe.query.all()
    return render_template('recipes.html', recipes=recipes)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', form=form)

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

# Logout route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Error handling route for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handling route for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
