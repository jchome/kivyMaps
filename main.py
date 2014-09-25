# -*- coding: utf-8 -*-

## install & run with 
# buildozer android debug deploy run

## see logs with
# adb logcat -s "python"

import kivy

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

from kvmap_core.mapviewer import MapViewer
from overlays.simpleoverlayserver import SimpleOverlayServer

window_width = 450
window_height = 800

Config.set('graphics', 'width', window_width)
Config.set('graphics', 'height', window_height)


class KVMaps(App):
	
	def build(self):
		layout = FloatLayout()
		self.mv = MapViewer(maptype="Roadmap", provider="openstreetmap")
		self.all_poi = []
		
		layout.add_widget(self.mv)
		self.mv.map.scale = 10000
		self.mv.center_to_latlon( (45.673728,4.75418), window_width, window_height )
		self.mv.map.overlays.append( SimpleOverlayServer() )
		
		return layout
	
		
if __name__ in ('__android__','__main__'):
	KVMaps().run()
