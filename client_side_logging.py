import logging

from flask import Flask, request

CLIENT_SIDE_LOG_FILE = '/var/log/client-side.log'

app = Flask(__name__)


@app.route("/", methods=["POST"])
def client_side_logging():
    logging.basicConfig(filename=('%s' % CLIENT_SIDE_LOG_FILE), level=logging.ERROR)
    logging.error(request.data)
    return request.data


if __name__ == "__main__":
    app.run()