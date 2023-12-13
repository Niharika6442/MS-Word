# Flask example
from flask import Flask, request, jsonify
from summerize import t5_summerizer, openai_summerizer
app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    document_content = data['document_content']
    summary = t5_summerizer(document_content)
    return jsonify({'summary': summary})


if __name__ == '__main__':
    app.run(port=5000)