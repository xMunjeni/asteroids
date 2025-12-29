import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"""Screen width: {SCREEN_WIDTH} /n Screen height: {SCREEN_HEIGHT}""")

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    #Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

   

        screen.fill("black")

        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        x = clock.tick(60)
        dt = x / 1000
        #print (dt)



if __name__ == "__main__":
    main()
