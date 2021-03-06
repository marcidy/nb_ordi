from flask import (
    render_template,
    request
)
from ordi_server import (
    app,
    cam,
)
from ordi_server.camera import NoCameraException


@app.route('/snap')
def snap_picture():
    try:
        cam.record()
        cam.snap()
    except NoCameraException:
        pass
        # as rpi to wake the cam
    return('')


@app.route('/retrieve')
def retrieve_picture():
    ''' Need to get file name from request'''
    # make sure this request has the filename in it somewhere.
    cam.move_file(filename, here)
    return('')


@app.route('/tweet')
def tweet():
    return('')


@app.route('/piready')
def piready():
    try:
        cam.set_device(cam.id)
    except NoCameraException:
        pass
        # tell pi to try to turn the camera on
    return('')


@app.route('/checkcamera')
def check_camera():
    try:
        cam.set_device(cam.id)
    except NoCameraException:
        pass
        # Tell pi to try to turn the camera on
    return('')


@app.route('/sleep')
def sleep():
    # sleep for a while, try again
    return('')
