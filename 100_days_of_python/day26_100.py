from replit import audio
import os, time


def play():
    source = audio.play_file('audio.wav')
    source.paused = False  # unpause the playback
    while True:
        stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : "))
        if stop_playback == 2:
            source.paused = True  # let's pause the file
            return  # let's go back from this play() subroutine
        else:
            continue


while True:
    # clear the screen
    os.system("clear")
    print("🎵 MyPOD Music Player ")
    time.sleep(2)
    # Show the menu
    menu = int(input("Press 1 to Play\nPress 2 to Exit\nPress anything else to see the menu again.\n"))
    # take user's input

    # check whether you should call the play() subroutine depending on user's input
    if menu == 1:
        play()
    elif menu == 2:
        exit()
    else:
        continue