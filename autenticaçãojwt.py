from flask import Flask, jsonify, request
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

SECRET_KEY = "minha-chave-secreta"

USUARIO = "admin"
SENHA = "123456"


def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({
                "erro": "Token não informado"
            }), 401

        try:
            tipo, token = auth_header.split(" ")

            if tipo != "Bearer":
                raise Exception()

            jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

        except Exception:
            return jsonify({
                "erro": "Token inválido ou expirado"
            }), 401

        return f(*args, **kwargs)

    return decorated


@app.route("/login", methods=["POST"])
def login():

    dados = request.get_json()

    username = dados.get("username")
    password = dados.get("password")

    if username != USUARIO or password != SENHA:
        return jsonify({
            "erro": "Credenciais inválidas"
        }), 401


    token = jwt.encode(
        {
            "usuario": username,
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm="HS256"
    )


    return jsonify({
        "access_token": token
    })


@app.route("/hello", methods=["GET"])
@token_obrigatorio
def hello():

    return jsonify({
        "mensagem": "Hello World"
    })


if __name__ == "__main__":
    app.run(debug=True)