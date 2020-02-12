from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

# Index page below
@app.route('/')
@app.route('/index')
def index():
  user = { 'first_name': 'Ashik' }
  posts = [
    {
      'author': {'user_name': 'Ashik'},
      'body': 'First day in portland'
    },
    {
      'author': {'user_name': 'Ajil'},
      'body': 'I wanna watch a movie'
    }
  ]
  return render_template('index.html', title='Cyber Crisis', user=user, posts=posts)

# Login in form below
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested')
    return redirect('/index')
  return render_template('login.html', title='Sign In', form=form)

