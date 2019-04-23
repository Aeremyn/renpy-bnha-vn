###################################################
##                                               ##
## Create Custom Transforms                      ##
##                                               ##
###################################################

init:
    transform centerleft:
        xalign 0.25
        yalign 1.0
    transform centerright:
        xalign 0.80
        yalign 1.0
    transform rightoffset:
        xalign 0.95
        yalign 1.0
    transform leftoffset:
        xalign 0.05
        yalign 1.0

###################################################
##                                               ##
## Declare Variables                             ##
##                                               ##
###################################################

# Characters
define riley = Character("Riley", who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/rileylace.png", namebox_background="GUI/rileynamebox.png")
define aizawa = Character("Aizawa", who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/textbox.png", namebox_background="GUI/namebox.png")
define tenya = Character("tenyaName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/bluelace.png", namebox_background="GUI/bluenamebox.png")
define shoto = Character("shotoName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/redlace.png", namebox_background="GUI/rednamebox.png")
define rikido = Character("rikidoName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/textbox.png", namebox_background="GUI/namebox.png")
define ochako = Character("ochakoName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/pinklace.png", namebox_background="GUI/pinknamebox.png")
define izuku = Character("izukuName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/greenlace.png", namebox_background="GUI/greennamebox.png")
define katsuki = Character("katsukiName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/orangelace.png", namebox_background="GUI/orangenamebox.png")
define eijiro = Character("eijiroName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/textbox.png", namebox_background="GUI/namebox.png")
define momo = Character("momoName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/textbox.png", namebox_background="GUI/namebox.png")
define denki = Character("Kaminari", who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/textbox.png", namebox_background="GUI/namebox.png")
define hitoshi = Character("hitoshiName", dynamic=True, who_color = "#ffffff", what_color = "#ffffff", window_background="GUI/textbox.png", namebox_background="GUI/namebox.png")

# Character Names
define tenyaName = "???"
define shotoName = "???"
define ochakoName = "???"
define izukuName = "???"
define katsukiName = "???"
define rikidoName = "???"
define momoName = "???"
define eijiroName = "???"
define hitoshiName = "???"

# Pronouns
define shehethey = "they"
define herhimthem = "them"
define herhistheir = "their"
define hershistheirs = "theirs"
define wantwants = "want"

# Love Points
default izukupoints = 0
default ochakopoints = 0
default shotopoints = 0
default tenyapoints = 0
default katsukipoints = 0
default hitoshipoints = 0

# Lunch Tracker
define ochakoLunchNum = 1
define ochakoLunchString = "%d" % ochakoLunchNum
define shotoLunchNum = 1
define shotoLunchString = "%d" % shotoLunchNum
define katsukiLunchNum = 1
define katsukiLunchString = "%d" % katsukiLunchNum
define tenyaLunchNum = 1
define tenyaLunchString = "%d" % tenyaLunchNum
define izukuLunchNum = 1
define izukuLunchString = "%d" % izukuLunchNum
define hitoshiLunchNum = 1
define hitoshiLunchString = "%d" % hitoshiLunchNum

#Other
define movieChoice = "none"
define beatBakugo = False
define ochakoMall = False

###################################################
##                                               ##
## Game Start and Setup                          ##
##                                               ##
###################################################

label start:

###################################################
##                                               ##
## Call to Labels                                ##
##                                               ##
###################################################

    # call screen test1
    # call beginning #done
    # call feelings #done
    # call introduction #done
    # call seatchoice #done
    # call class1 #done
    # call meetShinso
    # call lunchtime1 #done
    # call introductions #done
    # call class2 #done
    # call afternoon1 #done
    # #icecream #done
    # call bedtime1 #done
    # call day2start #done
    # call lunchtime2 #done
    # call class3 #done
    # call afternoon2 #done
    # call bedtime2 #done
    # call day3start
    # call devtest
## See corresponding .rpy files for details
    # call credits #done
###################################################
##                                               ##
## Game End                                      ##
##                                               ##
###################################################

return
