from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.slack.handler.changeStatus import changeStatus
from server.slack.model import StatusSchema
# from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.put("/change-status")
def change_status(status: StatusSchema):
    return changeStatus(status);