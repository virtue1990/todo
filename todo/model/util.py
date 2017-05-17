import uuid
from mongoengine import connect
def get_uuid():
    temp_id = uuid.uuid4().int & ((1<<32)-1)


def get_connect():
    clent = connect(alias='virtue')
