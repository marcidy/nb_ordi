from flask import (
    render_template,
    request
)
from nb_ordi import (
    app,
    cam,
)
from nb_ordi.exceptions import NoCameraException
import pudb


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


@app.route('/flashen')
def send_to_ft():
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
    pudb.set_trace()
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
