label beginning:

    play music "audio/ill-become-a-hero.mp3" fadeout 0.0 fadein 3.0
    scene bg blue with fade
    show riley at center with dissolve

    "You're Riley Marshall."
    "An exchange student from America, who is transferring into class 1-A under special recommendation. Your quirk is Heat Vision which allows you to see in infrared and to absorb and refract heat from your eyes."
    hide riley with dissolve
    menu:
        "What are your pronouns?"

        "She, please!":
            $ shehethey = "she"
            $ herhimthem = "her"
            $ herhistheir = "her"
            $ hershistheirs = "hers"
            $ wantwants = "wants"
            riley "She, please!"
        "He, please!":
            $ shehethey = "he"
            $ herhimthem = "him"
            $ herhistheir = "his"
            $ hershistheirs = "his"
            $ wantwants = "wants"
            riley "He, please!"
        "They, please!":
            $ shehethey = "they"
            $ herhimthem = "them"
            $ herhistheir = "their"
            $ hershistheirs = "theirs"
            $ wantwants = "want"
            riley "They, please!"
