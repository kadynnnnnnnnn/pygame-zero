import pgzrun
from random import randint 

timer = 0
countdown = 9


WIDTH = 400
HEIGHT = 400

dots = []
lines = []


next_dot = 0

for dot in range(0,10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill("black")

    if(timer > 8):      # 점들 없어지고 난뒤 3초 뒤에 다시 나타나게 함
        for dot in dots:
            dot.draw()

        for line in lines:
            screen.draw.line(line[0], line[1], (255, 255, 255))    
    elif(timer > 5):        # 5초동안 점들 보이게 해놓고 그다음에 화면 goes pitch black, dots disappear
        screen.fill("black")
        screen.draw.text(str(int(countdown)), center=(WIDTH/2,HEIGHT/2), color=(255,255,193), fontsize=300)
    else:                       # 기본 코드 for the dots to appear
        if(timer % 1 > 0.5):    # 타이머가 지날때마다 remainder이 0.5초면 텍스트가 보이게 하면서 텍스트를 깜빡이게 한다 --> 더 잘 보임
            screen.draw.text("remember the dots", midtop=(WIDTH / 2,10), fontsize=30, owidth=0.1, ocolor="red")
        
        number = 1
        for dot in dots:
            dot.draw()
            screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
            number = number + 1

        for line in lines:
            screen.draw.line(line[0], line[1], (255, 255, 255))
    
    

def on_mouse_down(pos):
    global next_dot
    global lines

    if(timer > 8):
        if(next_dot < 10):              # 더 큰 개념의 if로 밑에 있는 코드들을 묶어서 dots이 10이 됬을때 뭘 눌러도 게임 안 튕기게 한다
            if dots[next_dot].collidepoint(pos):
                if next_dot:
                    lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
                next_dot = next_dot + 1
            else: 
                lines = []
                next_dot = 0                # 숫자가 0이면 false, 나머지 값은 싹 다 true

def update():
    global timer, countdown

    timer += 1/60
    countdown -= 1/60

pgzrun.go()