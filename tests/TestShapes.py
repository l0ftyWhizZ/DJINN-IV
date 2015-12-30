from djinn.player.Player import *
from djinn.window.Window import *
from djinn.window.KeyboardEvent import *
from djinn.scenes.shapes.Sphere import *
from djinn.scenes.shapes.Cylinder import *
from djinn.scenes.shapes.Triangle import *
from djinn.scenes.Light import *
from djinn.scenes.Material import *
if __name__=="__main__":
	window = Window((800,600))
	window.start(70)
	window.caption("DJINN IV Game Engine")	
	window.icon('djinn-iv-logo.bmp')
	play = Player(0,0,-5.0)
	cylinder = Cylinder(0.5,0.5,15,-25,0,0,(0,1,0))
	sphere = Sphere(1,-15,0,0,(0,0,1))
	triangle = Triangle(-12,3,10,-20,6,8,-13,-4,11,[0.5,0.4,0.2])
	play.setOrigin(0,0,-25.0)
	light0 = Light(-20,5,-5,[1,1,1,1],1)
	light1 = Light(0,1,15,[1,1,1,1],1)
	light0.bake(GL_LIGHT0)
	light1.bake(GL_LIGHT1)
	moveList = [0,0,0]

	while True:
		KeyboardEvent(moveList)
		window.clear()
		
		play.move(moveList[0],0,moveList[2])
		sphere.build()
		cylinder.build()
		triangle.build()
		pygame.time.Clock().tick(60)
		window.update()
