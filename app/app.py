from flask import Flask, request
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
        return "POST Message Received", 200  # Sucesso

if __name__ == "__main__":
    app.run(port=8000, debug=True)