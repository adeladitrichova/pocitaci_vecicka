let play_for = 0
let touched_on = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    play_for = randint(500, 2000)
    basic.showIcon(IconNames.EigthNote)
    music.playTone(Note.C, play_for)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_event_touched() {
    
    if (play_for > 0) {
        touched_on = control.millis()
    }
    
})
input.onLogoEvent(TouchButtonEvent.Released, function on_logo_event_released() {
    let dur: number;
    let diff: number;
    
    if (touched_on > 0) {
        dur = control.millis() - touched_on
        diff = dur - play_for
        led.plotBarGraph(diff, play_for)
        play_for = 0
        touched_on = 0
    }
    
})
