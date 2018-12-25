from flask import Flask
from ordi_config import Config
from nb_ordi.camera import Camera


app = Flask(__name__)
app.config.from_object(Config)


cam = Camera(app.config['CAMERA_MODEL'], app.config['AUTOCONNECT'])


from nb_ordi import routes #NOQA
