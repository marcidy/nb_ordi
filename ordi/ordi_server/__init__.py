from flask import Flask
from ordi_server.camera import Camera


class Config:
    CAMERA_MODEL = "A2200"
    AUTOCONNECT = False


app = Flask(__name__)
app.config.from_object(Config)

cam = Camera(app.config['CAMERA_MODEL'], app.config['AUTOCONNECT'])

from ordi_server import routes #NOQA
