label day2start:
    play music "audio/ill-become-a-hero.mp3" fadeout 2.0 fadein 2.0
    scene bg riley-dorm with fade
    "Morning comes too soon."
    "You wake and groggily head to the bathroom to brush your teeth. When that's done you head down to the communal kitchen."
    "You must be on the late side because it's completely empty except for you. You make yourself some toast and eat on the way to class."
    scene bg classroom-front-view with fade
    "When you arrive you see your classmates all milling about doing various activities."
    "Deku talks animatedly to Todoroki. Iida appears to be studying. Ochako reads a fashion magazine, while Bakugo plays something on his Switch."
    call screen day2morning

    label day2shotoAndizuku:
        $ izukupoints += 1
        $ shotopoints += 1
        show shoto at centerleft
        show izuku at centerright
        with dissolve
        "You hear Deku talking loudly as you approach."
        izuku "He's new to the scene but he's really popular and strong too! I got to see his \"Premptive Binding Lacquered Chain Prison\" in person, it's really something!"
        "Todoroki turns to you as you approach"
        shoto "Good morning, Riley."
        izuku "Oh, hi Riley."
        riley "Hi, don't mind me, go on."
        izuku "Oh, uh I think that's all I had to say about Kamui Woods."
        riley "I'm a fan of Mountain Lady. She's so cool and strong."
        riley "What about you Todoroki? Do you have any favorite heroes?"
        shoto "Ah... me?"
        "He thinks for a moment."
        shoto "...All Might."
        izuku "Well, no one compares to All Might."
        "Aizawa walks in."
        aizawa "Class is starting, take your seats!"
    return

    label day2tenya:
        $ tenyapoints += 1
        show tenya at center
        with dissolve
        "You approach Iida, he seems really absorbed in his studies."
        riley "Hey Iida."
        "He jumps a little in his seat."
        tenya "Hello Riley. Good morning, did you need something?"
        riley "Just wanted to see what you were doing."
        "He shows you his book."
        tenya "Studying. I have a feeling theres going to be a pop quiz today."
        riley "In that case maybe I should study some too."
        "You sit down in the next desk over and pull out your notebook."
        "You open it flip a couple of pages and then remember that it's mostly blank."
        riley "Oh right... Hey Iida would you mind if I copied your notes for the first part of this chapter? I wasn't here yet to take them."
        tenya "Certainly."
        "He hands over his notebook and you open it to the page you need."
        riley "Your handwriting is very nice, Iida."
        "He blushes a little."
        tenya "Thank you."
        "You quickly copy the notes down and return his notebook to him."
        riley "Thanks Iida!"
        "Aizawa walks in."
        aizawa "Class is starting, take your seats!"
    return

    label day2katsuki:
        $ katsukipoints += 1
        show katsuki at center
        with dissolve
        "You walk over to where Bakugo sits, playing his game."
        riley "What'cha playing?"
        if beatBakugo:
            katsuki "Smash obviously. Practicing so next time I can reclaim my title as Champion."
            riley "Ahh so does that make me the current champion?"
            "He scowls at you."
            katsuki "Not for long."
            riley "We'll see. So aside from obsessing about beating me, what have you been up to?"
            katsuki "I'm not obsessing! ...And I've been reading mostly."
            riley "YOU read?"
            "He looks genuinely offended."
            katsuki "Yes I read."
            riley "What kind of books? Horror? Thrillers?"
            katsuki "Tch... nothing you'd be interested in."
            "Aizawa walks in."
            aizawa "Class is starting, take your seats!"
        else:
            katsuki "Smash. Practicing so I can retain my title as Champion."
            riley "I see... So aside from obsessing over a video game, what have you been up to?"
            katsuki "I'm not obsessing! ...And I've been reading mostly."
            riley "YOU read?"
            "He looks genuinely offended."
            katsuki "Yes I read."
            riley "What kind of books? Horror? Thrillers?"
            katsuki "Tch... nothing you'd be interested in."
            "Aizawa walks in."
            aizawa "Class is starting, take your seats!"
    return

    label day2ochako:
        $ ochakopoints += 1
        show ochako at center
        with dissolve
        "You sit down in the desk next to Ochako's"
        ochako "Hey Riley. You into fashion at all?"
        riley "A little."
        ochako "What do you think of this?"
        "She hands you the magazine and points to a celebrity wearing some designer outfit."
        riley "It's... nice?"
        ochako "Haha, very insightful Riley."
        riley "I'm guesss not very fashionable after all."
        ochako "I'm sure you dress fine. The latest fashions aren't for everyone anyway."
        "She smiles at you."
        ochako "If you ever needs any tips though, I'm your girl!"
        "Aizawa walks in."
        aizawa "Class is starting, take your seats!"
    return
return
