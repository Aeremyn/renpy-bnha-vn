label credits:
    $ credits_speed = 84
    $ quick_menu = False
    scene bg black with fade
    play music "audio/HEROES.mp3" noloop
    show credits_image at Move((0.5, 0.0), (0.5, -4.0), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+5)
