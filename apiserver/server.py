from flask import Flask,jsonify,request
import pickle


app = Flask(__name__)
flname = "somename.bin"

@app.route('/api/post',methods=['POST'])
def api():
    content = None
    with open(flname,'rb') as f:
        f.seek(0)

        try:
            content = pickle.load(f)
        except EOFError:
            print('error')
            content = {"field1":[request.form['field1']],"field2":[request.form['field2']]}

        else:
            content["field1"].append(request.form['field1'])
            content["field2"].append(request.form['field2'])
        
        print(content)


    with open(flname,'wb') as f:
        pickle.dump(content,f)


        




    return jsonify({"response":"ok"})


if __name__ == "__main__":
    app.run(port="80",host="0.0.0.0")