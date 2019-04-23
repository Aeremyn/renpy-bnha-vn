label seatchoice:
    scene bg classroom-front-view with fade
    "There are four seats available at the back of the classroom."
    call screen seatingchart

    label seatmomo:
        "Your new neighbor sits straight up in her seat, as if standing at attention, and watches you."
        "When you sit she greets you in perfect English."
        momo "Hello, I'm Momo Yaoyourozu, it is very nice to meet you."
        $ momoName = "Momo"
        riley "Hello Momo, it's nice to meet you too. Your English is very good."
        "This time she speaks in Japanese."
        momo "Thank you, if you need any help, please let me know."
        riley "Thank you, I will."
        aizawa "Alright, time to start class!"
    return

    label seatshoto:
        $ shotopoints += 1
        show shoto at center with dissolve
        "Your new neighbor watches you with interest as you approach your new desk."
        "By the time you sit down he has partially turned in his seat to look at you."
        shoto "Shoto Todoroki, welcome to class 1-A."
        $ shotoName = "Todoroki"
        riley "Nice to meet you, Todoroki."
        "He nods then turns back around."
        hide shoto with dissolve
        aizawa "Alright, time to start class!"
    return

    label seatrikido:
        "Your new neighbor gives you a warm smile as you approach and turns around to watch you take your seat."
        rikido "I'm Rikido Sato, if you need help with anything let me know. Welcome to Class 1-A, Marshall."
        $ rikidoName = "Sato"
        riley "Thanks. Nice to meet you, Sato."
        rikido "Nice to meet you too, Marshall. I hope we become friends."
        aizawa "Alright, time to start class!"
    return

    label seatochako:
        $ ochakopoints += 1
        show ochako at center with dissolve
        "Your new neighbor smiles warmly at you as you make your way down the aisle of desks."
        ochako "I'm Ochako Uraraka nice to meet you! You can just call me Ochako. Welcome to Class 1-A!"
        "She smiles widely at you."
        $ ochakoName = "Ochako"
        riley "Thanks Ochako, nice to meet you!"
        ochako "If you need any help let me know!"
        hide ochako with dissolve
        aizawa "Alright, time to start class!"
    return
