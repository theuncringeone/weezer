import pygame       #import stuff
import sys

pygame.init()       #initialization
run = True

screenx = 315       #get da display
screeny = 315

display = pygame.display.set_mode((screenx, screeny))   #init display
pygame.display.set_caption("weezer")

bluealbum_originalimage = pygame.image.load("bluealbum.png").convert()
bluealbum_img = pygame.transform.scale(bluealbum_originalimage, (screenx, screeny))     #whats with these programmers declaring my bluealbum.png
bluealbum_rect = bluealbum_img.get_rect()                                               #GET REKT!!!!
bluealbum_rect.center = (screenx // 2, screeny // 2)

pygame.display.set_icon(bluealbum_img)

lick = pygame.mixer.Sound("lick.mp3")       #what did they play on the mixer

while run:
    for event in pygame.event.get():                    #ooh ooh, and i handle events
        if event.type == pygame.QUIT:
            break

    display.blit(bluealbum_img, bluealbum_rect)         #ooh ooh, and i blit the thing
    pygame.display.flip()                               #ooh ooh, and now i flip displays
    channel = lick.play()
    while channel.get_busy():                           ################
        print("playing")                                #   L I C K    #
    print('finish')                                     ################
    break

pygame.quit()
sys.exit()