label lunchLauncher:
    play music "audio/lunch-song.mp3" fadeout 2.0 fadein 2.0
    scene bg cafeteria with fade
    "The day wears on and soon lunchtime comes."
    "Who do you sit next to?"

    menu:
        "Deku":
            call lunch2izuku
        "Ochako":
            call lunch2ochako
        "Iida":
            call lunch2tenya
        "Todoroki":
            call lunch2shoto
        "Bakugo":
            call lunch2katsuki
        "Shinso":
            call lunch2hitoshi
return
