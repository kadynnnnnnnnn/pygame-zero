import pgzrun
from  random import randint
timer = 30
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

hedgehog = Actor("hedgehog")
hedgehog.pos = 200,200

coin = Actor("coin")
coin.pos = 300,300

def draw():
    screen.fill("orange")            # fill means background. so, the background will be green

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10,10), fontsize=60)
        if score > 0:
            screen.draw.text("Winner: Fox", center=(WIDTH/2,HEIGHT/2), fontsize=40)
        elif score < 0:
            screen.draw.text("Winner: Hedgehog", center=(WIDTH/2,HEIGHT/2), fontsize=40)
        else:
            screen.draw.text("Draw!", center=(WIDTH/2,HEIGHT/2), fontsize=40)
    else:
        fox.draw()
        hedgehog.draw()
        coin.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))    # topleft -> where the topleft of the score will be
        screen.draw.text(str(round(timer,2)), topleft=(10,30), color = (255, 255,193), fontsize=30)
        screen.draw.text("fox : +10 / hedgehog : -10", color="black", topright=(390,10))


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))       

def time_up():
    global game_over    # global is used when trying to change 외부의 code
    game_over = True             

def update():
    global score
    global timer

    # fox
    if keyboard.left:
        if fox.x < 0+31:
            fox.x = 0+31
        else:
            fox.x = fox.x - 2
    elif keyboard.right:
        if fox.x > WIDTH-31:
            fox.x = WIDTH-31
        else:
            fox.x = fox.x + 2
    if keyboard.up:
        if fox.y < 0+42:    # adding 42 is half of the fox's size 
            fox.y = 0+42    # this constrains the fox from going above the height limit 
        else: 
            fox.y = fox.y - 4   # otherwise, the fox moves by 2 at a time
    elif keyboard.down:
        if fox.y > HEIGHT-42: 
            fox.y = HEIGHT-42
        else:
            fox.y = fox.y + 4


    # hedgehog
    if keyboard.a:
        if hedgehog.x < 0+27:
            hedgehog.x = 0+27
        else:
            hedgehog.x = hedgehog.x - 4
    elif keyboard.d:
        if hedgehog.x > WIDTH-27:
            hedgehog.x = WIDTH-27
        else:
            hedgehog.x = hedgehog.x + 4
    if keyboard.w:
        if hedgehog.y < 0+17:    # adding 42 is half of the fox's size 
            hedgehog.y = 0+17    # this constrains the fox from going above the height limit 
        else: 
            hedgehog.y = hedgehog.y - 2   # otherwise, the fox moves by 2 at a time
    elif keyboard.s:
        if hedgehog.y > HEIGHT-17: 
            hedgehog.y = HEIGHT-17
        else:
            hedgehog.y = hedgehog.y + 2


    coin_collected_fox = fox.colliderect(coin)
    coin_collected_hedgehog = hedgehog.colliderect(coin)

    if coin_collected_fox:
        score = score + 10
        place_coin()
    elif coin_collected_hedgehog:
        score -= 10     # -= is used for a loop. Ex: a=10. a-=1 would render a=9. ex: for i in range (5), a-=1. this would make a = 5.
        place_coin()

    timer -= 1/60

clock.schedule(time_up, timer)       # 30초가 지난 뒤  time_up이라는 함수를 실행시킴

place_coin()
pgzrun.go()