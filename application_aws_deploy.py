from flask import Flask
applicaiton = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Sup. Subscribe'

if __name__=="__main__":
    application.run()
