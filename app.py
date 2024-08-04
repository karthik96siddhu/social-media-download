from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.instagram_download import InstagramApi

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(InstagramApi, '/insta-download')

@app.route('/')
def hello():
    return 'Hello world!S'


if __name__ == '__main__':
    app.run(debug=True)


