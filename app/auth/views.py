from flask import render_template,redirect,url_for,request,flash
from . import auth
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db

# registration route
@auth.route('templates/auth/reqister',methods=['GET','POST'])
def register():
    '''
    function that registaers the users
    '''
    form =RegistrationForm()
    if form.validate_on_submit():
        user =User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    title="Registration"
    return render_template('auth/register.html',registration_form=form,title=title)