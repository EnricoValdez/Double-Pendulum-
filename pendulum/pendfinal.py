#credits:
# help with bugs: Ms.Ghent, and Mr.Moore
# help with math/understanding: https://en.wikipedia.org/wiki/Chaos_theory, and https://en.wikipedia.org/wiki/Double_pendulum
# help with pygame: https://www.pygame.org/docs/, and https://www.pygame.org/docs/ref/draw.html
# help with random: https://docs.python.org/3/library/random.html

#imported libraries
import pygame
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
pendamount = int(input("How many pendulums would you like to simulate? "))
#tuple which holds the pendulums characteristics/inital values
#pendulums = [(theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , RED), (theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , GREEN), 
             #(theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , BLUE), (theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , BLACK)] 
pendulums = [(theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , BLACK)] 
for i in range(5):
     RANDCOLOR = (random.randint (0,255),random.randint (0,255),random.randint (0,255))
     pendulums.append((theta1, theta2, omega1, omega2, random.uniform(0.009999999999999,0.01) , RANDCOLOR))

# Initialize Pygame
pygame.init()

# Set up the display
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Double Pendulum Simulation")

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
        
        pygame.draw.line(screen, COLOR, (350, 100), (350+x1, y1+100), 2)
        pygame.draw.circle(screen, COLOR, (350+x1, y1+100), M1)
        pygame.draw.line(screen, COLOR, (350+x1, y1+100), (350+x2, y2+100), 2)
        pygame.draw.circle(screen, COLOR, (350+x2, y2+100), M2)
        
        # Return the updated angles, velocities, and time to the tuples in the list
        return (theta1, theta2, omega1, omega2, delta_t, COLOR)

# Create a clock for timing
clock = pygame.time.Clock()

# Run the simulation loop
while True:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
            
    # Update the pendulum's angles, velocities, and positions on every itteration
    for i in range(5):
        pendulums[i] = double_pendulum(pendulums[i][0], pendulums[i][1], pendulums[i][2], pendulums[i][3],pendulums [i][4], pendulums[i][5])

    # Update the screen
    pygame.display.update()
    screen.fill(WHITE)
    


           

            


    

   
    
