from flask import Flask , render_template
from control import main , admin
from model import User
from flask_login import LoginManager
from ext import db
from dotenv import load_dotenv
import os

rot = os.path.dirname(__file__)
gol_rot = os.path.join(rot , 'mix.db')


app = Flask(__name__)

load_dotenv()


app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

app.config['RECAPTCHA_PUBLIC_KEY'] =  os.getenv('PUB')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.getenv('SEC')
db.init_app(app)



login_mang = LoginManager(app)
login_mang.login_view = 'login'
@login_mang.user_loader
def user_lod(user_id):
    return User.query.get(user_id)




app.add_url_rule('/' , 'home' , main.home)
app.add_url_rule('/login' , 'login' , main.login , methods = ['GET' , 'POST'])
app.add_url_rule('/logout' , 'logout' , main.logout , methods = ['GET' , 'POST'])
app.add_url_rule('/addpost' , 'add_post' , admin.add_post , methods = ['GET' , 'POST'])
app.add_url_rule('/allpost' , 'all_post' , admin.all_post , methods = ['GET' , 'POST'])
app.add_url_rule('/delpost' , 'delete' , admin.delete , methods = ['GET' , 'POST'])
app.add_url_rule('/edit' , 'edit' , admin.edit , methods = ['GET' , 'POST'])
app.add_url_rule('/post/<path:slug>' , 'single' , admin.single , methods = ['GET' , 'POST'])
app.add_url_rule('/search' , 'search' , admin.search , methods = ['GET' , 'POST'])
app.add_url_rule('/new' , 'new' , admin.new , methods = ['GET' , 'POST'])
app.add_url_rule('/delnewpost' , 'del_new' , admin.del_new , methods = ['GET' , 'POST'])
app.add_url_rule('/static/<path:filename>' , 'dowanload' , admin.dowanload , methods = ['GET' , 'POST'])



@app.before_request
def deta():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=False)
