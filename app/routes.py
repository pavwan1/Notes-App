from flask import Flask, Blueprint, render_template, url_for, flash, redirect, request
from sqlalchemy import case, desc
from app.forms import RegisterForm, LoginForm, NoteForm
from app.models import User, Note, now
from app import db, bcrypt
from flask_login import  login_user, login_required, current_user, logout_user
from datetime import datetime
import pytz
#
india = pytz.timezone('Asia/Kolkata')
now = datetime.now(india)

#START HERE
main = Blueprint('main', __name__)

@main.app_errorhandler(401)
def unauthorized_error(error):
    return render_template('login.html'), 401

@main.route("/")
def home():
    return redirect(url_for('main.login'))

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        
        new_user = User(username = form.username.data, email = form.email.data, password = hashed_pw )
        db.session.add(new_user)
        db.session.commit()
        
        flash(f'Account created for {form.username.data}!', 'success')
        
        return redirect(url_for('main.login'))
    return render_template('register.html', form= form)


@main.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            next_page=request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Login Filed, Please check email and password', 'danger')
    return render_template('login.html', form = form)


@main.route('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    form = NoteForm()
    
    if form.validate_on_submit():
        new_note = Note(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(new_note)
        db.session.commit()
        flash("Note added successfully", 'success')
        return redirect(url_for('main.dashboard'))
    
    base_query = Note.query.filter_by(user_id=current_user.id)
    
    #search logic here
    search_term = request.args.get("q", "").strip()
    
    if search_term:
        base_query= base_query.filter((Note.title.ilike(f"%{search_term}%")) | Note.content.ilike(f"%{search_term}%"))
    
    #sorting logic for note added OR note_updated    
    notes = base_query.order_by(desc(
        case(
            (Note.date_updated != None, Note.date_updated), else_= Note.date_created
            )
        )).all()
        
    return render_template('dashboard.html', form = form, notes = notes)

@main.route('/delete/<int:note_id>', methods = ['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    
    if note.author !=  current_user:
        flash("You don't have permission to delet", "danger")
        return redirect(url_for('main.dashboard'))
    
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully', 'danger')
    return redirect(url_for('main.dashboard'))

@main.route('/edit/<int:note_id>', methods=['POST', 'GET'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    print(note)
    
    if note.author != current_user:
        flash("You are not authorized to edit,", "danger")
        return redirect(url_for('main.dashboard'))
    
    form = NoteForm()
    
    if request.method=='GET':
        form.title.data = note.title
        form.content.data = note.content
        

    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        note.date_updated = now
        db.session.commit()
        flash("Note update sucessfully", 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('edit_note.html', form=form, note = note)

    
@main.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('profile.html', user = current_user)



@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.", "info")
    return redirect(url_for('main.login'))
