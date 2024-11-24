from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Import frames - okay to do this in the class since there will only
        # ever be one Player instance
        # self.downFrames = [pygame.image.load(join('images', 'player', 'down', f'{i}.png')).convert_alpha() for i in range(0,4)]
        # self.upFrames = [pygame.image.load(join('images', 'player', 'up', f'{i}.png')).convert_alpha().convert_alpha() for i in range(0,4)]
        # self.leftFrames = [pygame.image.load(join('images', 'player', 'left', f'{i}.png')).convert_alpha() for i in range(0,4)]
        # self.rightFrames = [pygame.image.load(join('images', 'player', 'right', f'{i}.png')).convert_alpha() for i in range(0,4)]

        self.frameIndex = 0
        self.image = self.downFrames[self.frameIndex]
        self.rect = self.image.get_frect(center = pos)

        self.speed = PLAYER_SPEED
        self.direction = pygame.Vector2()

    def processInput(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.processInput()
        self.move(dt)
