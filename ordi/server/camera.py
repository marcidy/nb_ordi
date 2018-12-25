import os
from PIL import Image
import subprocess
from nb_ordi.commands import (
    COMMANDS,
    run,
    unwrap_return,
)
from nb_ordi.exceptions import NoCameraException


class Picture:
    ''' Server side representation of an image and list of files which
    represent retakes or edits. '''

    files = None
    path = None
    convert = COMMANDS['convert']

    def __init__(self, filename):
        self.filename = filename
        self.files.append(self.filename)
        self.path = filename.split('/')

    def push(self, filename):
        self.files.push(filename)

    def pop(self, filename):
        return self.files.pop()

    def purge(self):
        self.files = list(self.files[-1])

    def pixelate(self, img_path, dest_path, width, height):
        cmd = [convert,
               img_path,
               "-resize",
               "{}x{}".format(width, height),
               "+dither",
               dest_path]

        return run_cmd(cmd)


class Camera:
    ''' A Camera object encapsualtes the server side calls to the camera
    hooked up to ordibooth server maching.  The camera shoudl be identified
    by a string in the config file.  The camera will attempt to find and
    connect to this camera.
    The Camera can take pictures, list files, and move files.  To take
    pictures, the camera should be in record mode.  The Camera can be
    powered on and off, but this command is sent tothe rpi as the on/off
    is connected to GPIO. '''

    connection_attempts = 0
    dev = None
    bus = None
    id = None
    mode = None
    ptpcam = COMMANDS['ptpcam']

    def __init__(self, id, autoconnect=False):
        self.id = id
        if autoconnect:
            self.set_device(self.id)

    def set_device(self, dev_id):
        self.connection_attempts += 1
        output = run([self.ptpcam, '-l'])

        for line in output:
            if dev_id in line:
                self.bus, self.dev = line.split('\t')[0].split('/')[0:2]
                break

        if self.dev is None or self.id is None:
            raise NoCameraException

    def list_files(self):
        photo_data = run([self.ptpcam, "--dev="+self.dev, "-L"])
        photos = []

        for photo in photo_data:
            if "IMG" in photo:
                photos.append(photo.split("\t")[-1])
        return(photos)

    def get_handle(self, file):
        photo_data = run([self.ptpcam, "--dev="+self.dev, "-L"])

        for photo in photo_data:
            if file in photo:
                return(photo.split('\t')[0].split(':')[0])

        return(None)

    def move_file(self, file, place):
        curdir = os.path.abspath('.')
        os.chdir(place)

        handle = self.get_handle(file)
        get = ["--dev=" + self.dev, "--get-file=" + handle]

        run(get)

        os.chdir(curdir)

    def upload():
        pass

    def record(self):
        run([self.ptpcam, "--dev="+self.dev, '--chdk=mode 1'])
        self.mode = "record"

    def playback(self):
        run([self.ptpcam, "--dev="+self.dev, '--chdk=mode 0'])
        self.mode = "playback"

    def snap(self):
        mode = self.mode
        self.record()

        run([self.ptpcam, "--dev="+self.dev, '--chdk=luar shoot()'])
