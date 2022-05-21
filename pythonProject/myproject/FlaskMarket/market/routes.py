from market import app
from flask import flash, render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db


@app.route('/about')
def about_page():
    return '<h1>About Page</h1>'


@app.route('/about/<username>')
def about_page_username(username):
    return f'<h1>This is About Page of {username}</h1>'


@app.route('/home')
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_form():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:  # if there are npt errors from the validators
        for err_msg in form.errors.values():
            flash(f'There is an error to create user {err_msg}', category='danger')
    return render_template('register.html', form=form)
