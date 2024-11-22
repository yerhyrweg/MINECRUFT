from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from panda3d.core import*
class Game(ShowBase):# напиши тут код основного вікна гри
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        x=10
        y=10
        self.hero = Hero(((x//2), (y//2), 3), self.land)
        base.camLens.setFov(90)
        props = WindowProperties.getDefault()
        props.setCursorHidden(True)
        base.win.requestProperties(props)
        

        

        
        
    
        
    
                
game = Game()
game.run()