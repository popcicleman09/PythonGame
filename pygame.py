import pygame as pg

pg.init()
screen = pg.display.set_mode((400, 300))
done = False

while not done:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True
        
        pg.display.flip()

def gameStart:
		print "Starting Game"

if event.type == pg.KEYDOWN and event.key == pg.K_ENTER:
	gameStart

if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
        moveleft
        
if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
        moveright
        
if event.type == pg.KEYDOWN and event.key == pg.K_UP:
        moveup
        
if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
	movedown



