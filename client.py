import pygame
from pygame.display import set_caption
from pygame.version import PygameVersion

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3

    def draw(self, win):
        """takes a window and draws a rectangle on screen"""
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        """checks what key user presses"""
        # returns dict of all keys with val 0 ( not pressing key) or 1 ( pressing key)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.val
        if keys[pygame.K_RIGHT]:
            self.x += self.val
        if keys[pygame.K_UP]:
            self.y -= self.val
        if keys[pygame.K_DOWN]:
            self.y += self.val

        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win, player):
    """updates dinwo"""
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True

    p1 = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redrawWindow(win, p1)


if __name__ == "__main__":
    main()
