from flask import Flask,jsonify,request


app = Flask(__name__)
flname = "somename.bin"


@app.route('/api/post',methods=['POST'])
def api():
    print(request.json)



    return jsonify({"response":"ok"})


if __name__ == "__main__":
    app.run(port="8080",host="0.0.0.0")