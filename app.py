from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data['prompt']
    previous_interactions = data.get('previous_interactions', [])
    conversation = "\n".join(previous_interactions + [prompt])
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=conversation,
        max_tokens=150,
        temperature=0.7,
        stop=["\n"]
    )
    return jsonify({'response': response.choices[0].text.strip()})

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

