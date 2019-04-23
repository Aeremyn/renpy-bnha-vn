label lunchtime1:
    scene bg cafeteria with fade
    play music "audio/lunch-song.mp3" fadeout 2.0 fadein 2.0
    "Who do you sit next to?"
    call screen lunchtime


    label lunch1ochako:
        $ ochakopoints += 1
        if ochakoName == "Ochako":
            show ochako at center with dissolve
            ochako "Hi Riley! Isn't the food here terrific?"
            "She eats another spoonful of curry."
            ochako "Have you met everyone in class yet? Probably not right? I'll introduce you after we eat, so dig in!"
            riley "Ok, thanks!"
            "She finishes eating and waits for you to finish."
            ochako "Okay Riley, I hope you're ready for lots of introductions!"
        else:
            show ochako at center with dissolve
            ochako "Oh hi, it's Riley right? I'm Ochako."
            $ ochakoName = "Ochako"
            "She eats another spoonful of curry."
            ochako "Have you met everyone in class yet? Probably not right? I'll introduce you after we eat, so dig in!"
            riley "Ok, thanks!"
            "She finishes eating and waits for you to finish."
            ochako "Okay Riley, I hope you're ready for lots of introductions!"
        hide ochako with dissolve
        $ izukuLunchNum = 2
        $ izukuLunchString = "%d" % izukuLunchNum
        $ ochakoLunchNum = 2
        $ ochakoLunchString = "%d" % ochakoLunchNum
        $ tenyaLunchNum = 2
        $ tenyaLunchString = "%d" % tenyaLunchNum
        $ shotoLunchNum = 2
        $ shotoLunchString = "%d" % shotoLunchNum
        $ katsukiLunchNum = 2
        $ katsukiLunchString = "%d" % katsukiLunchNum
    return



    label lunch1izuku:
        $ izukupoints += 1
        show izuku at center with dissolve
        izuku "O-oh hi, you're Riley right? I'm Izuku Midoriya, or you can call me Deku if you like."
        $ izukuName = "Deku"
        "He smiles an unsure smile."
        riley "Nice to meet you, Deku."
        "His smile widens and he opens his mouth to speak but another voice drowns his out."
        hide izuku with dissolve
        show ochako at center with easeinright
        if ochakoName == "Ochako":
            ochako "Hey Riley, I hope you're ready for lots of introductions!"
        else:
            ochako "Hey, it's Riley right? I hope you're ready for lots of introductions!"
        hide ochako with dissolve
        $ izukuLunchNum = 2
        $ izukuLunchString = "%d" % izukuLunchNum
        $ ochakoLunchNum = 2
        $ ochakoLunchString = "%d" % ochakoLunchNum
        $ tenyaLunchNum = 2
        $ tenyaLunchString = "%d" % tenyaLunchNum
        $ shotoLunchNum = 2
        $ shotoLunchString = "%d" % shotoLunchNum
        $ katsukiLunchNum = 2
        $ katsukiLunchString = "%d" % katsukiLunchNum
    return



    label lunch1katsuki:
        show katsuki at center with dissolve
        "The spikey haired boy glares at you."
        katsuki "What do you want?"
        "The red-haired boy next to him speaks up."
        eijiro "Hey be nice, Bakugo!"
        "Bakugo ignores him."
        show katsuki with hpunch
        katsuki "WELL, WHAT DO YOU WANT?"
        menu:
            "I just thought I'd introduce myself.":
                riley "I just thought I'd introduce myself to my new classmates."
                katsuki "Well buzz off, nerd!"
                hide katsuki with dissolve
                if ochakoName == "Ochako":
                    "Just then, Ochako appears at your side."
                    show ochako at center with easeinright
                    ochako "Hey Riley, I hope you're ready for lots of introductions!"
                else:
                    "Just then, the brown haired girl from class appears at your side."
                    show ochako at center with easeinright
                    ochako "Hey, it's Riley right? I hope you're ready for lots of introductions!"
            "I just need a place to sit.":
                $ katsukipoints += 1
                riley "I just need a place sit, not everything is about you."
                katsuki "Tch..."
                "He looks mildly annoyed, but doesn't say anything else."
                hide katsuki with dissolve
                if ochakoName == "Ochako":
                    "Just then, Ochako appears at your side."
                    show ochako at center with easeinright
                    ochako "Hey Riley, I hope you're ready for lots of introductions!"
                else:
                    "Just then, the brown haired girl from class appears at your side."
                    show ochako at center with easeinright
                    ochako "Hey, it's Riley right? I hope you're ready for lots of introductions!"
        hide ochako with dissolve
        $ izukuLunchNum = 2
        $ izukuLunchString = "%d" % izukuLunchNum
        $ ochakoLunchNum = 2
        $ ochakoLunchString = "%d" % ochakoLunchNum
        $ tenyaLunchNum = 2
        $ tenyaLunchString = "%d" % tenyaLunchNum
        $ shotoLunchNum = 2
        $ shotoLunchString = "%d" % shotoLunchNum
        $ katsukiLunchNum = 2
        $ katsukiLunchString = "%d" % katsukiLunchNum
    return



    label lunch1tenya:
        $ tenyapoints += 1
        show tenya at center with dissolve
        tenya "Ah! It's Riley, isn't it? Nice to meet you! My name is Tenya Iida, pleased to make your acquaintance."
        $ tenyaName = "Iida"
        "He looks at the food on your tray."
        tenya "Be sure to eat all your food, a well-balanced diet is vital to our continued learning here at U.A."
        riley "Nice to meet you too, Iida. I'll be sure to keep that in mind."
        "He smiles at you and looks like he's about to speak when another voice interrupts."
        hide tenya with dissolve
        show ochako at center with easeinright
        if ochakoName == "Ochako":
            ochako "Hey Riley, I hope you're ready for lots of introductions!"
        else:
            ochako "Hey, it's Riley right? I hope you're ready for lots of introductions!"
        hide ochako with dissolve
        $ izukuLunchNum = 2
        $ izukuLunchString = "%d" % izukuLunchNum
        $ ochakoLunchNum = 2
        $ ochakoLunchString = "%d" % ochakoLunchNum
        $ tenyaLunchNum = 2
        $ tenyaLunchString = "%d" % tenyaLunchNum
        $ shotoLunchNum = 2
        $ shotoLunchString = "%d" % shotoLunchNum
        $ katsukiLunchNum = 2
        $ katsukiLunchString = "%d" % katsukiLunchNum
    return



    label lunch1shoto:
        $ shotopoints += 1
        if shotoName == "Todoroki":
            show shoto at center with dissolve
            "Todoroki seems to be surprised you decided to sit next to him, but doesn't say anything."
            riley "Hi again, Todoroki."
            "He looks like he's about to say something, but another voice interrupts."
            hide shoto with dissolve
            show ochako at center with easeinright
            if ochakoName == "Ochako":
                ochako "Hey Riley, I hope you're ready for lots of introductions!"
            else:
                ochako "Hey, it's Riley right? I hope you're ready for lots of introductions!"
        else:
            show shoto at center with dissolve
            "The boy seems to be surprised you decided to sit next to him, but doesn't say anything."
            riley "Hi, nice to meet you."
            "He looks like he's about to say something, but another voice interrupts."
            hide shoto with dissolve
            show ochako at center with easeinright
            if ochakoName == "Ochako":
                ochako "Hey Riley, I hope you're ready for lots of introductions!"
            else:
                ochako "Hey, it's Riley right? I hope you're ready for lots of introductions!"
        hide ochako with dissolve
        $ izukuLunchNum = 2
        $ izukuLunchString = "%d" % izukuLunchNum
        $ ochakoLunchNum = 2
        $ ochakoLunchString = "%d" % ochakoLunchNum
        $ tenyaLunchNum = 2
        $ tenyaLunchString = "%d" % tenyaLunchNum
        $ shotoLunchNum = 2
        $ shotoLunchString = "%d" % shotoLunchNum
        $ katsukiLunchNum = 2
        $ katsukiLunchString = "%d" % katsukiLunchNum
    return

    label lunch1hitoshi:
        $ hitoshipoints += 1
        show hitoshi at center with dissolve
        "He seems surprised you chose to sit with him."
        riley "Hi Shinso."
        hitoshi "Hey Riley."
        "A long uncomfortable silence passes between the two of you."
        if ochakoName == "Ochako":
            "You open your mouth to speak, but another voice drowns yours out."
            hide hitoshi with dissolve
            show ochako at center with easeinright
            ochako "Hey Riley, I hope you're ready for lots of introductions!"
        else:
            "You open your mouth to speak, but another voice drowns yours out."
            hide hitoshi with dissolve
            show ochako at center with easeinright
            ochako "Hey, it's Riley right? I hope you're ready for lots of introductions!"
        hide ochako with dissolve
        $ izukuLunchNum = 2
        $ izukuLunchString = "%d" % izukuLunchNum
        $ ochakoLunchNum = 2
        $ ochakoLunchString = "%d" % ochakoLunchNum
        $ tenyaLunchNum = 2
        $ tenyaLunchString = "%d" % tenyaLunchNum
        $ shotoLunchNum = 2
        $ shotoLunchString = "%d" % shotoLunchNum
        $ katsukiLunchNum = 2
        $ katsukiLunchString = "%d" % katsukiLunchNum
        $ hitoshiLunchNum = 2
        $ hitoshiLunchString = "%d" % hitoshiLunchNum
    return
return
