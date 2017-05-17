from ..model.todo  import TodoModel
from flask import g
from ..model.util import get_uuid

class TodoManager(object):
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def list(self):
        email = g.email
        tdm = TodoModel()
        result = tdm.list_item(email)

        return result

    def save_item(self,**kwargs):
        _id = get_uuid()
        tdm = TodoModel()
        tdm.save_item(**kwargs)
        return tdm.save_item(**kwargs)

