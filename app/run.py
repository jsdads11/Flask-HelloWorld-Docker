from flask import Flask                          # import flask framework into our code
import json

app = Flask(__name__)    

@app.route("/")					 # create an instance of the flask app  when we hit the URL to “/” it calls the functionand returns result
def helloworld():                                # Helloworld function which simply returns a plain string "Hello World!"
    return "Hello World!"                        # 

@app.route("/get_data")
def getdata():
    data = {
        'name' : 'My Name',
        'url' : 'My URL'
    }
    return json.dumps(data)


if __name__ == "__main__":                       # 
    app.run()                                    # start the flask app server and start to listen to the incoming requests     


# to exec: python run.py


