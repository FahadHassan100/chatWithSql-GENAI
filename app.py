from flask import Flask, jsonify
from chatSql import ChatWithSql

app = Flask(__name__)
obj = ChatWithSql("root", "", "localhost","testingdublicatedb")

@app.route('/send-message', methods=["GET"])
def send_message():
    
    message = obj.message("How many tables do we have")
    return jsonify({"message":message})


if __name__ == '__main__':
    app.run(debug=True)