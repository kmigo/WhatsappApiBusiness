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

"""
{'object': 'whatsapp_business_account',
'entry': [
    {'id': '118349154557213', 
    'changes': [
         {'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15550847474', 'phone_number_id': '115759418151225'}, 
        'contacts': [{'profile': {'name': 'Patrick'}, 'wa_id': '5527995258068'}], 
    'messages': [
        {'from': '5527995258068', 'id': 'wamid.HBgNNTUyNzk5NTI1ODA2OBUCABIYIEVCNUY2RERDRTc2QTAzMTNCQTY2NTk0NUJEMjJGMzRDAA==', 'timestamp': '1694891965', 'text': {'body': 'Oi'}, 'type': 'text'}
        ]
     },
     'field': 'messages'}
     ]
    }
    ]
    }
"""

@app.post('/webhook')
def webhook(body:dict,req: Request):
    entry = body.get('entry',[])
    if len(entry) > 0:
        entry = entry[0]
    id = entry.get('id',None)
    changes = entry.get('changes',[])
    if len(changes) > 0:
        changes = changes[0]
    messages = changes.get('messages',[])
    if len(messages) > 0:
        messages = messages[0]
    from_ = messages.get('from',None)
    message_id = messages.get('id',None)
    message = messages.get('text',{}).get('body',None)
    type = messages.get('type',None)
    print(from_,message_id,message,type,id)
    
 

        
        
    """if req and "body" in req and "entry" in body and len(body["entry"]) > 0 \
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
                WPService().send_message({'to':destination,'message':'foi'},id_)"""
                
            

    return {'message': 'Hello World'}