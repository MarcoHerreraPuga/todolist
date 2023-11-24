from flask import Flask
from app.routes.tasks import task_route
from app.routes.users import user_route

from app.config import Config

# instancia de Flaks
app_flask = Flask(__name__)
from app.db import db
app_flask.config.from_object(Config)

app_flask.register_blueprint(task_route)
app_flask.register_blueprint(user_route)



db.init_app(app_flask)

with app.app_context():
    db.create_all()


""" para que la aplicacion se ejecute y no se este recargando  """
if __name__ == "__main__":
    app_flask.run(debug=True)