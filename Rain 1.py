#membuat robot agar bisa belok kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#membuat robot bisa berputar
def turn_around():
    turn_left()
    turn_left()

#cek tembok
def check_wall():
    while wall_on_right():
        if wall_in_front():
             turn_left()  
        else:
             move()
                   
#membuat tembok
def close_wall():
    turn_right()
    build_wall()
    turn_left()

#####robot akan terus berjalan sampai tujuan#####
move()
turn_right()
move()

while not at_goal(): 
    check_wall()
    close_wall()
    
