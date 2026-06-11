from flask import Flask, jsonify, request

app = Flask(__name__)

# Credenciais fixas
USUARIO = "admin"
SENHA = "123456"

def autenticar():
    auth = request.authorization

    if not auth:
        return False

    return auth.username == USUARIO and auth.password == SENHA

@app.route("/hello", methods=["GET"])
def hello():
    if not autenticar():
        return (
            jsonify({"erro": "Credenciais inválidas"}),
            401,
            {"WWW-Authenticate": 'Basic realm="Login Required"'}
        )

    return jsonify({
        "mensagem": "Hello World"
    })

if __name__ == "__main__":
    app.run(debug=True)