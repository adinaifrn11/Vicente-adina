from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEY = "minha-chave-secreta"

@app.route("/hello", methods=["GET"])
def hello():
    chave_recebida = request.headers.get("X-API-Key")

    if chave_recebida != API_KEY:
        return jsonify({
            "erro": "API Key inválida ou não informada"
        }), 401

    return jsonify({
        "mensagem": "Hello World"
    })

if __name__ == "__main__":
    app.run(debug=True)