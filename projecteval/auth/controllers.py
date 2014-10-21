from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from werkzeug import check_password_hash, generate_password_hash

from projecteval import db

from projecteval.auth.forms import LoginForm

from projecteval.auth.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login():
	
	form = LoginForm(request.form)

	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()

		if user and check_password_hash(user.password, form.password.data):
			session['user_id'] = user.id

			flash('Welcome %s' % user.username)

			return redirect(url_for('auth.home'))

		flash('Wrong email or password', 'error-message')

	return render_template("auth/login.html", form=form)
