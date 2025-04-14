input.onButtonPressed(Button.A, function () {
    if (input.isGesture(Gesture.LogoUp)) {
        basic.showArrow(ArrowNames.North)
        guess.push(0)
    } else if (input.isGesture(Gesture.LogoDown)) {
        basic.showArrow(ArrowNames.South)
        basic.clearScreen()
        guess.push(1)
    } else if (input.isGesture(Gesture.TiltRight)) {
        basic.showArrow(ArrowNames.East)
        basic.clearScreen()
        guess.push(2)
    } else if (input.isGesture(Gesture.TiltLeft)) {
        basic.showArrow(ArrowNames.West)
        basic.clearScreen()
        guess.push(3)
    } else {
    	
    }
})
function show_array (array: number[]) {
    for (let value of array) {
        if (value == 0) {
            basic.showArrow(ArrowNames.North)
            basic.clearScreen()
            basic.pause(100)
        } else if (value == 1) {
            basic.showArrow(ArrowNames.South)
            basic.clearScreen()
            basic.pause(100)
        } else if (value == 2) {
            basic.showArrow(ArrowNames.East)
            basic.clearScreen()
            basic.pause(100)
        } else if (value == 3) {
            basic.showArrow(ArrowNames.West)
            basic.clearScreen()
            basic.pause(100)
        } else {
        	
        }
    }
}
input.onButtonPressed(Button.AB, function () {
    not_equal = 0
    if (list.length == guess.length) {
        for (let index = 0; index <= list.length; index++) {
            if (list[index] != guess[index]) {
                not_equal = 1
                break;
            }
        }
    } else {
        not_equal = 1
    }
    if (not_equal == 0) {
        basic.showIcon(IconNames.Yes)
        list.push(randint(0, 3))
        show_array(list)
        guess = []
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.B, function () {
    show_array(guess)
})
input.onGesture(Gesture.Shake, function () {
    guess = []
})
let not_equal = 0
let guess: number[] = []
let list: number[] = []
list = [randint(0, 3), randint(0, 3)]
show_array(list)
