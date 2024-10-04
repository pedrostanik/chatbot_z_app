from flask import Flask, request
from .send_message import SendMessage
app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST', 'PUT'])
def get_webhook():
    if request.method == 'POST':
        print('Entered POST Method')
        # Recebendo mensagens do webhook via PUT
        payload = request.get_json()
        print(f'payload: {payload}')
        
        if not payload:
            return "No JSON payload received", 400  # Tratamento de erro se o JSON estiver vazio
        
        print(f"Payload received in POST: {payload}")
        if 'text' in payload:
            message = payload['text']['message']
            phone = payload['phone']
            print(f'message: {message}')
            print(f'phone: {phone}')
            send_message = SendMessage()
            answer = f'Mensagem {message} recebida!'
            send_message.send_message(phone, answer)
        return "POST Message Received", 200  # Sucesso

if __name__ == "__main__":
    app.run(port=8000, debug=True)