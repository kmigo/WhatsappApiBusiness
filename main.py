from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get('/webhook')
def webhook(req: Request):
    return int(req.query_params['hub.challenge'])