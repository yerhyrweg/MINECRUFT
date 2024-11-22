
key_turn_left = "q"
key_turn_right = "e"
key_forward = "w"
key_back = "s"
key_left = "a"
key_right = "d"
switch_camera = "c"
switch_mode = "z"

key_up ="space"
key_down = "shift"

key_build = "b"
key_destroy ="v"

key_save = 'r'
key_load = 'l'



class Hero():

    def __init__(self, name, health, strength, agility):
        self.Land = land
        self.mode = True
        self.hero = Loader.LoadModel('smiley')
        self.hero.setColor(1,0.5,0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos) 
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        
#

        

    def cameraBind(self):
        base.camera.setH(180) 
        base.disableMouse()
        base.camera.reparent.To(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInteffaceNode.setPos(-pos[0], -pos[1], -pos[2])
        base.camera.reparentTo(render) 
        base.enablellouse() 
        self.cameraOn = False