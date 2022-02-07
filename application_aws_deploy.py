from flask import Flask
application_aws_deploy = Flask(__name__)
@application_aws_deploy.route('/')
def hello_world():
    return 'Hello world.'
