from flask import Flask , request , render_template , redirect , flash , url_for , send_from_directory
from ext import db
from werkzeug.utils import secure_filename
from flask_login import login_required
from model import Post 
import os

upload_photo = 'static/photo'
upload_muz = 'static/muz'


class Admin():
    
    def __init__(self):
        pass
    
    @login_required
    def add_post(self):
        if request.method == 'POST':
            titel = request.form['titel']
            text = request.form['text']
            singer = request.form['singer']
            pic = request.files['pic']
            music = request.files['music']

            sec_photo = secure_filename(pic.filename)
            sec_muz = secure_filename(music.filename)

            pic.save(os.path.join(upload_photo , sec_photo))
            music.save(os.path.join(upload_muz , sec_muz))

            post = Post(titel = titel , text = text , singer = singer , pic = f'/photo/{pic.filename}' , music = f'/muz/{music.filename}')
            post.save_slug()
            db.session.add(post)
            db.session.commit()
            flash('پست آپلود شد' , 'success')
            return redirect(url_for('add_post'))
        return render_template('add.html')



    def all_post(self):
        post = Post.query.all()
        return render_template('allpost.html' , posts = post)
    
    @login_required
    def delete(self):
        Post.query.filter_by(id = request.args.get('id')).delete()
        db.session.commit()
        flash('پست حذف شد' , 'success')
        return redirect(url_for('all_post'))
    
    @login_required
    def edit(self):
        post = Post.query.filter_by(id = request.args.get('id')).first()
        if request.method == 'POST':
            titel = request.form['titel']
            text = request.form['text']
            singer = request.form['singer']
            pic = request.files['pic']
            music = request.files['music']

            sec_photo = secure_filename(pic.filename)
            sec_muz = secure_filename(music.filename)

            pic.save(os.path.join(upload_photo , sec_photo))
            music.save(os.path.join(upload_muz , sec_muz))

            post.titel = titel
            post.text = text
            post.update_slug()
            post.singer = singer
            post.pic = f'photo/{pic.filename}'
            post.music = f'muz/{music.filename}'

            db.session.commit()
            flash('ویرایش انجام شد' , 'success')
            return redirect(url_for('edit'))

        return render_template('edit.html' , post = post)
    

    def single(self , slug):
        post = Post.query.filter_by(slug = slug).first()
        return render_template('single.html' , post = post , titel = post.titel)
    
    def dowanload(self , filename):
        return send_from_directory(upload_muz , filename , as_attachment = True)
    
    def search(self):
        if request.method == "POST":
            search = request.form['jost']
            post = Post.query.all()

            result = []

            for post in post:
                if search in post.titel or search in post.singer:
                    result.append(post)

                    return render_template('search.html' , posts = result)
    
    @login_required
    def new(self):
        if request.method == "POST":
            post = Post.query.filter_by(id = request.args.get('id')).first()
            post.new = 'newest'
            db.session.commit()
            flash('اضافه شد به جدیدترین ها' , 'success')
            return redirect(url_for('all_post'))
        return render_template('allpost.html')
    
    @login_required
    def del_new(self):
        if request.method == "POST":
            post = Post.query.filter_by(id = request.args.get('id')).first()
            post.new = ''
            db.session.commit()
            flash('پست از جدید ها حذف شد'  , 'danger')
            return redirect(url_for('all_post'))
        return render_template('allpost.html')
