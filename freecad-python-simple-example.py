# create new sketch

App.activeDocument().addObject('Sketcher::SketchObject','Sketch')
App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000,0.000000,0.000000),App.Rotation(0.000000,0.000000,0.000000,1.000000))
Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii \n OrthographicCamera {\n viewportMapping ADJUST_CAMERA \n position 0 0 87 \n orientation 0 0 1  0 \n nearDistance -112.88701 \n farDistance 287.28702 \n aspectRatio 1 \n focalDistance 87 \n height 143.52005 }')
Gui.activeDocument().setEdit('Sketch')

# add circles
x = 0
y = 0
while x < 100:
	while y < 100:
		# print "x:" + str(x) + ", y:" + str(y)
		App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(x,y),App.Vector(0,0,1),4))
		y = y + 10
		pass
	x = x + 10
	y = 0
	pass

# close sketch
Gui.getDocument('Unnamed').resetEdit()
App.getDocument('Unnamed').recompute()
