from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route('/kakaotalk_chatbot_skill', methods=['POST'])
def kakaotalk_chatbot_skill():
    user_message = request.json['userRequest']['utterance']

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{user_message}\n",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )

    reply_message = response.choices[0].text.strip()
    
    return jsonify({
        'version': '2.0',
        'template': {
            'outputs': [
                {
                    'simpleText': {
                        'text': reply_message
                    }
                }
            ]
        }
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
