import os
from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__, static_folder='static')

# Configurer la clé API OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
