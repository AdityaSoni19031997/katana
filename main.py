import os
import yaml
import logging
from flask import Flask, redirect
from apis import blueprint as api

with open(r"./configurations/config.yml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api/v1')
DEFAULT_API_VERSION = config['DEFAULT_API_VERSION']

# Redirect to default namespace version
@app.route('/')
def redirect_default_version(default_version=DEFAULT_API_VERSION):
    return redirect(f"/api/v{default_version}", code=302)

if __name__ == "__main__":

    if not os.path.exists(config["MODEL_DIR"]):
        os.makedirs(config["MODEL_DIR"], exist_ok=True)
    app.run(debug=config["DEBUG"], host=config["HOST"], port=config["PORT"])
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
 
