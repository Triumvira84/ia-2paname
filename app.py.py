from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data['prompt']
    previous_interactions = data.get('previous_interactions', [])
    conversation = "\n".join(previous_interactions + [prompt])
    
    # Utilisation de la méthode de l'API OpenAI
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=conversation,
        max_tokens=150,
        temperature=0.7,
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
