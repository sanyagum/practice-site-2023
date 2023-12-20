from flask import Flask
import os
from importlib import import_module

app = Flask(__name__)


for file in os.listdir('routes'):
    if file == '__pycache__': continue
    module = import_module(f'routes.{file[:-3]}')
    app.register_blueprint(module.bp)


if __name__ == '__main__':
    app.run(debug=True)