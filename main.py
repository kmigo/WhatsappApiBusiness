from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.service.wp import WPService
load_dotenv()

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

@app.post('/webhook')
def webhook(body:dict,req: Request):
    value = {}
    print(body)
    if req and "body" in req and "entry" in body and len(body["entry"]) > 0 \
        and "changes" in body["entry"][0] and len(body["entry"][0]["changes"]) > 0:
        value = body["entry"][0]["changes"][0].get("value")

    if value.get('messages'):
        if value and "messages" in value and len(value["messages"]) > 0:
            id_ = value["messages"][0].get("id")
            destination = value["messages"][0].get("from")
            message = value["messages"][0].get("text",{}).get('body',None)
            location = value["messages"][0].get("location")
            interaction = value["messages"][0].get("interaction")
            if message:
                WPService().send_message({'to':destination,'message':'foi'},id_)
                
            

    return int(req.query_params['hub.challenge'])