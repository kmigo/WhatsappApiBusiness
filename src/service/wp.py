import requests
import os


class WPService:
    def __init__(self):
        self.url = f"{os.getenv('WP_URL')}/${os.environ.get('WP_ID')}"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': os.environ.get("WP_TOKEN")
        }

    def send_message(self, data,id):
        import json
        response = requests.post(f"{self.url}/messages", {
            'messaging_product': 'whatsapp',
            'to': data['to'],
            'context':{
                'message_id':id
            },
            'type': 'text',
            'text': {
                'body': data['message']
            }
        }, headers=self.headers)
        print(self.headers)
        print(response.headers)
        print(json.dumps(response.json(),indent=4))
