class saw(object):
    rotate = [pygame.image.load(os.path.join('images', 'SAW0.PNG')),pygame.image.load(os.path.join('images', 'SAW1.PNG')),pygame.image.load(os.path.join('images', 'SAW2.PNG')),pygame.image.load(os.path.join('images', 'SAW3.PNG'))]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)  # Defines the accurate hitbox for our character 
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        if self.rotateCount >= 8:  # This is what will allow us to animate the saw
            self.rotateCount = 0
        win.blit(pygame.transform.scale(self.rotate[self.rotateCount//2], (64,64)), (self.x,self.y))  # scales our image down to 64x64 before drawing
        self.rotateCount += 1