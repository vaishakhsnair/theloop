from flask import Flask,jsonify,request
import pickle


app = Flask(__name__)
flname = "somename.bin"


@app.route('/api/get')
def get():
    with open(flname,'rb') as f:
        content = pickle.load(f)
        return jsonify(content)
    

@app.route('/api/post',methods=['POST'])
def api():
    content = None
    with open(flname,'rb') as f:
        f.seek(0)

        try:
            content = pickle.load(f)
        except EOFError:
            print('error')
            content = {"voltage":[request.form['field1']],"percent":[request.form['field2']]}

        else:
            content["voltage"].append(request.form['field1'])
            content["percent"].append(request.form['field2'])
            content["valength"] = [i for i in range(len(content))]
        
        print(content)


    with open(flname,'wb') as f:
        pickle.dump(content,f)


        




    return jsonify({"response":"ok"})


if __name__ == "__main__":
    app.run(port="80",host="0.0.0.0")