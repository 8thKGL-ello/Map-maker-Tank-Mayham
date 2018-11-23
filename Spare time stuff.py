import os
import random
import pygame
import time

colc = 54

change_size = False

user_map = []
print("W for walls, T for teleport, ONLY TWO TELEPORTS ALLOWED")
print("TELEPORTS ONLY WORK ON THE EDGE OF THE MAP AND IF YOU USE 53 COLUMNS")
deciscion = input("[m]ake your own map or use set map? >> ")
if deciscion == "m" or deciscion == "M":
    row1 = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    row2 = "W" + input("ROW 2 >> ") + "W"
    row3 = "W " + input("ROW 3 >> ") + "W"
    row4 = "W" + input("ROW 4 >> ") + "W"
    row5 = "W" + input("ROW 5 >> ") + "W"
    row6 = "W" + input("ROW 6 >> ") + "W"
    row7 = "W" + input("ROW 7 >> ") + "W"
    row8 = "W" + input("ROW 8 >> ") + "W"
    row9 = "W" + input("ROW 9 >> ") + "W"
    row10 = "W" + input("ROW 10 >> ") + "W"
    row11 = "W" + input("ROW 11 >> ") + "W"
    row12 = "W" + input("ROW 12 >> ") + "W"
    row13 = "W" + input("ROW 13 >> ") + "W"
    row14 = "W" + input("ROW 14 >> ") + "W"
    row15 = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
    if len(row2) < 52:
        colc = len(row2)
        row2="W" + row2 + "W"
    if len(row3) < 52:
        row3="W" + row3 + "W"
        if len(row3) > colc:
            colc = len(row3)
    if len(row4) < 52:
        row4="W" + row4 + "W"
        if len(row4) > colc:
            colc = len(row4)
    if len(row5) < 52:
        row5="W" + row5 + "W"
        if len(row5) > colc:
            colc = len(row5)
    if len(row6) < 52:
        row6="W" + row6 + "W"
        if len(row6) > colc:
            colc = len(row6)
    if len(row7) < 52:
        row7="W" + row7 + "W"
        if len(row7) > colc:
            colc = len(row7)
    if len(row8) < 52:
        row8="W" + row8 + "W"
        if len(row8) > colc:
            colc = len(row8)
    if len(row9) < 52:
        row9="W" + row9 + "W"
        if len(row9) > colc:
            colc = len(row9)
    if len(row10) < 52:
        row10="W" + row10 + "W"
        if int(len(row10)) > colc:
            colc = int(len(row10))
    if int(len(row11)) < 52:
        row11="W" + row11 + "W"
        if int(len(row11)) > colc:
            colc = int(len(row11))
    if int(len(row12)) < 52:
        row12="W" + row12 + "W"
        if int(len(row12)) > colc:
            colc = int(len(row12))
    if int(len(row13)) < 52:
        row13="W" + row13 + "W"
        if int(len(row13)) > colc:
            colc = int(len(row13))
    if int(len(row14)) < 52:
        row14 = "W" + row14 + "W"
        if int(len(row14)) > colc:
            colc = int(len(row14))
    user_map.append(row1)
    user_map.append(row2)
    user_map.append(row3)
    user_map.append(row4)
    user_map.append(row5)
    user_map.append(row6)
    user_map.append(row7)
    user_map.append(row8)
    user_map.append(row9)
    user_map.append(row10)
    user_map.append(row11)
    user_map.append(row12)
    user_map.append(row13)
    user_map.append(row14)
    user_map.append(row15)
else:
    user_map = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        "W   WWWWWWWWWWWWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                                    W",
        "W                                                    W",
        "W   WWWWWWWW  WWWWWW   WWWW   WWWWWWW   WWWW    WWWWWW",
        "W     WWWWWW  WWWWWW   WWWW   WWWWWWW   WWWWWW   WWWWW",
        "T                                                    T",
        "W                                                    W",
        "WWW   WWWWWWWWWWWWWW   WWWWW   WWWWWW   WWWWWW WWW   W",
        "WWW                    WWWWWWW   WWWW   WWWWWW WWW   W",
        "WWWW  WWW   WWWWWWWW                                 W",
        "WWWW  WWWW    WWWWWW   WWWWW   WWWWWW   WWWWWWW  WWWWW",
        "WWWW  WWWWWWW   WWWW   WWWWWW   WWWWW   WWWWWWW  WWWWW",
        "WWWW  WWWWWWWW                          WW       WWWWW",
        "WWWW                   WWWWWWWWWWWWWW       WWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]


class Shoot(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 8, 8)
        if len(bullets2) < p2_shot_count:
            bullets2.append(self)


class Shoot2(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 8, 8)
        if len(bullets) < p1_shot_count:
            bullets.append(self)


# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)
        if change_size:
            self.rect = pygame.Rect(32, 32, 9, 9)

        self.rect2 = pygame.Rect(768, 32, 16, 16)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move2(self, dx2, dy2):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx2 != 0:
            self.move_single_axis2(dx2, 0)
        if dy2 != 0:
            self.move_single_axis2(0, dy2)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
        for teleport in tele:
            if self.rect.colliderect(teleport.rect):
                if dx > 0:
                    player.move(-810,0)
                if dx < 0:
                    player.move(810, 0)

    def move_single_axis2(self, dx2, dy2):

        # Move the rect
        self.rect2.x += dx2
        self.rect2.y += dy2

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect2.colliderect(wall.rect):
                if dx2 > 0:  # Moving right; Hit the left side of the wall
                    self.rect2.right = wall.rect.left
                if dx2 < 0:  # Moving left; Hit the right side of the wall
                    self.rect2.left = wall.rect.right
                if dy2 > 0:  # Moving down; Hit the top side of the wall
                    self.rect2.bottom = wall.rect.top
                if dy2 < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect2.top = wall.rect.bottom
        for teleport in tele:
            if self.rect2.colliderect(teleport.rect):
                if dx2 > 0:
                    player.move2(-810, 0)
                if dx2 < 0:
                    player.move2(810, 0)


# Nice class to hold a wall rect
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


class teleport(object):
    def __init__(self, pos):
        tele.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


class ability(object):
    def __init__(self, pos):
        power_up.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

clock = pygame.time.Clock()
walls = []  # List to hold the walls
tele = []
bullets = []
bullets2 = []
power_up = []
player = Player()  # Create the player

tele_count = 1

x = y = 0
for row in user_map:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "T" and tele_count < 3:
            teleport((x,y))
            tele_count += 1
        if col == " ":
            if random.randint(0,100) == 0:
                ability((x,y))
        x += 16
    y += 16
    x = 0

game_width = colc * 16

# Set up the display
pygame.display.set_caption("Do stuff")
screen = pygame.display.set_mode((game_width, 240))
# Parse the level string above. W = wall, E = exit

x_movement = 0
y_movement = 0

shooting = False

p1_shot_count = 10
p2_shot_count = 10

move_speed_adder_p2 = False
move_speed_adder_p1 = False

change_size = False

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()

    # Move the player if an arrow key is pressed
    if move_speed_adder_p1 == False:
        if key[pygame.K_LEFT]:
            player.move(-3, 0)
        if key[pygame.K_RIGHT]:
            player.move(3, 0)
        if key[pygame.K_UP]:
            player.move(0, -3)
        if key[pygame.K_DOWN]:
            player.move(0, 3)
        if key[pygame.K_COMMA]:
            Shoot2((player.rect.x, player.rect.y))
            shooting = True
    else:
        if key[pygame.K_LEFT]:
            player.move(-5, 0)
        if key[pygame.K_RIGHT]:
            player.move(5, 0)
        if key[pygame.K_UP]:
            player.move(0, -5)
        if key[pygame.K_DOWN]:
            player.move(0, 5)
        if key[pygame.K_COMMA]:
            Shoot2((player.rect.x, player.rect.y))
            shooting = True

    if move_speed_adder_p2 == False:
        if key[pygame.K_a]:
            x_movement = -3
            player.move2(-3, 0)
        if key[pygame.K_d]:
            x_movement = 3
            player.move2(3, 0)
        if key[pygame.K_w]:
            y_movement = -3
            player.move2(0, -3)
        if key[pygame.K_s]:
            y_movement = -3
            player.move2(0, 3)
        if key[pygame.K_e]:
            Shoot((player.rect2.x, player.rect2.y))
            shooting = True
    else:
        if key[pygame.K_a]:
            x_movement = -5
            player.move2(-5, 0)
        if key[pygame.K_d]:
            x_movement = 5
            player.move2(5, 0)
        if key[pygame.K_w]:
            y_movement = -5
            player.move2(0, -5)
        if key[pygame.K_s]:
            y_movement = -5
            player.move2(0, 5)
        if key[pygame.K_e]:
            Shoot((player.rect2.x, player.rect2.y))
            shooting = True

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for teleport in tele:
        pygame.draw.rect(screen, (255, 165, 0), teleport.rect)
    for power in power_up:
        pygame.draw.rect(screen, (255, 165, 100), power.rect)
    pygame.draw.rect(screen, (255, 0, 0), player.rect)
    pygame.draw.rect(screen, (200, 25, 255), player.rect2)
    if shooting:
        for bullet in bullets2:
            pygame.draw.rect(screen, (200, 25, 255), bullet.rect)
        for bullet in bullets:
            pygame.draw.rect(screen, (255, 0, 0), bullet.rect)

    for bullet in bullets2:
        if player.rect.colliderect(bullet.rect):
            print("You dead arrow key player")
            pygame.display.quit()
            quit()

    for bullet in bullets2:
        for wall in walls:
            if bullet.rect.colliderect(wall.rect):
                bullets2.remove(bullet.rect)

    for bullet in bullets2:
        for teleport in tele:
            if bullet.rect.colliderect(teleport.rect):
                if bullet.rect.x < 500:
                    bullet.rect.x += 810
                if bullet.rect.x > 500:
                    bullet.rect.x -= 810

    for bullet in bullets:
        if player.rect2.colliderect(bullet.rect):
            print("You dead wasd player")
            pygame.display.quit()
            quit()

    for bullet in bullets:
        for wall in walls:
            if bullet.rect.colliderect(wall.rect):
                bullets.remove(bullet.rect)

    for bullet in bullets:
        for bull in bullets2:
            if bullet.rect.colliderect(bull.rect):
                bullets.remove(bullet.rect)
                bullets2.remove(bull.rect)

    for bullet in bullets:
        for teleport in tele:
            if bullet.rect.colliderect(teleport.rect):
                if bullet.rect.x < 500:
                    bullet.rect.x += 810
                if bullet.rect.x > 500:
                    bullet.rect.x -= 810

    if len(bullets2) > 0:
        for bullet in bullets2:
            if player.rect2.x < player.rect.x:
                bullet.rect.x += 3
            else:
                bullet.rect.x -= 3

    if len(bullets) > 0:
        for bullet in bullets:
            if player.rect.x < player.rect2.x:
                bullet.rect.x += 3
            else:
                bullet.rect.x -= 3

    for power in power_up:
        if player.rect.colliderect(power.rect):
            power_chooser = random.randint(1, 3)
            if power_chooser == 1:
                power_up.remove(power.rect)
                p1_shot_count = 30
            elif power_chooser == 2:
                move_speed_adder_p1 = True
            elif power_chooser == 3:
                player.rect = pygame.Rect(player.rect.x, player.rect.y, 11, 11)

    for power in power_up:
        if player.rect2.colliderect(power.rect):
            power_chooser2 = random.randint(1,3)
            if power_chooser2 == 1:
                power_up.remove(power.rect)
                p2_shot_count = 30
            elif power_chooser2 == 2:
                power_up.remove(power.rect)
                move_speed_adder_p2 = True
            elif power_chooser2 == 3:
                player.rect2 = pygame.Rect(player.rect2.x, player.rect2.y, 11, 11)

    pygame.display.flip()