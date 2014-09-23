# -*- coding: utf-8 -*-

import kivy

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line,Color,Ellipse
from kivy.config import Config

from MapViewer import MapViewer
from overlays.simpleoverlayserver import SimpleOverlayServer

window_width = 800
window_height = 800

Config.set('graphics', 'width', window_width)
Config.set('graphics', 'height', window_height)


class KVMaps(App):
	
	def build(self):
		layout = FloatLayout()
		self.mv = MapViewer(maptype="Roadmap", provider="openstreetmap")
		self.all_poi = []
		
		layout.add_widget(self.mv)
		self.mv.map.scale = 20
		self.mv.center_to_latlon( (48.8583, 2.2944), window_width, window_height )
		self.mv.map.overlays.append( SimpleOverlayServer() )
		
		return layout
	
		
if __name__ in ('__android__','__main__'):
	KVMaps().run()
