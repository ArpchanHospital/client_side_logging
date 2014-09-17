from flask import Flask, request, make_response

from RotatingLogger import RotatingLogger

LOGGER_NAME = "client_side"

CONFIG_FILE = "logging.yml"

app = Flask(__name__)


@app.route("/", methods=["POST"])
def client_side_logging():
    logger = RotatingLogger(CONFIG_FILE, LOGGER_NAME)
    logger.log.error(request.data)
    return make_response(request.data, 201)


if __name__ == "__main__":
    app.run()