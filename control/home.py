from flask import Flask , render_template , request , flash ,redirect , url_for
from ext import db
from werkzeug.security import check_password_hash
from flask_login import login_user , logout_user , current_user
from model import User , Post
from form import loginuse

class Home():

    def __init__(self):
        pass

    def home(self):
        page = request.args.get('page' , default= 1 , type=int)
        post = Post.query.paginate(page=page , per_page=4)
        return render_template('home.html' , posts = post)


    def login(self):
        form = loginuse()
        if request.method == 'POST':
            if form.validate_on_submit():
                email = request.form['email']
                password = request.form['password']
                user = User.query.filter_by(email = email).first()
                if user:
                    if check_password_hash(user.password , password):
                        login_user(user)
                        return redirect(url_for('home'))
                    else:
                        flash('ایمیل یا رمز عبور اشتباه است' , 'danger')
                else:
                    flash('کاربر با مشخصات بالا وجود ندارد' , 'danger')
                    return redirect(url_for('login'))
                

        return render_template('login.html' , form = form)
    
    def logout(self):
        if request.method == 'POST':
            logout_user()
            return redirect(url_for('home'))















