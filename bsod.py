import pygame
import pyqrcode
import _thread
import random
from PIL import Image
from pygame.locals import *

# Initialize Pygame
pygame.init()

##########################################################################
#
#  Function to help locate the UI elements on the screen
#
##########################################################################
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

screenshot = pygame.image.load('Bsodwindows10.png')
###########################################################################
# And within the `print_bsod` function:
#blit_alpha(screen, screenshot, (0, 0), 128)


def get_random_stopcode(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return random.choice(lines).strip()

# Generate a QR code
url = pyqrcode.create('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
url.png('qrcode_temp.png', scale=4)

# Open the QR code and invert the colors
im = Image.open('qrcode_temp.png')
im = im.convert("RGB")
datas = im.getdata()

new_image = []
for item in datas:
    # change all black pixels to blue
    if item[0] in list(range(0, 50)):
        new_image.append((0, 120, 215))
    # change all white pixels to white
    else:
        new_image.append((255, 255, 255))

im.putdata(new_image)
im.save("qrcode.png")



# Set the dimensions of the window
infoObject = pygame.display.Info()
size = (1920, 1080)
screen = pygame.display.set_mode(size, FULLSCREEN | SCALED)

# Define colors
blue = (0, 120, 215)
white = (255, 255, 255)

# Load QR code image
qrcode = pygame.image.load('qrcode.png')
qrcode = pygame.transform.scale(qrcode, (115, 115))

# Define font sizes
font_large_size = 210
font_medium_size = 40
font_small_size = 20
font_info_size = 16

# Load Segoe UI font
try:
    font_search_string = "Segoe UI Semilight, Wingdings"
    
    font_large = pygame.font.SysFont(font_search_string, font_large_size)
    font_medium = pygame.font.SysFont(font_search_string, font_medium_size)
    font_small = pygame.font.SysFont(font_search_string, font_small_size)
    font_info = pygame.font.SysFont(font_search_string, font_info_size)
except FileNotFoundError:
    print("Font not found, using default font")
    font_large = pygame.font.Font(None, font_large_size)
    font_medium = pygame.font.Font(None, font_medium_size)
    font_small = pygame.font.Font(None, font_small_size)
    font_info = pygame.font.Font(None, font_info_size)

# Define positions
frown_pos = [190, 105]
line1_pos = [208, 391]
line2_pos = [208, 450]
line3_pos = [208, 510]
line4_pos = [343, 695]
error1_pos = [343, 762]
error2_pos = [343, 795]
qrcode_pos = [208, 700]
progress_pos = [208, 600]
progress_text_pos = [290, 600]

def print_bsod():
    pygame.mouse.set_visible(False)
    screen.fill(blue)
    
    #### TEST STUFF
    #blit_alpha(screen, screenshot, (0, 0), 128)
    #### TEST STUFF END
    
    text = font_large.render(":(", True, white)
    screen.blit(text, frown_pos)
    text = font_medium.render("Your PC ran into a problem and needs to restart. We're", True, white)
    screen.blit(text, line1_pos)
    text = font_medium.render("just collecting some error info, and then we'll restart for", True, white)
    screen.blit(text, line2_pos)
    text = font_medium.render("you.", True, white)
    screen.blit(text, line3_pos)
    text = font_small.render("For more information about this issue and possible fixes, visit https://www.windows.com/stopcode", True, white)
    screen.blit(text, line4_pos)
    text = font_info.render("If you call a support person, give them this info:", True, white)
    screen.blit(text, error1_pos)
    text = font_info.render("Stop code: {}".format(get_random_stopcode('stopcodes.txt')), True, white)
    screen.blit(text, error2_pos)
    screen.blit(qrcode, qrcode_pos)
    text = font_medium.render("complete", True, white)
    screen.blit(text, progress_text_pos)
    pygame.display.flip()

    for i in range(1, 101):
        pygame.time.wait(300)
        text = font_medium.render("{}%".format(i), True, white)
        screen.fill(blue, (progress_pos[0], progress_pos[1], 80, 60))
        screen.blit(text, progress_pos)
        pygame.display.flip()

        # Take a screenshot at 1%
        if i == 1:
            pygame.image.save(screen, 'screenshot.png')

        # Check for the quit event inside the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return

    #pygame.time.wait(5000)

try:
    print_bsod()
finally:
    pygame.mouse.set_visible(True)
    pygame.quit()
