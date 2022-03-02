from fastapi import Request, FastAPI
from pydantic import BaseModel
import uvicorn
import json


class RequestBody(BaseModel):
    challenge: str


app = FastAPI()


@app.post("/status/meeting")
async def set_status(request: Request):
    resp = await request.json()
    print(json.dumps(resp, indent=4, sort_keys=True))
    return resp


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001)
