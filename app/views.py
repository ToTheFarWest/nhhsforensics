from flask import render_template, session, flash, redirect, request
from app import app
from .users.UserForms import LoginForm, RegisterForm
from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from .extensions import db, login_manager, csrf

def configure_extensions(app):  
   # flask-sqlalchemy
   db.init_app(app)

   ## flask-login
   #login_manager.login_view = 'frontend.index'
   #login_manager.refresh_view = 'frontend.index'

   @login_manager.user_loader
   def load_user(id):
      return User.query.get(int(id))

   login_manager.setup_app(app)

   # flask-wtf
   #csrf(app)
configure_extensions(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                            title='Home')
@app.route('/signup')
@login_required
def signup():
    return render_template('signup.html',
                            title="Signup")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate() == False:
#        return "RIP registration error"
        flash('Registration error')
    elif request.method == 'POST' and form.validate():
        username = form.user_name.data
        email = form.email.data
        password

    elif request.method == 'GET':
        return render_template('register.html',
                                title="Register",
                                form=form) 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for username="%s", remember_me="%s"' % (form.username.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title="Login",
                            form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/index")
