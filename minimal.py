# -*- coding: utf-8 -*-

import kivy

kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line,Color,Ellipse
from kivy.config import Config

from MapViewer import MapViewer

window_width = 800
window_height = 800

Config.set('graphics', 'width', window_width)
Config.set('graphics', 'height', window_height)

#from projections import *

class PointOfInterest:
	def __init__(self, aName, aCoord):
		self.name = aName
		self.coord = aCoord
		

class KVMaps(App):
	
	def draw_cross(self,x,y):
		length = 40
		self.mv.canvas.add( Color(1, 0, 0) )
		self.mv.canvas.add( Line(points=(x-length,y,x+length,y)) )
		self.mv.canvas.add( Line(points=(x,y-length,x,y+length)) )

	def draw_point(self,x,y):
		radius = 100
		self.mv.canvas.add( Color(1, 0, 0,0.3) )
		self.mv.canvas.add( Ellipse(pos=(x-radius/2, y-radius/2), size=(radius,radius)) )
	
	def build(self):
		layout = FloatLayout()
		self.mv = MapViewer(maptype="Roadmap", provider="openstreetmap")
		self.all_poi = []
		
		layout.add_widget(self.mv)
		self.mv.map.scale = 30
		#self.mv.map.bind(on_touch_move = self.move_map)
		
		self.all_poi.append(PointOfInterest("paris", (48.8583, 2.2944) ) )
		self.all_poi.append(PointOfInterest("maison", (45.669785, 4.758683) ) )
		
		self.mv.center_to_latlon( self.all_poi[0].coord, window_width, window_height )
		
		self.draw_all_poi()
		return layout
	
	def draw_all_poi(self):
		radius = 100
		self.mv.canvas.add( Color(1, 0, 0,0.3) )
		for aPoi in self.all_poi:
			(x,y) = self.mv.map.get_local_xy_from_latlon(aPoi.coord[0], aPoi.coord[1], window_width, window_height)
			aPoi.display = Ellipse(pos=(x-radius/2, y-radius/2), size=(radius,radius))
			self.mv.canvas.add(aPoi.display)
	
	def move_map(self, aMapViewerPlane, event):
		return
		# need some review...
# 		maison = (45.669785, 4.758683)
# 		target_lat_long = maison
# 		target_xy = self.mv.map.get_xy_from_latlon(*target_lat_long)
# 		zero_xy = ( (window_width*0.5)-(TILE_W*self.mv.map.scale) , (window_height*0.5)-(TILE_H*self.mv.map.scale) )
# 		following_target = (
# 						aMapViewerPlane.x - zero_xy[0] + (window_width*0.5)+target_xy[0],
# 						aMapViewerPlane.y - zero_xy[1]+ (window_height*0.5)+target_xy[1]
# 						)
# 		((window_width)+aMapViewerPlane.x+target_xy[0], (window_height)+aMapViewerPlane.y+target_xy[1])
# 		
# 		self.draw_point( *following_target )
		
		
		
if __name__ in ('__android__','__main__'):
	KVMaps().run()
 	