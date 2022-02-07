from flask import Flask
applicaiton = Flask(__name__)

@applicaiton.route('/')
def hello_world():
    return 'Sup. Subscribe'

if __name__=="__main__":
    applicaiton.run()