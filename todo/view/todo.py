from flask import session,redirect,Blueprint,jsonify
from commandr import command,Run
from pprint import pprint
from ..lib.todo import TodoManager
from ..model.util import get_connect

blueprint = Blueprint('todo',__name__,url_prefix='/todo')

@blueprint.before_request
def before_request():
    print 'login'
    get_connect()
    pprint(session)


@blueprint.route('/add',methods=['GET','POST'])
def add_item():
    tdm = TodoManager()
    data = {
        'content':'xxxx'
    }
    tdm.save_item(**data)
    return 'hello world'
