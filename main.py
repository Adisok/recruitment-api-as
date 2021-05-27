import hashlib
import secrets
from typing import Optional
from views import router as messages_api_router
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, Response, HTTPException, Depends

app = FastAPI()
security = HTTPBasic()
app.api_token: Optional[str] = None
app.secret_code = ["It ain't much", " but it's honest work"]
app.username = "Daft_user"
app.password = "Daft_Password"
app.include_router(messages_api_router, tags=["messages"])

@app.get("/")
def root():
    return PlainTextResponse("Hello Daft!")


@app.post("/token", status_code=201)
def login_session(response: Response, credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, app.username)
    correct_password = secrets.compare_digest(credentials.password, app.password)

    if not (correct_password and correct_username):
        raise HTTPException(status_code=401, detail="Wrong Passowrd or Username")
    else:
        app.api_token = hashlib.sha256(f"{app.secret_code[0]}{app.username}:"
                                       f"{app.password}{app.secret_code[1]}".encode()).hexdigest()
        response.set_cookie(key="api_token", value=f"{app.api_token}")
        return {"api_token": f"BASIC{app.api_token}"}
