from functools import partial
from pyspacelib.ft import flaschen_taschen as ft
from pyspacelib.ft.ft_controller import (
    FTController,
    FTImage,
)
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
# Config.set('graphics', 'fullscreen', 'auto')
# Config.set('graphics', 'window_state', 'maximized')
# Window.fullscreen = 'auto'


class OrdiBooth(BoxLayout):
    source = './test.png'
    source2 = './water.jpg'


class FlaschenTaschenViewer(Widget):

    ftc = FTController()

    def load_image(self, img_path='./test.png'):
        self.fti = FTImage(img_path, "./")
        self.fti.pixelate(ft.width, ft.height)
        self.ftc.fill_buffer(self.fti)

    def add_bottles(self, wid):
        _x, _y = self.pos
        _h, _w = self.size

        self.load_image()
        height = ft.height
        width = ft.width
        grid = self.ftc.grid
        bottle_size = min(_h/height, _w/width)

        with wid.canvas:
            for y in range(width):
                for x in range(height):
                    r, g, b = grid[height-(x+1)][y]
                    Color(r/255, g/255, b/255)
                    Ellipse(pos=(y*bottle_size + self.y,
                                 x*bottle_size + self.x),
                            size=(bottle_size, bottle_size))  # NOQA

    def reset(self, wid):
        wid.canvas.clear()

    def show(self):
        self.ftc.show()


class OrdiApp(App):

    def build(self):
        return OrdiBooth()


if __name__ in ("__main__", "__android__"):

    app = OrdiApp()
    app.run()
