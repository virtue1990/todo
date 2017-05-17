from mongoengine import *
from datetime import datetime
from pprint import pprint
import json
class TodoModel(Document):
    meta = {
        'db_alias': 'virtue',
        'collection':'todo',
        'indexes':[
            {'fields':['email']}
        ]
    }
    _id = IntField()
    email = StringField()
    content = StringField()
    create_time = DateTimeField(required=True,default=datetime.now)



    def save_item(self,**kwargs):

        try:
            _id = kwargs.get('_id')
            obj = TodoModel.objects(_id=_id).first()
            if obj:
                TodoModel.update(**kwargs)
            else:
                TodoModel(**kwargs).save()

            return True
        except Exception,e:
            pprint(e)

    def list_item(self,email):
        try:
            obj = TodoModel.objects(email=email)
            result = list()
            for item in obj:
                temp_item = json.loads(item.to_json())
                result.append(temp_item)
            return result
        except Exception,e:
            pprint(e)


