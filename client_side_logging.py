import logging
from logging.handlers import TimedRotatingFileHandler


from flask import Flask, request, make_response


CLIENT_SIDE_LOG_FILE = 'client-side.log'

app = Flask(__name__)
logger = logging.getLogger("Client Side ")
logger.setLevel(logging.ERROR)
log_handler = TimedRotatingFileHandler(CLIENT_SIDE_LOG_FILE, when='s', interval=5)
log_handler.setLevel(logging.ERROR)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)



@app.route("/", methods=["POST"])
def client_side_logging():
    # logging.basicConfig(format='%(levelname)s: %(asctime)s  ---  %(message)s', filename=CLIENT_SIDE_LOG_FILE, level=logging.ERROR)
    # logging.error(request.data)
    logger.error(request.data)
    return make_response(request.data, 201)


if __name__ == "__main__":
    app.run()