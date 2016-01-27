import simplegui
message="Stop on integer number min 2/5 times to win."

counter = 0
t = 0
tries = 0
wins = 0
last_stop = 0


def format(t):
    global counter
    a = counter // 600
    b = ((counter//100)%6)
    c = (counter//10)%10
    d = counter%10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)


def start():
    global message
    message="Stop on whole number to win."
    timer.start()
    
def stop():
    global tries
    global wins
    global tries
    global last_stop
    global message
    timer.stop()
    if counter != last_stop:
        tries += 1
        last_stop = counter
        if counter%10 == 0:
                wins += 1
    update_score()
    if counter%10==0 and tries-wins<=3:
        temp=2-wins
        message="Wins required : %s " %temp
        if temp==0:
            message="Congrats! You won the game."
            reset()
    elif tries-wins>3 or (tries>3 and wins==0):
        message = "Sorry,You lost."
        reset()
    else :
        message = "Try again"
    
  
        
def reset():
    global counter
    global tries
    global wins
    global last_stop
    timer.stop()
    counter = 0
    wins = 0
    tries = 0
    last_stop = 0
    

def tick():
    global counter
    counter += 1
    return counter

def draw(canvas):
    canvas.draw_text(message,(20,100),23,"Red")
    canvas.draw_text(format(t), (170, 160), 40, "Orange")
    canvas.draw_text(update_score(), (0, 25), 25, "White")
    
def update_score():
    global tries
    global wins
    return "Wins/tries : " + str(wins) + "/" + str(tries)
    

frame = simplegui.create_frame("Stopwatch: The Game", 450, 300)


timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
button1 = frame.add_button("Start", start, 50)
button2 = frame.add_button("Stop", stop, 50)
button3 = frame.add_button("Reset", reset, 50)


frame.start()
