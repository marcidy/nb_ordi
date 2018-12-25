from functools import partial
from pyspacelib.ft import flaschen_taschen as ft
from pyspacelib.ft.ft_controller import (
    FTController,
    FTImage,
)
from kivy.app import App
from kivy.graphics import Color, Ellipse
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


class FlaschenTaschenViewer(BoxLayout):

    ftc = FTController()

    def add_bottles(self, wid):
        self.fti = FTImage("./test.png", "./")
        self.fti.pixelate(ft.width, ft.height)
        self.ftc.fill_buffer(self.fti)

        height = ft.height
        width = ft.width
        grid = self.ftc.grid

        with wid.canvas:
            for y in range(width):
                for x in range(height):
                    r, g, b = grid[height-(x+1)][y]
                    Color(r/255, g/255, b/255)
                    Ellipse(pos=(y*20, x*20), size=(20, 20))

    def reset(self, wid):
        wid.canvas.clear()

    def show(self):
        self.ftc.show()

    def build(self):
        root = Builder.load_file("ordi.kv")
        return root


class FlaschenTaschenApp(App):

    def build(self):
        Builder.load_file("./ordi.kv")
        return FlaschenTaschenViewer()


if __name__ in ("__main__", "__android__"):

    app = FlaschenTaschenApp()
    app.run()
