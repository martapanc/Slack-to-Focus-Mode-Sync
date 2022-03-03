from fastapi import Request, FastAPI
from pydantic import BaseModel
from pathlib import Path

import uvicorn
import subprocess
import yaml
from datetime import datetime


class RequestBody(BaseModel):
    challenge: str


config_path = Path('.') / 'config/config.yml'
with open(config_path) as config_file:
    config = yaml.safe_load(config_file)

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "UP",
        "timestamp": await get_current_timestamp()
    }


async def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.post("/status/meeting")
async def set_status(request: Request):
    resp = await request.json()
    if "challenge" in resp:
        return {'challenge': resp['challenge']}

    meeting_status = "in a meeting"
    user = resp['event']['user']

    if user['id'] == config['user_id']:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if meeting_status in user['profile']['status_text'].lower():
            subprocess.run(['shortcuts', 'run', 'Focus Mode ON'])
            print('%s: In a meeting' % current_time)
        else:
            subprocess.run(['shortcuts', 'run', 'Focus Mode OFF'])
            print('%s: Free' % current_time)
        return resp
    else:
        return {'message': 'not my event'}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001)
