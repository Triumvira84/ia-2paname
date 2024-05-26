from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__, static_folder='.')

# Assurez-vous d'utiliser votre propre clé API OpenAI
openai.api_key = 'YOUR_API_KEY'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data['prompt']
    previous_interactions = data.get('previous_interactions', [])
    conversation = "\n".join(previous_interactions + [prompt])
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=conversation,
        max_tokens=150,
        temperature=0.7,
        stop=["\n"]
    )
    return jsonify({'response': response.choices[0].text.strip()})

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run()
