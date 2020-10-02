from flask import Flask, request, jsonify
from flask_cors import CORS
import service
import json

app = Flask(__name__)
CORS(app)

@app.route('/upload',methods = ['POST','GET'])
def upload():
    
    f = request.files['file']
    msg = service.process(f)
    return jsonify(response = msg)
    
@app.route('/search',methods = ['POST','GET'])
def search():
   searchRequest = request.get_json()
   
   response = service.search(searchRequest)
   
   return json.dumps({"response": response})
   
@app.route('/home',methods = ['POST','GET'])
def home():
    
   result = service.getHomeDetails()
   
   if type(result).__name__ == 'dict':
       return result
   elif type(result).__name__ == 'str':
       return jsonify(errorMessage = result)
    
@app.route('/infoupload',methods = ['POST','GET'])
def infoupload():
    f = request.files['file']
    msg = service.saveInfo(f)
    return jsonify( response = msg)
    

if __name__ == '__main__':
   app.run(host= '0.0.0.0')
   


#curl -i -X POST -F "file=@C:\Users\Deval\Desktop\HACKATHON\POC\data25.xlsx" http://127.0.0.1:5000/upload

#curl -i -X POST -F "file=@C:\Users\Deval\Desktop\HACKATHON\POC\userdata.xlsx" http://127.0.0.1:5000/infoupload

