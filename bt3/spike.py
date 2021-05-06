
class spike(saw):  # We are inheriting from saw
    img = pygame.image.load(os.path.join('images', 'spike.png'))
    def draw(self,win):
        self.hitbox = (self.x + 10, self.y, 28,315)  # defines the hitbox
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))