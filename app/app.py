from flask import Flask, request
from .send_message import SendMessage
from .assistant_gpt import AssistantGPT
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
            if phone == '5514988068820' or phone =='5514997424753':
                send_message = SendMessage()
                # answer = f'Mensagem {message} recebida!'
                assistant_gpt = AssistantGPT()
                answer = assistant_gpt.execute(message)
                send_message.send_message(phone, answer)
                return "POST Message Received", 200  # Sucesso
            return "POST Message Received, Not the Right user", 201  # Sucesso

if __name__ == "__main__":
    app.run(port=8000, debug=True)