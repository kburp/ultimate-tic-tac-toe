# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

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

    # to set width of the game window
    width = 1000
    # to set height of the game window
    height = 1000

    # to set width of individual games "windoes"
    smallWidth = 300
    smallHeight = 300

    # calculate margins for small games
    margin = ((width / 3) - smallWidth) / 2
  
    # color of the straightlines on that 
    # white game board, dividing board 
    # into 9 parts
    line_color = (0, 0, 0)


    # Draw Ultimate board
        # drawing vertical lines
    pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
   
    # Draw Ultimate board
        # drawing horizontal lines
    pygame.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pygame.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)

    # draw small tic tac toe games
    for changeInX in range(3):
        distChangeX = changeInX * (width / 3)

        for changeInY in range(3):
            distChangeY = changeInY * (width / 3)

            # drawing vertical lines
            pygame.draw.line(screen, line_color, ((smallWidth / 3) + distChangeX, margin + distChangeY), ((smallWidth / 3) + distChangeX, smallHeight + distChangeY), 7)
            pygame.draw.line(screen, line_color, ((smallWidth / 3 * 2) + distChangeX, margin + distChangeY), ((smallWidth / 3 * 2) + distChangeX, smallHeight + distChangeY), 7)
        
            # drawing horizontal lines
            pygame.draw.line(screen, line_color, (margin + distChangeX, (smallHeight / 3) + distChangeY), (smallWidth + distChangeX, (smallHeight / 3) + distChangeY), 7)
            pygame.draw.line(screen, line_color, (margin + distChangeX, (smallHeight / 3 * 2) + distChangeY), (smallWidth + distChangeX, (smallHeight / 3 * 2) + distChangeY), 7)
        

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
