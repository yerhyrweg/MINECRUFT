
key_turn_left = "q"
key_turn_right = "e"
key_forward = "s"
key_back = "w"
key_left = "d"
key_right = "a"
switch_camera = "c"
switch_mode = "z"

playerMoveSpeed = 10

key_up = "space"
key_down = "shift"

key_build = "b"
key_destroy = "v"

key_save = "f5"
key_load = "f6"

key_btype_0 = "0"
key_btype_1 = "1"
key_btype_2 = "2"
key_btype_3 = "3"



class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.btype = 0
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1,0.5,0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        
    def cameraBind(self):
        base.enableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1)
        self.cameraOn = True       
    
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False       
        
    def changeViev(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()       
        
    def resetMouse(self):   
        cx = base.win.getProperties().getXSize() // 2
        cy = base.win.getProperties().getYSize() // 2
        base.win.movePointer(0,cx,cy)    
        self.resetMouse()    
            
          
    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)%360)
    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)
        
        if base.mouseWatcherNode.hasMouse():
            x = base.mouseWatcherNode.getMouseX()
            y = base.mouseWatcherNode.getMouseY()
        
    def look_at(self, angle):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())
        
        dx, dy = self.check_dir(angle)
        
        x_to = x_from + dx
        y_to = y_from + dy
        
        return x_to, y_to, z_from
    
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    
    def check_dir(self, angle):
        if angle >= 0 and angle <=20:
            return (0,-1)
        elif angle <=65:
            return (1,-1)
        elif angle <=110:
            return (1,0)
        elif angle <=155:
            return (1,1)
        elif angle <=200:
            return (0,1)
        elif angle <=245:
            return (-1,1)
        elif angle <=290:
            return (-1,0)
        elif angle <=335:
            return (-1,-1)
        else:
            return (0,-1)
        camera
    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)
    
    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
        
    def change_mode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True
    
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2]+1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
    
    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ()+1)
    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ()-1)
            
    def build(self):
        angle = self.hero.getH()%360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos, type = self.btype)
        else:
            self.land.buildBlock(pos, type = self.btype)
            
    def setBuild(self, type):
        self.btype = type
    
    def destroy(self):
        angle = self.hero.getH()%360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)
    



    def accept_events(self):
        base.accept(switch_mode, self.change_mode)
        base.accept(key_up, self.up)
        base.accept(key_up + '-repeat', self.up)
        base.accept(key_down, self.down)
        base.accept(key_down + '-repeat', self.down)
        
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward+'-repeat', self.forward)
        base.accept(key_back, self.back)
        base.accept(key_back+'-repeat', self.back)
        base.accept(key_left, self.left)
        base.accept(key_left+'-repeat', self.left)
        base.accept(key_right, self.right)
        base.accept(key_right+'-repeat', self.right)
        
        base.accept(switch_camera, self.changeViev)
        
        base.accept(key_save, self.land.save_map)
        base.accept(key_load, self.land.load_map)
        
        base.accept(key_build, self.build)
        base.accept(key_btype_0, self.setBuild, [0])
        base.accept(key_btype_1, self.setBuild, [1])
        base.accept(key_btype_2, self.setBuild, [2])
        base.accept(key_btype_3, self.setBuild, [3])
        
        
        
        
        base.accept(key_destroy, self.destroy)
        
        