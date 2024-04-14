import configparser
import json
import requests

from typing import Optional
from fastapi import APIRouter
from requests.auth import HTTPBasicAuth
from internal import EosRequest

router = APIRouter()

config = configparser.ConfigParser()
config.read('config.ini')


@router.get("/api/v1/commands/", tags=["eos"])
def run_command(command: Optional[str] = "show version"):
    request = EosRequest(config, None, None)

    request.update_cmd_params({
        "version": 1,
        "cmds": command.split(","),
        "format": "json"
    })

    response_str = requests.post(request.endpoint,
                                 json=request.payload,
                                 headers=request.headers,
                                 auth=HTTPBasicAuth(request.user, request.password),
                                 verify=False).text

    return json.loads(response_str)
