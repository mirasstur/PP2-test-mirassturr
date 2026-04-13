import pygame
from ball import Ball
WIDTH, HEIGHT = 800,600
WHITE = (255,255,255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()
    
    ball = Ball(WIDTH, HEIGHT)
    
    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =  False
                
            if event.type == pygame.KEYDOWN:
                
                print(f"pressed: {pygame.key.name(event.key)}")
                
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    ball.move(0,-ball.step)
                if event.type == pygame.K_DOWN or event.key == pygame.K_s:
                    ball.move(0, ball.step)
                if event.type == pygame.K_LEFT or event.key == pygame.K_a:
                    ball.move(-ball.step, 0)
                if event.type == pygame.K_RIGHT or event.key == pygame.K_d:
                    ball.move(ball.step, 0)
                
        ball.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()