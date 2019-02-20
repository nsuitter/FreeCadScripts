################################## 
# Type in the dimensions here
# e.g. 4x8 wall would be
# hFeet = float(8)
# wFeet = float(4)

hFeet = float(16)
wFeet = float(4)

##################################
hInches = float(hFeet/2)
wInches = float(wFeet/2)
hMM = float(hInches*25.4)
wMM = float(wInches*25.4)


App.activeDocument().addObject('Sketcher::SketchObject','Sketch')
App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000,0.000000,0.000000),App.Rotation(0.000000,0.000000,0.000000,1.000000))
Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii \n OrthographicCamera {\n viewportMapping ADJUST_CAMERA \n position 0 0 87 \n orientation 0 0 1  0 \n nearDistance -112.88701 \n farDistance 287.28702 \n aspectRatio 1 \n focalDistance 87 \n height 143.52005 }')
Gui.activeDocument().setEdit('Sketch')
App.ActiveDocument.Sketch.addGeometry(Part.Line(App.Vector(0.000000,0.000000,0),App.Vector(wMM,0.000000,0)))
App.ActiveDocument.Sketch.addGeometry(Part.Line(App.Vector(wMM,0.000000,0),App.Vector(wMM,hMM,0)))
App.ActiveDocument.Sketch.addGeometry(Part.Line(App.Vector(wMM,hMM,0),App.Vector(0.000000,hMM,0)))
App.ActiveDocument.Sketch.addGeometry(Part.Line(App.Vector(0.000000,hMM,0),App.Vector(0.000000,0.000000,0)))
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',0,2,1,1)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',1,2,2,1)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',2,2,3,1)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',3,2,0,1)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Horizontal',0)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Horizontal',2)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Vertical',1)) 
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Vertical',3)) 
App.ActiveDocument.recompute()
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',0,1,-1,1)) 
App.ActiveDocument.recompute()
Gui.activeDocument().resetEdit()
App.activeDocument().recompute()
App.activeDocument().addObject("PartDesign::Pad","Pad")
App.activeDocument().Pad.Sketch = App.activeDocument().Sketch
App.activeDocument().Pad.Length = 10.0
App.ActiveDocument.recompute()
Gui.activeDocument().hide("Sketch")
Gui.activeDocument().setEdit('Pad',0)
App.ActiveDocument.Pad.Length = 3.175000
App.ActiveDocument.Pad.Reversed = 0
App.ActiveDocument.Pad.Midplane = 0
App.ActiveDocument.Pad.Length2 = 100.000054
App.ActiveDocument.Pad.Type = 0
App.ActiveDocument.Pad.UpToFace = None
App.ActiveDocument.recompute()
Gui.activeDocument().resetEdit()


App.activeDocument().addObject('Sketcher::SketchObject','Sketch001')
App.activeDocument().Sketch001.Support = (App.ActiveDocument.Pad,["Face6"])
App.activeDocument().recompute()
Gui.activeDocument().setEdit('Sketch001')


def addCircle():
	App.ActiveDocument.Sketch001.addGeometry(Part.Circle(App.Vector(x,y,0),App.Vector(0,0,1),1.6))
	App.ActiveDocument.recompute()
	pass

x = 3.175
y = 3.175
yStart = y

def getCondtions():

	global xCondition
	global yCondition
	global yChange
	global xChange

	if x > 0:
		xCondition = "x < " + str(wMM)
		xChange    = "x + 6.35"
	else:
		xCondition = "x >- " + str(wMM)
		xChange    = "x - 6.35"
		pass

	if y > 0:
		yCondition = "y < " + str(hMM-7)
		yChange    = "y + 6.35"
	else:
		yCondition = "y >-" + str(hMM-7)
		yChange    = "y - 6.35"
		pass
	pass


getCondtions()

while eval(xCondition):
	addCircle()
	while eval(yCondition):
		y = eval(yChange)
		addCircle()
		pass
	x = eval(xChange)
 	y = yStart
 	getCondtions()
	pass

Gui.activeDocument().resetEdit()
App.activeDocument().recompute()
App.activeDocument().addObject("PartDesign::Pocket","Pocket")
App.activeDocument().Pocket.Sketch = App.activeDocument().Sketch001
App.activeDocument().Pocket.Length = 5.0
App.ActiveDocument.recompute()
Gui.activeDocument().hide("Sketch001")
Gui.activeDocument().hide("Pad")
Gui.activeDocument().setEdit('Pocket')
Gui.ActiveDocument.Pocket.ShapeColor=Gui.ActiveDocument.Pad.ShapeColor
Gui.ActiveDocument.Pocket.LineColor=Gui.ActiveDocument.Pad.LineColor
Gui.ActiveDocument.Pocket.PointColor=Gui.ActiveDocument.Pad.PointColor
App.ActiveDocument.Pocket.Length = 0.793750
App.ActiveDocument.Pocket.Type = 0
App.ActiveDocument.Pocket.UpToFace = None
App.ActiveDocument.recompute()
Gui.activeDocument().resetEdit()



App.activeDocument().addObject('Sketcher::SketchObject','Sketch002')
App.activeDocument().Sketch002.Support = (App.ActiveDocument.Pocket,["Face5"])
App.activeDocument().recompute()
Gui.activeDocument().setEdit('Sketch002')




x = 1.2
y = 3.175

while y < hMM:
	lx = x - 25.4/32
	rx = x + 25.4/32
	ty = y + 25.4/16
	by = y - 25.4/16
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(rx,ty,0)))
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(lx,by,0),App.Vector(rx,by,0)))
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(lx,by,0)))
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(rx,ty,0),App.Vector(rx,by,0)))
	y = y + 6.35
	pass

x = wMM - 1.2
y = 3.175

while y < hMM:
	lx = x - 25.4/32
	rx = x + 25.4/32
	ty = y + 25.4/16
	by = y - 25.4/16
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(rx,ty,0)))
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(lx,by,0),App.Vector(rx,by,0)))
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(lx,by,0)))
	App.ActiveDocument.Sketch002.addGeometry(Part.Line(App.Vector(rx,ty,0),App.Vector(rx,by,0)))
	y = y + 6.35
	pass

Gui.activeDocument().resetEdit()
App.activeDocument().recompute()
App.activeDocument().addObject("PartDesign::Pocket","Pocket001")
App.activeDocument().Pocket001.Sketch = App.activeDocument().Sketch002
App.activeDocument().Pocket001.Length = 5.0
App.ActiveDocument.recompute()
Gui.activeDocument().hide("Sketch002")
Gui.activeDocument().hide("Pocket")
Gui.activeDocument().setEdit('Pocket001')
Gui.ActiveDocument.Pocket001.ShapeColor=Gui.ActiveDocument.Pocket.ShapeColor
Gui.ActiveDocument.Pocket001.LineColor=Gui.ActiveDocument.Pocket.LineColor
Gui.ActiveDocument.Pocket001.PointColor=Gui.ActiveDocument.Pocket.PointColor
App.ActiveDocument.Pocket001.Length = 1.587500
App.ActiveDocument.Pocket001.Type = 0
App.ActiveDocument.Pocket001.UpToFace = None
App.ActiveDocument.recompute()
Gui.activeDocument().resetEdit()




App.activeDocument().addObject('Sketcher::SketchObject','Sketch003')
App.activeDocument().Sketch003.Support = (App.ActiveDocument.Pocket001,["Face5"])
App.activeDocument().recompute()
Gui.activeDocument().setEdit('Sketch003')




x = 3.175
y = 1.2

while x < wMM:
	lx = x - 25.4/16
	rx = x + 25.4/16
	ty = y + 25.4/32
	by = y - 25.4/32
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(rx,ty,0)))
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(lx,by,0),App.Vector(rx,by,0)))
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(lx,by,0)))
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(rx,ty,0),App.Vector(rx,by,0)))
	x = x + 6.35
	pass

x = 3.175
y = hMM - 1.2

while x < wMM:
	lx = x - 25.4/16
	rx = x + 25.4/16
	ty = y + 25.4/32
	by = y - 25.4/32
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(rx,ty,0)))
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(lx,by,0),App.Vector(rx,by,0)))
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(lx,ty,0),App.Vector(lx,by,0)))
	App.ActiveDocument.Sketch003.addGeometry(Part.Line(App.Vector(rx,ty,0),App.Vector(rx,by,0)))
	x = x + 6.35
	pass

Gui.activeDocument().resetEdit()
App.activeDocument().recompute()
App.activeDocument().addObject("PartDesign::Pocket","Pocket002")
App.activeDocument().Pocket002.Sketch = App.activeDocument().Sketch003
App.activeDocument().Pocket002.Length = 5.0
App.ActiveDocument.recompute()
Gui.activeDocument().hide("Sketch003")
Gui.activeDocument().hide("Pocket001")
Gui.activeDocument().setEdit('Pocket002')
Gui.ActiveDocument.Pocket002.ShapeColor=Gui.ActiveDocument.Pocket001.ShapeColor
Gui.ActiveDocument.Pocket002.LineColor=Gui.ActiveDocument.Pocket001.LineColor
Gui.ActiveDocument.Pocket002.PointColor=Gui.ActiveDocument.Pocket001.PointColor
App.ActiveDocument.Pocket002.Length = 1.587500
App.ActiveDocument.Pocket002.Type = 0
App.ActiveDocument.Pocket002.UpToFace = None
App.ActiveDocument.recompute()
Gui.activeDocument().resetEdit()

