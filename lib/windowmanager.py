import subprocess

class Window():
    'Represents a window and applies operations to it'
    
    def __init__(self, name, xPos, yPos, width, height):
        self.name = name
        self.grav = 0
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height
        

    def update(self):
        subprocess.call(['wmctrl', '-r',  self.name, '-e', '%i,%i,%i,%i,%i' % (self.grav, self.x, self.y, self.w, self.h)])
        
    def setxywh(self, xPos, yPos, width, height):
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height
        self.update()

 
