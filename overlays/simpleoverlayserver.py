'''
Created on Sep 23, 2014

@author: Julien CORON
'''
from overlays.overlayserver import OverlayServer


from kivy.graphics import Color,Ellipse

class SimpleOverlayServer(OverlayServer):
	'''
	Simple usage of subclass OverlayServer
	'''


	def __init__(self):
		'''
		Constructor
		'''
		self.type = 'simple'
		# 2 points on interest for this SimpleOverlayServer
		self.pois = [(48.8583, 2.2944), (45.669785, 4.758683)]
	
	def draw_in(self, aMapViewer):
		'''implement the method to draw in the MapViewer
		'''
		radius = 50.0/aMapViewer.scale
		x = aMapViewer.cmin[0]
		y = aMapViewer.cmin[1]
		(display_width, display_height) = aMapViewer.parent.size
		
		for aPoi in self.pois:
			(poi_x,poi_y) = aMapViewer.get_local_xy_from_latlon(aPoi[0], aPoi[1], display_width, display_height)
			with aMapViewer.canvas:
				Color(1, 0, 0, 0.2)
				Ellipse(pos=(x + poi_x/aMapViewer.scale - radius/2, y + poi_y/aMapViewer.scale - radius/2), size=(radius,radius))
		return
	