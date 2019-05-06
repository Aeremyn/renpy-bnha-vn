label afternoon1:
    "You head to your room."
    scene bg riley-dorm with fade
    "You find everything in order and only have to unpack a box of personal items you brought from home."
    "After you finish unpacking you hear a knock at your door."
    "You open it and Deku is standing there looking a little nervous."
    show izuku at center with dissolve
    izuku "Hey Riley, I just wanted to check to make sure you're settled in okay."
    riley "Yup, all good!"
    izuku "Good! I also wanted to know if you wanted to go to the movies?"
    riley "Uhm..."
    "He turns red and waves his hands in front of his face."
    izuku "I don't mean with just me, some of our classmates are going too!"
    riley "Oh okay, in that case..."
    menu:
        "Sure, I'll go!":
            izuku "Okay, great!"
            "He looks down at your clothes."
            izuku "Oh, you still haven't changed. Well, meet us down in the common room when you're ready and we'll head out!"
            riley "Okay, see you in a few."
            hide izuku with dissolve
            "He turns to go and you close your door behind him."
            "You quickly change clothes and head down to the common room."
            scene bg common-room with fade
            "You find Ochako, Iida, and Deku waiting for you."
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Glad you decided to join us Riley!"
            tenya "Yes, making time for relaxing is just as important as making time for studying!"
            izuku "Should we head out?"
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            "You walk though the city following your classmates' lead."
            ochako "So Riley, you come from America right? Are you used to the city?"
            riley "I grew up in suburbs in America, but I've been to the city before."
            ochako "I see, what city did you go to? New York, Hollywood, Chicago?"
            riley "Oh nowhere like that..."
            "Before you can continue, you round the corner and come upon the movie theatre."
            izuku "What should we watch?"
            tenya "I would like to watch that new historical drama."
            ochako "Boooooring, let's watch a horror movie!"
            izuku "I don't like horror movies very much, maybe an action movie instead?"
            izuku "What do you think Riley?"
            menu:
                "Historical drama sounds best.":
                    $ movieChoice = "historicalDrama"
                    $ tenyapoints += 1
                    "Iida looks happy."
                    scene bg cinema with fade
                    "You all make your way inside the theatre and shuffle into your seats."
                    menu:
                        "Sit with Ochako.":
                            call afternoon1moviesOchako
                        "Sit with Deku.":
                            call afternoon1moviesIzuku
                        "Sit with Iida.":
                            call afternoon1moviesTenya
                "Horror movie, all the way!":
                    $ movieChoice = "horror"
                    $ ochakopoints += 1
                    "Ochako looks happy."
                    scene bg cinema with fade
                    "You all make your way inside the theatre and shuffle into your seats."
                    menu:
                        "Sit with Ochako.":
                            call afternoon1moviesOchako
                        "Sit with Deku.":
                            call afternoon1moviesIzuku
                        "Sit with Iida.":
                            call afternoon1moviesTenya
                "An action movie sounds fun.":
                    $ movieChoice = "action"
                    $ izukupoints += 1
                    "Deku looks happy."
                    scene bg cinema with fade
                    "You all make your way inside the theatre and shuffle into your seats."
                    menu:
                        "Sit with Ochako.":
                            call afternoon1moviesOchako
                        "Sit with Deku.":
                            call afternoon1moviesIzuku
                        "Sit with Iida.":
                            call afternoon1moviesTenya
        "No thanks, maybe next time.":
            izuku "Oh, okay, no problem. See you later!"
            hide izuku with dissolve
            "You close the door, lay down on your bed, and immediately fall asleep."
            "You wake up about an hour later."
            menu:
                "Go to the Common Room.":
                    scene bg common-room with fade
                    "As you enter the room you notice some of your other classmates."
                    "Todoroki sits alone on a couch, reading. Meanwhile Bakugo, Kirishima, and Kaminari loudly play a videogame."
                    menu:
                        "Play games with Bakugo and friends.":
                            call afternoon1CommonRoomKatsuki
                        "Read with Todoroki.":
                            call afternoon1CommonRoomShoto
                "Get some extra training in.":
                    $ hitoshipoints += 1
                    scene bg training-grounds with fade
                    "As you approach you see a lone figure standing in the middle of the training grounds."
                    "The figure faces away from you but you'd recognize that indigo hair anywhere."
                    riley "Shinso!"
                    show hitoshi with dissolve
                    "He turns around and you wave excitedly and trot over."
                    riley "I didn't expect to see you here, what are you up to?"
                    "He smirks."
                    hitoshi "Um, training?"
                    "You put your hands on your hips and huff."
                    riley "I know that smartass. What {i}kind{/i} of training?"
                    hitoshi "I'm training with a capture weapon similar to Aizawa-sensei's"
                    riley "Ohh, I thought your scarf looked familiar!"
                    hitoshi "It's not exactly a scarf..."
                    riley "Whatever! Show me what you can do with it!"
                    hitoshi "O-okay..."
                    "He turns back towards the direction he was facing when you arrived."
                    "In front of him he has several cans and bottles set up at varying heights."
                    "You note that it reminds you of a carnival game but don't say so, instead you remind dead silent so Shinso can focus."
                    "After a moment of concentration, Shinso suddenly lashes out with his weapon at the first target, but instead of grabbing the can he merely knocks it over."
                    hitoshi "Tch..."
                    "He tries again going after the next target, and again he simply knocks it over."
                    show hitoshi with hpunch
                    hitoshi "Ugh! I'm never going to get this!"
                    "His eyes are fixed to the floor in front of him. There's a mix of emotions on his face, but most of all he looks... ashamed."
                    "You slowly walk over to him and put a hand on his shoulder."
                    "His head snaps up to look at you."
                    riley "Hey-"
                    hitoshi "If you're going to make fun of me, just do it already."
                    riley "I'm not gonna make fun of you."
                    "You try your best to put on a soft, disarming smile."
                    riley "Look how long have you been at this?"
                    hitoshi "Weeks."
                    riley "Right, I heard it took Aizawa years to master his weapon."
                    "He looks down at the floor again."
                    riley "Hey, give it another go."
                    hitoshi "What's the point?"
                    riley "Please? They say third time's the charm!"
                    "He sighs deeply, but begins to focus once more."
                    "He throws his weapon and... actually grabs the can!"
                    "His eyes go wide and he quickly pulls his weapon back, bringing the can toward himself."
                    "There's a huge smile on his face."
                    hitoshi "I did it! I actually did it!"
                    riley "Great job! That was awesome!"
                    "He remembers you're there and composes himself. Then clears his throat."
                    hitoshi "Uhh, thanks for the encouragement Riley."
                    "You smile at him."
                    riley "-you couldn't have done it without me?"
                    hitoshi "I wouldn't go {i}that{/i} far."
                    "You chuckle half at your own joke and half at the other's pride."
                    hitoshi "Well I think I'm about done for today..."
                    riley "Okay, well I haven't even started so I guess it's bye for now."
                    hitoshi "Yeah, bye."
                    "He turns to walk away, then stops and looks over his shoulder."
                    hitoshi  "And... thanks."
                    "You smile at him and give a thumbs up and he turns and goes without stopping again."
                    "You turn to your own task."
                    "After about two hours you finally decide to call it a night and return to the dorms to shower and sleep."



    label afternoon1moviesOchako:
        show ochako at center with dissolve
        $ ochakopoints += 1
        if movieChoice == "horror":
            ochako "So you like horror movies too Riley? We'll have to have a movie night sometime!"
            riley "Yeah, that sounds great!."
            "The movie starts and Ochako is held captivated by the scenes of bloodshed and screaming."
            "You look over at the other two. Iida looks mildly nervous, but Deku looks terrified."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
        elif movieChoice == "historicalDrama":
            ochako "So how are you liking U.A. so far Riley?"
            riley "It's been interesting so far. That training exercise was really tough."
            ochako "That's Aizawa for you, you should've seen, on the first day-"
            tenya "Shh! It's starting!"
            "Ochako looked rather bored through the whole movie, but at least she seemed to enjoy your company."
            "You look over at the other two. Iida seems to be enjoying himself, but Deku looks a little lost."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
        else:
            ochako "So how are you liking U.A. so far Riley?"
            riley "It's been interesting so far. That training exercise was really tough."
            ochako "That's Aizawa for you, you should've seen, on the first day-"
            izuku "Shh! It's starting!"
            "Ochako looked rather bored through the whole movie, but at least she seemed to enjoy your company."
            "You look over at the other two. Deku seems to be really enjoying himself, but Iida looks a little disappointed."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
    return

    label afternoon1moviesIzuku:
        show izuku at center with dissolve
        $ izukupoints += 1
        if movieChoice == "action":
            izuku "The heroes in action movies are so cool don't you think Riley? Of course none of them are as amazing as All Might."
            riley "Yeah, I can't wait to meet All Might myself."
            "The movie starts and Deku gets wrapped up in the excitement. He even throws his hands up and cheers when the heroes save the day."
            "You look over at the other two. Iida looks disappointed, and Ochako looks bored."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
        elif movieChoice == "horror":
            izuku "So you like horror movies Riley?"
            riley "Yeah, they're great."
            izuku "I see..."
            riley "What's wrong? Do they scare you?"
            izuku "A-a little."
            menu:
                "Reassure him.":
                    riley "Don't worry I hear this one isn't too scary. Next time we'll watch something else, okay?"
                    izuku "O-okay."
                    "The movie starts and Ochako shushes you."
                "Offer to hold his hand.":
                    riley "I can hold your hand if you're too scared."
                    "He blushes at first, then looks mad."
                    izuku "It's not nice to tease people Riley."
                    "Before you can object, the movie starts and Ochako shushes you."
            "Deku looks terrified the whole time."
            "You look over at the other two. Ochako seems to be enjoying herself, but Iida looks a little nervous."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
        else:
            izuku "So how are you liking U.A. so far Riley?"
            riley "It's amazing! Is it true All Might is a teacher there?"
            izuku "Yeah, he's so cool too! I can't wait for-"
            tenya "Shh! It's starting!"
            "Deku looks a little lost in all the courtly intrigue."
            "You look over at the other two. Iida seems to be enjoying himself, but Ochako looks bored."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
    return

    label afternoon1moviesTenya:
        show tenya at center with dissolve
        $ tenyapoints += 1
        if movieChoice == "historicalDrama":
            tenya "I have read this film is as educational as it is entertaining. I hope the critics are correct."
            riley "I hope so too."
            "The movie starts and Iida is engrossed by the courtly manners and political intrigue."
            "You look over at the other two. Ochako looks bored, and Deku looks a little lost."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
        elif movieChoice == "horror":
            tenya "So Riley, are you enjoying your time at U.A.?"
            riley "Yeah it's great. The training was brutal, but I guess that's the only way we'll learn."
            tenya "I agree, the teacher's methods are sometimes harsh but-"
            ochako "Shh! It's starting!"
            "The movie starts and Iida looks a little nervous."
            "You look over at the other two. Ochako seems to be enjoying herself, but Deku looks terrified."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
        else:
            tenya "So Riley, are you enjoying your time at U.A.?"
            riley "Yeah it's great. The training was brutal, but I guess that's the only way we'll learn."
            tenya "I agree, the teacher's methods are sometimes harsh but-"
            izuku "Shh! It's starting!"
            "The movie starts and Iida looks a little disappointed."
            "You look over at the other two. Deku seems to be enjoying himself, but Ochako looks bored."
            "The movie ends and you all make your way out of the theatre."
            scene bg city with fade
            show ochako at leftoffset
            show tenya at rightoffset
            show izuku at center
            with dissolve
            ochako "Ohh! We should all go get ice cream!"
            tenya "No! It's getting late we should return to the dorms and go to sleep!"
            ochako "Ugh, you're being so boring today!"
            tenya "And you're being irresponsible!"
            izuku "Don't fight you two!"
            ochako "..."
            tenya "..."
            izuku "I know, why don't we ask Riley what [shehethey] [wantwants] to do?"
            ochako "What do you think Riley, going for some ice cream can't hurt, right?"
            tenya "Surely Riley will see reason and choose to return home."
            menu:
                "Go get ice cream.":
                    $ ochakopoints += 1
                    tenya "Hmm, I suppose it can't hurt to stay out late just this once..."
                    call icecream
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
                "Return to the dorms.":
                    $ tenyapoints += 1
                    ochako "Aww, okay if Riley thinks that's best maybe Iida is right..."
                    "You all head home."
                    "Once you get to the common room you all tell each other good night and head in seperate directions."
    return

    label afternoon1CommonRoomKatsuki:
        $ katsukipoints += 1
        $ beatBakugo = True
        "You plop down on the floor next to Bakugo."
        katsuki "What do YOU want?"
        denki "Hey Riley, come to join in our epic battle to defeat the champion, Bakugo?"
        eijiro "Yeah, Riley join us!"
        riley "Sure, sounds fun."
        denki "Okay, be careful, Bakugo is a beast!"
        "Luckily for you, you're VERY familiar with this game."
        menu:
            "Go easy on 'em.":
                "You hold back a bit and to your surprise you find that Bakugo is actually winning."
                "You try your best to recover, but it's far too late. You come in second place."
                "Bakugo smiles smugly at you."
            "Show no mercy!":
                "You go all out and thrash all of them, even the so called champion Bakugo."
                "They all turn to you, stunned, and you give them your most innocent smile."
                "Bakugo looks annoyed, but doesn't say anything."
        riley "Best two out of three?"
        katsuki "You're on!"
        "You then proceed to soundly defeat them all for the next two rounds."
        katsuki "Best of ten!"
        riley "Sure, let's go!"
        "You continue on that way for hours, until finally Bakugo declares:"
        katsuki "I'M DONE WITH THIS STUPID GAME!"
        "He throws the controller down in a fit of rage."
        eijiro "Hey Bakugo don't get so worked up, it's just a game."
        katsuki "Tch... whatever. Thanks for playing with us, I guess."
        "He storms away, but he seemed to enjoy the challenge you posed at least."
        "You bid the other two good night and return to your room."
    return

    label afternoon1CommonRoomShoto:
        $ shotopoints += 1
        $ todorokiBook = True
        "You sit down on the couch next to Todoroki."
        riley "What'cha reading?"
        "He starts, only just noticing your presence."
        shoto "\"The Hound and the Falcon\", a friend recommended it."
        riley "Hmm, never heard of that one. What's it about?"
        shoto "I'm not sure yet, but I know it's historical fiction."
        riley "Sounds interesting, can I borrow it when you're done?"
        "He looks at you appraisingly, then nods."
        "You rummage through your bag and pull out your own book."
        riley "This is my favorite it's about... well, actually it's better if you read it."
        riley "When you're done with that book we can trade."
        shoto "Sure."
        riley "Anyway, don't let me bother you any longer. Go ahead and continue your book."
        shoto "You weren't a bother, but thanks."
        "He opens his book back up to the page he marked and continues reading."
        "You crack open your book and do the same."
        "You both sit, reading in silence (other than the occasional ruckus caused by Bakugo and company) for a few hours. Until Todoroki marks his page and closes his book."
        shoto "I'm going to head to bed. Good night Riley."
        "Theres a hint of a smile on his lips."
        riley "Good night Todoroki."
        "He turns to go and quickly disappears up the stairs leaving you alone with your book."
        "You soon decide to return to your room too."
    return

return
