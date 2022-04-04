from json import JSONEncoder
import profile
from urllib import response
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
from server.slack.model import StatusSchema
from server.slack.init import client

def changeStatus(status: StatusSchema):
    expiration = datetime.now() + timedelta( hours = status.status_expiration )
    
    status.status_expiration = expiration.timestamp()

    new_status = jsonable_encoder(status)
    response = client.users_profile_set(profile = new_status)

    return response.get('ok')