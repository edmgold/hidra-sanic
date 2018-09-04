from sanic import Sanic
from sanic.response import json

from src.api.users.users_routes import user_blueprint
from src.api.users.users_model import Create

from sanic_openapi import swagger_blueprint, openapi_blueprint

app = Sanic('server')

app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)
app.blueprint(user_blueprint)

app.config.API_VERSION = '1.0.0'
app.config.API_TITLE = 'Api de usuários'
app.config.API_DESCRIPTION = 'Squad abastecimento'
app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
app.config.API_CONTACT_EMAIL = 'abastecimento@luizalabs.com'

if __name__ == "__main__":
    Create.execute()
    app.run(host="0.0.0.0", port=8000)