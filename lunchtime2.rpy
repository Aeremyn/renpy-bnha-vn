label lunch2izuku:
    if izukuLunch = 2:
        $ izukupoints += 1
        show izuku at center
        with dissolve
        "You sit down next to Deku."
        izuku "Hi Riley."
        riley "Hey Deku. What'cha eating?"
        izuku "Katsudon, it's my favorite!"
        riley "Ahh, I've never tried it."
        izuku "Here, have some."
        "He offers his bowl to you. You gingerly take a piece and stick it in your mouth."
        riley "Itsch Delishish."
        izuku "Haha, I think so too."
        "The two of you chat the rest of lunch away and then it's time to return to class."
        $ izukuLunch = 3
    else:
        call lunch3izuku
return

label lunch2ochako:
    if ochakoLunch = 2:
        $ ochakopoints += 1
        show ochako at center
        with dissolve
        "You sit down next to Ochako."
        ochako "Hey Riley."
        riley "Hi Ochako."
        if not ochakoMall:
            ochako "Hey do you have any plans for the weekend? Wanna go hangout at the mall?"
            menu:
                "Sure.":
                    ochako "Great, this'll be fun. We'll go shopping and maybe see a movie or something."
                    riley "Sounds like fun."
                    $ ochakoMall = True
                    $ ochakopoints += 1
                "Sorry, I have plans.":
                    ochako "Aww, too bad. Maybe next time?"
                    riley "Yeah, next time."
        else:
            ochako "So, is pizza your favorite food Riley?"
            "You stop as you're about to take another bite."
            riley "Haha, is it that obvious?"
            ochako "It's just that I noticed you got the same thing yesterday, hehe."
            riley "What about you Ochako? What's your favorite food?"
            ochako "Me? I dunno, I like anything japanese, but I guess... Mochi, mochi is my favorite."
            riley "Ahh, too bad they don't serve that here."
            ochako "Yeah."
            "She pouts at first, then shakes herself."
            ochako "But they have plenty of other delicious food, we're really lucky!"
            riley "That's true!"
        "You and Ochako chitchat lunch away and then head back to class."
        $ ochakoLunch = 3
    else:
        call lunch3ochako
return

label lunch2tenya:
    if tenyaLunch = 2:
        $ tenyapoints += 1
        show tenya at center
        with dissolve
        "You sit down next to Iida."
        tenya "Greetings Riley."
        riley "Hey Iida."
        "He looks at your tray."
        tenya "Make sure you're getting proper nuitrition from your meals Riley."
        "You look down at your plate of pizza."
        tenya "As aspiring heroes we must be sure to keep our bodies it peak physical form!"
        riley "Maybe I should eat better... but I think you should relax and eat whatever you want once in a while too."
        "You look at Iida's plate. Well balanced and perfectly portioned."
        riley "I think you can definitely relax a little, you seem to eat right all the time."
        tenya "Hmm, I suppose you do have a point. As I've said before, relaxing is important too."
        "Still, the rest of lunch Iida attempts to teach you the importance of eating each food group and in proper portions."
        $ tenyaLunch = 3
    else:
        call lunch3tenya
return

label lunch2shoto:
    if shotoLunch = 2:
        $ shotopoints += 1
        show shoto at center
        with dissolve
        "You sit down next to Todoroki."
        riley "Hi Todoroki."
        shoto "Hi."
        "You sit there silently for a minute."
        riley "What do you think we'll be doing for Hero Training today?"
        shoto "Hmm..."
        "He thinks for a bit."
        shoto "Probably more rescue training, but Aizawa might surprise us."
        riley "I just hope it's not a test, I haven't caught up yet."
        shoto "I don't think we'll have a test yet, but I can help you study if you want."
        riley "Really? That'd be great!"
        "You spend the rest of lunch talking and studying with Todoroki."
        $ shotoLunch = 3
    else:
        call lunch3shoto
return

label lunch2katsuki:
    if katsukiLunch = 2:
        $ katsukipoints += 1
        show katsuki at center
        with dissolve
        "You sit down next to Bakugo."
        katsuki "Hey nerd."
        riley "Hey Bakugo."
        "The two of you eat in silence for a while."
        katsuki "So, what's America like?"
        riley "It's okay, I think I like Japan better though."
        katsuki "You have any friends back in the States?"
        riley "Mmm, not really. You don't seem to have a lot of friends either."
        katsuki "I guess so."
        riley "Just a couple of loners I guess, huh?"
        katsuki "Heh, we're not really loners if we're together."
        riley "Haha, I guess that's true."
        "Lunch soon ends and it's time to go back to class."
        $ katsukiLunch = 3
    else:
        call lunch3katsuki
return

label lunch2hitoshi:
    if hitoshiLunch = 2:
        $ hitoshipoints += 1
        show hitoshi at center with dissolve
        riley "Hey there, Shinso."
        hitoshi "Hi Riley, did you need something?"
        riley "Nope! Just wanted to sit with you."
        hitoshi "Oh... okay."
        "After that theres a mildly awkward silence."
        riley "So, um, you said you're not in the Hero Course yet, right? What are you in right now?"
        "He makes a face that tells you you might've chosen the wrong topic, but he answers anyway."
        hitoshi "General Studies."
        riley "Wow, so you must be pretty smart then huh?"
        hitoshi "I guess."
        riley "I don't think I could've made it in under normal circumstances honestly. I'm just lucky they accepted my special recommendation."
        "He looks a little shocked at first, then his face turns to a smile."
        hitoshi "It takes a brave person to admit that. I'm impressed."
        riley "Err I think I'm not so much brave as I am a blabbermouth."
        "He chuckles."
        "You pass the rest of lunch with relative little talking, but you feel closer to Shinso nonetheless."
        "Soon lunch ends and it's time for class again."
    else:
        call lunch3hitoshi
return
