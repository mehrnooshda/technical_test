import traceback
from flask import jsonify
from werkzeug.exceptions import HTTPException
from app import create_app
import config


app = create_app()

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST, port=int(config.PORT))

