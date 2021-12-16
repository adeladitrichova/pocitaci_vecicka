play_for = 0
touched_on = 0
def on_button_pressed_a():
    global play_for
    play_for = randint(500, 2000)
    basic.show_icon(IconNames.EIGTH_NOTE)
    music.play_tone(Note.C, play_for)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_logo_event_touched():
    global touched_on
    if play_for > 0:
        touched_on = control.millis()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_event_touched)
def on_logo_event_released():
    global touched_on, play_for
    if touched_on > 0:
        dur = control.millis() - touched_on
        diff = dur - play_for
        led.plot_bar_graph(diff, play_for)
        play_for = 0
        touched_on = 0
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_event_released)
