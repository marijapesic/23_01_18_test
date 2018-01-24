from flask import Flask
from models import *


app = Flask(__name__)

# COMMENTS = [
#     Comment("hello", "2018-01-01"),
#     Comment("world", "2018-01-02"),
#     Comment("test", "2018-01-03"),
# ]
c1 = ['first_comment','second_comment','third_comment']


@app.route("/")
@app.route('/index')
def index():
    user = {'username': 'Marija'}
    return render_template('index.html', title='Home', user=user)
     """Home route handler."""
