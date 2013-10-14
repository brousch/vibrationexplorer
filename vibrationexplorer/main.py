#!/usr/bin/env python2.7

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

__version__ = '0.1'


class VibrationExplorer(BoxLayout):
    pass


class VibrationExplorerApp(App):
    def build(self):
        return VibrationExplorer()


if __name__ == '__main__':
    app = VibrationExplorerApp()
    app.run()
