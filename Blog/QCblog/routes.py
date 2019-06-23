from flask import render_template, flash, redirect, url_for, flash, request
from QCblog.forms import RegistrationForm, LoginForm, RecipeForm, PostForm
from QCblog import app, db, bcrypt
from QCblog.models import User, Post, Recipe
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/")
@app.route("/home")
def home():
	posts=Post.query.all()
	return render_template('home.html', posts=posts)
	
@app.route("/recipepage")
def recipePage():
	recipes=Recipe.query.all()
	return render_template('recipepage.html', recipes=recipes)

	
m1="login has an error refer to video3"
@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		H_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=H_password)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title="Register", form=form)
	
@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login unseccessfull. Please check email and password', 'danger')
	return render_template('login.html', title="Login", form=form)
	
@app.route("/recipe",  methods=['GET', 'POST'])
def recipe():
	form = RecipeForm()
	if form.validate_on_submit():
		recipe = Recipe(title=form.title.data, recipe=form.recipe.data, author=current_user)
		db.session.add(recipe)
		db.session.commit()
		flash('{} recipe was added!'.format(form.title.data), 'success')
		return redirect(url_for("recipePage"))
	else:
		flash('something went wrong please check your information', 'danger')
	return render_template('recipe.html', title='Recipe', form=form, legend="Add Recipe")
	
@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))
	
@app.route("/account")
@login_required
def account():
	posts=Post.query.all()
	recipes=Recipe.query.all()
	return render_template('account.html', title='Account', posts=posts, recipes=recipes)
	
@app.route("/post", methods=['GET', 'POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title=form.title.data, content=form.post.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		flash('Your post has been added!', 'success')
		return redirect(url_for("home"))
	return render_template('post.html', title='Post', form=form, legend="New Post")
	
@app.route("/selectedpost/<id>")
def selectedpost(id):
	post=Post.query.get(id)
	return render_template('selectedpost.html', title=post.title, post=post)
	
@app.route("/updatePost<int:id>", methods=['GET', 'POST'])
@login_required
def updatePost(id):
	post=Post.query.get(id)
	form=PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.post.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':	
		form.title.data = post.title
		form.post.data = post.content
	return render_template('post.html', title='Update Post', form=form, legend="Update Post")
	
@app.route("/updateRecipe<int:id>", methods=['GET', 'POST'])
@login_required
def updateRecipe(id):
	recipe=Recipe.query.get(id)
	form=RecipeForm()
	if form.validate_on_submit():
		recipe.title = form.title.data
		recipe.recipe = form.recipe.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':	
		form.title.data = recipe.title
		form.recipe.data = recipe.recipe
	return render_template('recipe.html', title='Update Recipe', form=form, legend="Update Recipe")

@app.route("/deleteRecipe<int:id>", methods=['POST'])
@login_required
def deleteRecipe(id):
	recipe=Recipe.query.get(id)
	db.session.delete(recipe)
	db.session.commit()
	return redirect(url_for('account'))
	
@app.route("/deletePost<int:id>", methods=['POST'])
@login_required
def deletePost(id):
	post=Post.query.get(id)
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('account'))
