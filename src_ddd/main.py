from typing import Dict

from flasgger import Swagger
from flask import Flask

from config import routes
from config.di_container import container

swagger = Swagger()


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(routes.api_orders_v1)

    # documentation
    swagger.init_app(app=app)

    return app


app = create_app()


@app.route(rule='/_health')
def get_health() -> Dict:
    """
    Health
    ---
    tags:
      - API
    responses:
      200:
        description: success and small message.
        example: OK
    """
    return container.get('get_health_action').handle()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
