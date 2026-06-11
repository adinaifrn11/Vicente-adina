from flask import Flask, jsonify
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)

# Chave usada para gerar os nonces do Digest
app.config["SECRET_KEY"] = "minha-chave-secreta"

auth = HTTPDigestAuth()

usuarios = {
    "admin": "123456"
}

@auth.get_password
def get_pw(username):
    return usuarios.get(username)

@app.route("/hello", methods=["GET"])
@auth.login_required
def hello():
    return jsonify({
        "mensagem": "Hello World"
    })

if __name__ == "__main__":
    app.run(debug=True)