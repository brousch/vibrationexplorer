#!/usr/bin/env python2.7

from array import array

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from jnius import autoclass

__version__ = '0.1'


class VibrationExplorer(BoxLayout):
    def do_vibrate(self, pattern):
        PythonActivity = autoclass('org.renpy.android.PythonActivity')
        Context = autoclass('android.content.Context')
        activity = PythonActivity.mActivity
        vibrator = activity.getSystemService(Context.VIBRATOR_SERVICE)
        if vibrator.hasVibrator():
#            if pattern.isdigit():
#                pat = long(pattern)
#            else:
#                pat = [long(p) for p in pattern.split(',')]
            pat = [0,500,500,500]
            vibrator.vibrate(pat, -1)
        else:
            popup = Popup(title='No Vibrator',
                          content=Label(text='Your device does not have a vibration motor.'),
                          size_hint=(0.5, 0.5))
            popup.open()


class VibrationExplorerApp(App):
    def build(self):
        return VibrationExplorer()


if __name__ == '__main__':
    app = VibrationExplorerApp()
    app.run()
