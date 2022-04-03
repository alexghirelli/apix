from json import JSONEncoder
import profile
from urllib import response
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from server.slack.model import StatusSchema
from server.slack.init import client

def changeStatus(status: StatusSchema):
    new_status = jsonable_encoder(status)
    response = client.users_profile_set(profile = new_status)

    return response.get('ok')