import pygame, sys
from button import Button
import math
import sys
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
RED = (255,0,0)

# Set up the simulation parameters
G = 9.81   # gravitational constant
L1 = 100   # length of the first pendulum arm
L2 = 100   # length of the second pendulum arm
M1 = 10    # mass of the first pendulum bob
M2 = 10    # mass of the second pendulum bob
theta1 = math.pi/2   # initial angle of the first pendulum arm
theta2 = math.pi/2   # initial angle of the second pendulum arm
omega1 = 0   # initial angular velocity of the first pendulum arm
omega2 = 0   # initial angular velocity of the second pendulum arm
pendamount = 0 #int(input("How many pendulums would you like to simulate? "))
#tuple which holds the pendulums characteristics/inital values
#pendulums = [(theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , RED), (theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , GREEN), 
             #(theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , BLUE), (theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , BLACK)] 


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def double_pendulum(theta1, theta2, omega1, omega2, delta_t, COLOR):
        # Calculate the angular accelerations
        alpha1 = (-G*(2*M1+M2)*math.sin(theta1) - M2*G*math.sin(theta1-2*theta2)
                   - 2*math.sin(theta1-theta2)*M2*(omega2**2*L2 + omega1**2*L1*math.cos(theta1-theta2))) / (L1*(2*M1+M2-M2*math.cos(2*theta1-2*theta2)))
        
        alpha2 = (2*math.sin(theta1-theta2)*((omega1**2*L1*(M1+M2))
                                              + G*(M1+M2)*math.cos(theta1) + omega2**2*L2*M2*math.cos(theta1-theta2))) / (L2*(2*M1+M2-M2*math.cos(2*theta1-2*theta2)))
   
        # Update the angular velocities
        omega1 += alpha1*delta_t
        omega2 += alpha2*delta_t
   
        # Update the angles
        theta1 += omega1*delta_t
        theta2 += omega2*delta_t
    
        # Calculate the positions of the pendulum bobs
        x1 = L1*math.sin(theta1)
        y1 = L1*math.cos(theta1)
        x2 = x1 + L2*math.sin(theta2)
        y2 = y1 + L2*math.cos(theta2)

        # Draw the pendulum arms and bobs
        
        pygame.draw.line(SCREEN, COLOR, (660, 350), (660+x1, y1+350), 2)
        pygame.draw.circle(SCREEN, COLOR, (660+x1, y1+350), M1)
        pygame.draw.line(SCREEN, COLOR, (660+x1, y1+350), (660+x2, y2+350), 2)
        pygame.draw.circle(SCREEN, COLOR, (660+x2, y2+350), M2)
        
        # Return the updated angles, velocities, and time to the tuples in the list
        return (theta1, theta2, omega1, omega2, delta_t, COLOR)

# Create a clock for timing
clock = pygame.time.Clock()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
     #int (input ("put # here"))
    pendulums = [(theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , BLACK)] 
    for i in range(pendamount):
     RANDCOLOR = (random.randint (0,255),random.randint (0,255),random.randint (0,255))
     pendulums.append((theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , RANDCOLOR))

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

       

        PLAY_BACK = Button(image=None, pos=(1120, 675), 
                            text_input="BACK", font=get_font(75), base_color="Grey", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        for i in range(pendamount):
            pendulums[i] = double_pendulum(pendulums[i][0], pendulums[i][1], pendulums[i][2], pendulums[i][3],pendulums [i][4], pendulums[i][5])
        pygame.display.update()
        
def options():
    global pendamount
    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))



        OPTIONS_TEXT = get_font(35).render("you are rendering " + str(pendamount)+ " pendulums", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        OPTIONS_TEXT2 = get_font(15).render("use up/down arrow to change pendulum amount", True, "White")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 360))

        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)

        OPTIONS_BACK = Button(image=None, pos=(1120, 675), 
                            text_input="BACK", font=get_font(75), base_color="Grey", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pendamount +=1
                if event.key == pygame.K_DOWN:
                    pendamount -=1

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("CHAOS THEORY", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()