
define all_phone_text = [
    #carnivore
    ["Rise and shine dweeb",
    "Yo did you do the\nhomework, I’m kinda fucked",
    "D",
    ""],
    #herbivore
    ["Good morning [player]-kun, can’t\nwait to meet you today at\nschool smile emoji",
    "Look, [player]-kun, a beautiful\nflower bloomed in our\nclassroom (flower emoji)\nI always take care of it after\nschool~",
    "Excited for tomorrow!",
    ""],
    #plant
    ["Hey [player]-kun hows catching\nup going, I’m done with my\nwork so … m-maybe … I c-can\nhelp you if you need… I’m free\nin the morning if you’d like…\n(>⩊<)",
    "Have a g-good morning\n(˵ •̀ ᴗ - ˵ )",
    "Come to school",
    ""],
    #fungus
    ["play this roblox game w me \nfnaf eternal nights",
    "*reel*\nim crine bruh 😭\nlook at this dancing cat\nwhat does it even do",
    "yuh william afton spotted\nin theaters",
    ""],
]


<<<<<<< HEAD
=======
screen click_sfx:
    # left mouse button release
    key "mouseup_1" action Play("sound", "audio/click.ogg")

image notifaction:
    "/gui/tile.png"

>>>>>>> 94a054780c8ebf7323ea3b139448f724d8da3044
screen phone_text_noti:
    modal True

    image "/images/backgrounds/bg_phone_texts.png"

    imagebutton:
        xpos 100
        ypos 100
        idle "/gui/back.png"
        at Transform(xzoom = -1.0)

        action [Hide("phone_text_noti"), Show("phone_timezone")]

    imagebutton:
        idle "/gui/text_notfication_transparent.png"
        hover "/gui/text_notfication_black.png"
        xpos 743 ypos 14
        at Transform(rotate=3, alpha=0.25)
        action [Hide("phone_text_noti"), Function(choose_text, 0), Show("phone_text")]
    imagebutton:
        idle "/gui/text_notfication_transparent.png"
        hover "/gui/text_notfication_black.png"
        xpos 736 ypos 126
        at Transform(rotate=3, alpha=0.25)
        action [Hide("phone_text_noti"), Function(choose_text, 2), Show("phone_text")]
    imagebutton:
        idle "/gui/text_notfication_transparent.png"
        hover "/gui/text_notfication_black.png"
        xpos 729 ypos 238
        at Transform(rotate=3, alpha=0.25)
        action [Hide("phone_text_noti"), Function(choose_text, 3), Show("phone_text")]
    imagebutton:
        idle "/gui/text_notfication_transparent.png"
        hover "/gui/text_notfication_black.png"
        xpos 722 ypos 350
        at Transform(rotate=3, alpha=0.25)
        action [Hide("phone_text_noti"), Function(choose_text, 1), Show("phone_text")]


    vbox:
        xpos 770
        ypos 190
        spacing 65
        at Transform(rotate=3)
        # if no varabiles in first part of strings for dialogue this works
        # day 1 we have no texts so day 0 is day 2
        # if string "[player_name]" then error will occur 
        text " ".join(all_phone_text[0][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text " ".join(all_phone_text[2][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text " ".join(all_phone_text[3][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text " ".join(all_phone_text[1][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50

#screen for a given persons text

define phone_text = ""
define height_text = 0
define who_texted = -1

screen phone_text:
    modal True

    image "/images/backgrounds/messages"+str(who_texted)+".png"

    imagebutton:
        xpos 100
        ypos 100
        idle "/gui/back.png"

        action [Hide("phone_text"), Show("phone_text_noti")]
    
    #compose text of three images bottom image is fixed and top moves based on text length
    # middle is strechted with zoom to make it fit size of text

    image "/gui/text_bub_bot.png"
    image "/gui/text_bub_top.png":
        anchor(0.5, 0.435)
        pos(960, 475)
        yzoom ((24 + 4)*(height_text / 70 + 0.01))

    # size is pixel height of text + 4 pixel(atleast for size 24) padding added 

    text phone_text:
        yanchor(0.0) color "#000000" xpos 830 ypos 490 size 24



#screen for choosing when to have event

default sch_time_temp = -1
default sch_time = -1
default sch_name = ""
default chosen_time0 = False
default chosen_time1 = False
default chosen_time2 = False

screen phone_timezone:
    modal True
    image "/images/backgrounds/bg_phone.png"

    if day != 1:
        imagebutton:
            xpos 100
            ypos 100
            idle "/gui/back.png"

            action [Hide("phone_timezone"), Show("phone_text_noti")]

    imagebutton:
        idle "/gui/schedule_transparent_tile.png" at Transform(anchor=(0,0), pos= (723,43), rotate=3)
        action [SetVariable("sch_time_temp", 0), SetVariable("chosen_time0", True), SetVariable("chosen_time1", False), SetVariable("chosen_time2", False)]
    imagebutton:
        idle "/gui/schedule_transparent_tile.png" at Transform(anchor=(0,0), pos= (712,270), rotate=3)
        action [SetVariable("sch_time_temp", 1), SetVariable("chosen_time1", True), SetVariable("chosen_time0", False), SetVariable("chosen_time2", False)]
    imagebutton:
        idle "/gui/schedule_transparent_tile.png" at Transform(anchor=(0,0), pos= (700,510), rotate=3)
        action [SetVariable("sch_time_temp", 2), SetVariable("chosen_time2", True), SetVariable("chosen_time0", False), SetVariable("chosen_time1", False)]

    if sch_name == "carnivore":
        image "/gui/carni_schedule_icon.png" at Transform(anchor=(0,0), pos= (730 + 5*sch_time, 105 + 225*sch_time), rotate=3)
    if sch_name == "plant":
        image "/gui/plant_schedule_icon.png" at Transform(anchor=(0,0), pos= (730 + 5*sch_time,105 + 225*sch_time), rotate=3)
    
    if sch_name == "fungus":
        image "/gui/fungus_schedule_icon.png" at Transform(anchor=(0,0), pos= (730 + 5*sch_time,105 + 225*sch_time), rotate=3)
    if sch_name == "herbivore":
        image "/gui/herbivore_schedule_icon.png" at Transform(anchor=(0,0), pos= (730 + 5*sch_time,105 + 225*sch_time), rotate=3)




    #first row
    if chosen_time0:
        image "/gui/icon_select.png":
            anchor(0, 0) xpos 1050 ypos 55 rotate 3
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1050, 257), rotate=3)
            action [SetVariable("sch_name", "carnivore"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time0", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1193, 265), rotate=3)
            action [SetVariable("sch_name", "plant"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time0", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1335, 272), rotate=3)
            action [SetVariable("sch_name", "fungus"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time0", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1477, 280), rotate=3)
            action [SetVariable("sch_name", "herbivore"),  SetVariable("sch_time", sch_time_temp),SetVariable("chosen_time0", False)]
    
    #secound row
    if chosen_time1:
        image "/gui/icon_select.png":
            anchor(0, 0) xpos 1050 ypos 285 rotate 3
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1050, 487), rotate=3)
            action [SetVariable("sch_name", "carnivore"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time1", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1193, 495), rotate=3)
            action [SetVariable("sch_name", "plant"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time1", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1335, 502), rotate=3)
            action [SetVariable("sch_name", "fungus"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time1", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1477, 510), rotate=3)
            action [SetVariable("sch_name", "herbivore"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time1", False)]
    
    if chosen_time2:
        image "/gui/icon_select.png":
            anchor(0, 0) xpos 1050 ypos 515 rotate 3
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1050, 717), rotate=3)
            action [SetVariable("sch_name", "carnivore"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time2", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1193, 725), rotate=3)
            action [SetVariable("sch_name", "plant"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time2", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1335, 735), rotate=3)
            action [SetVariable("sch_name", "fungus"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time2", False)]
        imagebutton:
            idle "/gui/icon_select_transparent.png" at Transform(anchor=(0,0), pos= (1477, 745), rotate=3)
            action [SetVariable("sch_name", "herbivore"), SetVariable("sch_time", sch_time_temp), SetVariable("chosen_time2", False)]

    

    imagebutton:
        xpos 100
        ypos 800
        idle "/gui/back.png"

        action [Hide("phone_timezone"), Function(start_day), Jump("plan")]


#handles phone logic

label phone:

    scene bg_black

    if day == 1:
        show screen phone_timezone
    else:
        show screen phone_text_noti

    window hide
    
    pause


init python:

    def choose_text(ch):
        # as two day offset
        store.who_texted = ch
        store.phone_text = store.all_phone_text[ch][store.day - 2]
        store.height_text = store.phone_text.count("\n") + 1

    def start_day():
        store.schedule[store.sch_time]= store.sch_name
        store.sch_time = -1
        store.sch_name = ""
        store.sch_time_temp = -1

        