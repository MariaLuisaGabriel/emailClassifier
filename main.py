from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/classify', methods=['GET'])
def receber_dados():
    dados = request.get_json()
    emailcontent = dados.get('emailcontent')
    return jsonify({
        "mensagem": f"{emailcontent}"
    })

if __name__ == '__main__':
    app.run()