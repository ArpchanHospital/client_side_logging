import logging

from flask import Flask, request, make_response


CLIENT_SIDE_LOG_FILE = '/var/log/client-side.log'

app = Flask(__name__)


@app.route("/", methods=["POST"])
def client_side_logging():
    logging.basicConfig(format='%(levelname)s: %(asctime)s  ---  %(message)s', filename=CLIENT_SIDE_LOG_FILE, level=logging.ERROR)
    logging.error(request.data)
    return make_response(request.data, 201)


if __name__ == "__main__":
    app.run()