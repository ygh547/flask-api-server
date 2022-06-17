from flask import Flask

app = Flask(__name__)

# API가 있어야 한다. 아래코드가 API
@app.route('/' , mothods= ['GET'])
def hello_world():
    return 'Hello World hihihi'

if __name__ == '__main__' :
    app.run()