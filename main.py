def on_button_pressed_a():
    if input.is_gesture(Gesture.LOGO_UP):
        basic.show_arrow(ArrowNames.NORTH)
        guess.append(0)
    elif input.is_gesture(Gesture.LOGO_DOWN):
        basic.show_arrow(ArrowNames.SOUTH)
        basic.clear_screen()
        guess.append(1)
    elif input.is_gesture(Gesture.TILT_RIGHT):
        basic.show_arrow(ArrowNames.EAST)
        basic.clear_screen()
        guess.append(2)
    elif input.is_gesture(Gesture.TILT_LEFT):
        basic.show_arrow(ArrowNames.WEST)
        basic.clear_screen()
        guess.append(3)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def show_array(array: List[number]):
    for value in array:
        if value == 0:
            basic.show_arrow(ArrowNames.NORTH)
            basic.clear_screen()
            basic.pause(100)
        elif value == 1:
            basic.show_arrow(ArrowNames.SOUTH)
            basic.clear_screen()
            basic.pause(100)
        elif value == 2:
            basic.show_arrow(ArrowNames.EAST)
            basic.clear_screen()
            basic.pause(100)
        elif value == 3:
            basic.show_arrow(ArrowNames.WEST)
            basic.clear_screen()
            basic.pause(100)
        else:
            pass

def on_button_pressed_ab():
    global not_equal, guess
    not_equal = 0
    if len(list2) == len(guess):
        index = 0
        while index <= len(list2):
            if list2[index] != guess[index]:
                not_equal = 1
                break
            index += 1
    else:
        not_equal = 1
    if not_equal == 0:
        basic.show_icon(IconNames.YES)
        list2.append(randint(0, 3))
        show_array(list2)
        guess = []
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    show_array(guess)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global guess
    guess = []
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

not_equal = 0
guess: List[number] = []
list2: List[number] = []
list2 = [randint(0, 3), randint(0, 3)]
show_array(list2)