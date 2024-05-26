from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__, static_folder='static')
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data['prompt']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].text.strip()})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

