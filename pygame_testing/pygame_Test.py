# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([900, 900])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        print(pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0] == True:
            print("pressed")
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 0, 80, 80))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 130, 80, 80))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 260, 80, 80))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(140, 0, 80, 80))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(140, 130, 80, 80))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(140, 260, 80, 80))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(270, 0, 80, 80))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(270, 130, 80, 80))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(270, 260, 80, 80))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(120, 0, 10, 360))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(250, 0, 10, 360))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 110, 360, 10))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 240, 360, 10))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
