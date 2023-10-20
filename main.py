# main.py

from flask import Blueprint, g,current_app,render_template,request,redirect,flash,url_for,session
from .utils.api import is_api_key_valid


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('login.html')

@main.route('/', methods=['POST'])
def login_post():
    api_key = request.form.get('api')
    #remember = True if request.form.get('remember') else False
    session['api_key'] = api_key
    
    if is_api_key_valid(api_key) == False:
        flash('Invalid API key')
        return redirect(url_for('main.index'))
    else:
        return redirect(url_for('upl.uplbot'))
