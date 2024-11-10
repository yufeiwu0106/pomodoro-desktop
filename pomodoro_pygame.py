from pomodoro_button import PomodoroButton
from shortbreak_button import ShortbreakButton
from longbreak_button import LongbreakButton
from start_button import StartButton
from exit_button import ExitButton
from id_text import IdText
from timer import Timer
from id_input_box import IdInputBox
from user import User
from db import Database

import pygame
import pygame_menu


WIDTH, HEIGHT = 1200, 800
FONT_SIZE = 38
START_COUNTDOWN = False
COUNTER = 25 * 60
IS_WORK_MODE = True

NEEDS_DRAW = [] # Rectangles that need to be displayed. clock will always be the last element
SELECTED_BUTTON = None

def main():
    db = Database()
    db.init()

    # initialize the game window
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))


    pomodoro_button = PomodoroButton(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
    )
    pomodoro_button.draw()
    NEEDS_DRAW.append(pomodoro_button)

    shortbreak_button = ShortbreakButton(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
    )
    shortbreak_button.draw()
    NEEDS_DRAW.append(shortbreak_button)

    longbreak_button = LongbreakButton(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
    )
    longbreak_button.draw()
    NEEDS_DRAW.append(longbreak_button)

    start_button = StartButton(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
    )
    start_button.draw()
    NEEDS_DRAW.append(start_button)

    exit_button = ExitButton(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
    )
    exit_button.draw()
    NEEDS_DRAW.append(exit_button)
    
    id_text = IdText(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
    )
    id_text.draw()
    NEEDS_DRAW.append(id_text)

    id_input_box = IdInputBox(
        width=WIDTH,
        height=HEIGHT,
        window=window,
    )
    id_input_box.draw()
    NEEDS_DRAW.append(id_input_box)

    
    # NOTE: timer needs to be added at last
    timer = Timer(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
        counter=1500, # 25 mins
    )
    timer.draw()
    NEEDS_DRAW.append(timer)

    # menu.add.button("Start", start_the_game)
    # menu.add.button("Quit", pygame_menu.events.EXIT)

    run_eventloop(
        window,
        start_button,
        exit_button,
        pomodoro_button,
        shortbreak_button,
        longbreak_button,
        id_text,
        id_input_box,
        db
    )

def run_eventloop(
    window,
    start_button,
    exit_button,
    pomodoro_button,
    shortbreak_button,
    longbreak_button,
    id_text,
    id_input_box,
    db,
):
    global START_COUNTDOWN # init: False
    global COUNTER
    global SELECTED_BUTTON
    global IS_WORK_MODE # init: True

    SELECTED_BUTTON = pomodoro_button

    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        
        # After this for loop, we should know which rectangles should be drawn
        for event in pygame.event.get():

            # Detects clicking start button event
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if event object type is QUIT then quitting the pygame and program both.
                if exit_button.get_button_rect().collidepoint(event.pos):
                    # deactivates the pygame libr
                    pygame.quit()
                    quit()

                
                if event.button == 1:  # left mouse button
                    if start_button.get_button_rect().collidepoint(event.pos): # check if the click collides with the start button rectangle
                        play_start()

                        if start_button.paused:
                            # If the countdown is in progress, pause the countdown
                            START_COUNTDOWN = False
                            start_button.set_started()
                            print("Countdown start!")

                        else: # If the countdown is paused, restart the countdown
                            START_COUNTDOWN = True
                            start_button.set_paused()
                            print("Countdown paused!")

                        # if COUNTDOWN = 0, then stop countdown timer.
                        if COUNTER == 0:
                            START_COUNTDOWN = False
                            print("Countdown reached 0, stopping countdown.")
                        
                    if pomodoro_button.get_button_rect().collidepoint(event.pos):
                        play_click()
                        print("User resets pomodoro timer. Stop countdown.")
                        # POMODORO_COUNTER = 1500 # reset start counter
                        COUNTER = 1500 # reset counter
                        START_COUNTDOWN = False # stop count down
                        reset_timer(window, 25 * 60) # update NEEDS_DRAW to 25 minutes
                        SELECTED_BUTTON = pomodoro_button
                        start_button.set_started()
                        IS_WORK_MODE = True
                    if shortbreak_button.get_button_rect().collidepoint(event.pos):
                        play_click()
                        print("User resets short break timer. Stop countdown.")
                        COUNTER = 5 * 60
                        START_COUNTDOWN = False
                        reset_timer(window, 5 * 60) 
                        SELECTED_BUTTON = shortbreak_button
                        start_button.set_started()
                        IS_WORK_MODE = False
                    if longbreak_button.get_button_rect().collidepoint(event.pos):
                        play_click()
                        print("User resets long break timer. Stop countdown.")
                        COUNTER = 15 * 60
                        START_COUNTDOWN = False
                        reset_timer(window, 15 * 60)
                        SELECTED_BUTTON = longbreak_button
                        start_button.set_started()
                        IS_WORK_MODE = False

            # Detect key down (typing)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    id_input_box.text = id_input_box.text[:-1]
                elif event.key == pygame.K_RETURN:
                    user = User(
                        width=WIDTH,
                        height=HEIGHT,
                        window=window,
                        user_name=id_input_box.text,
                        db=db,
                    ) # Initialize user with user id
                    print(f"Username is: {user.user_name}")
                    user.init_row()
                    NEEDS_DRAW.insert(0, user)

                else:
                    id_input_box.text += event.unicode

            if START_COUNTDOWN and event.type == timer_event:
                COUNTER -= 1
                # pop the old counter and push the new to refresh the timer
                NEEDS_DRAW.pop()
                timer = Timer(
                    width=WIDTH,
                    height=HEIGHT,
                    font_size=FONT_SIZE,
                    window=window,
                    counter=COUNTER,
                ) 
                NEEDS_DRAW.append(timer)

                # add_timer_easy(window, WIDTH, HEIGHT)
                pygame.display.flip()

                # countdow completes
                if COUNTER == 0:
                    start_button.toggle_text()
                    START_COUNTDOWN = False # Stop checking the timer 
                    # pygame.time.set_timer(timer_event, 0)
                    play_notif()

                    # if mode is Work, then need to update work times in db
                    if IS_WORK_MODE:
                        user.refresh_work_times()


        # draw all rectangle
        window.fill((244, 236, 220))
        for rect in NEEDS_DRAW:
            rect.draw()

        if SELECTED_BUTTON is not None:
            SELECTED_BUTTON.draw_hint()

        pygame.display.update()


def reset_timer(window, counter):
    NEEDS_DRAW.pop()
    timer = Timer(
        width=WIDTH,
        height=HEIGHT,
        font_size=FONT_SIZE,
        window=window,
        counter=counter,
    )
    NEEDS_DRAW.append(timer)

    # pygame.time.set_timer(timer_event, 1000)

    


def play_notif():
    """
    Load a sound file and play
    """
    notifsound = pygame.mixer.Sound("notif.mp3")
    notifsound.play()


def play_click():
    """
    Load the click button sound
    """
    clickbutton = pygame.mixer.Sound("click.mp3")
    clickbutton.play()


def play_start():
    """
    Load the start button sound
    """
    clickstart = pygame.mixer.Sound("start.mp3")
    clickstart.play()

if __name__ == "__main__":
    main()
