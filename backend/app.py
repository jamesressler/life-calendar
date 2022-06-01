from flask import Flask, request, redirect
from flask_cors import CORS, cross_origin
import sys
sys.path.append('..')
import database

app = Flask(__name__)
CORS(app)
model = database.get_model()
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/comments", methods=['GET','POST'])
@cross_origin(origin='localhost')
def comments():
    entries = {"name": [], "message": []}
    if(request.method=='POST'):
        data = request.get_json()
        model.insert(data['name'], data['message'])
    else:
        print("In GET")
        for row in model.select():
            print(row)
            entries["name"].append(row[0])
            entries["message"].append(row[1])
    return entries

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)