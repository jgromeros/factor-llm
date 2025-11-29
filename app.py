from flask import Flask
from flask_smorest import Api

from factor.llm.api.extract_api import extract_api

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Factor LLM API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.4"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    api = Api(app)
    api.register_blueprint(extract_api)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
