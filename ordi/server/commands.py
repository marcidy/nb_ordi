import subprocess


COMMANDS = {
    'ptpcam': "/home/marcidy/Projects/noisebridge/ordibooth/libptp-chdk/src/ptpcam", # NOQA
    'convert': "/usr/bin/convert"
}


def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode(
        "utf-8").split("\n")


def unwrap_return(chdk_return):
    return chdk_return.split(":")[-1]
