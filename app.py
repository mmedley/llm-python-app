from flask import Flask, request, jsonify
import openai
import os
 
# Initialize Flask app
app = Flask(__name__)
 
# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
 
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        
        # Generate response using GPT-4
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return jsonify({"response": response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)