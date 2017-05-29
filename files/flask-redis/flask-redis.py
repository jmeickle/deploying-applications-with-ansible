from flask import Flask
from flask_redis import FlaskRedis
import traceback

app = Flask(__name__)
redis_store = FlaskRedis(app)

@app.route('/')
def hello_world():
    return 'Welcome to Deploying Applications With Ansible! You are visitor ' \
           'number: {}'.format(redis_store.incr(1))


# A little Flask magic to show backtraces in HTTP responses.
@app.errorhandler(Exception)
def show_errors(exception):
    return("<pre>" + traceback.format_exc() + "</pre>"), 500