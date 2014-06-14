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

class OpenWindowList():
    'Retreives a list of open windows along with their positions and dimentions'

    def __init__(self):
        self.list = []
        self.__load()

    def __load(self):
        output = subprocess.check_output(['wmctrl', '-l', '-p', '-G']).decode('utf-8')

        for line in output.split('\n'):
            tokenList = line.split(None)
            if len(tokenList) < 6:
                continue

            x = int(tokenList[2])
            y = int(tokenList[3])
            w = int(tokenList[4])
            h = int(tokenList[5])
            name = ''

            for i in range(8, len(tokenList)):
                name += tokenList[i] + ' '
            
            win = Window(name.strip(), x, y, w, h)
            self.list.append(win)
