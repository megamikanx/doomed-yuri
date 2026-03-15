
define all_phone_text = [
    #carnivore
    ["Rise and shine dweeb",
    "Yo did you do the homework, I’m kinda fucked",
    "D",
    ""],
    #herbivore
    ["Good morning [player_name]-kun, can’t wait to meet you today at school smile emoji",
    "Look, [player_name]-kun, a beautiful flower bloomed in our classroom (flower emoji)\nI always take care of it after school~",
    "Excited for tomorrow!",
    ""],
    #plant
    ["Hey [player_name]-kun hows catching up going, I’m done with my work so … m-maybe … I c-can help you if you need… I’m free in the morning if you’d like…(>⩊<)",
    "Have a g-good morning (˵ •̀ ᴗ - ˵ )",
    "Come to school",
    ""],
    #fungus
    ["play this roblox game w me \nfnaf eternal nights",
    "*reel*\nim crine bruh 😭\nlook at this dancing cat\nwhat does it even do",
    "yuh william afton spotted in theaters",
    ""],
]

screen phone_text_noti:
    modal True

    imagebutton:
        xpos 100
        ypos 100
        idle "/gui/back.png"
        at Transform(xzoom = -1.0)

        action [Hide("phone_text_noti"), Show("phone_timezone")]

    vbox:
        xpos 1000
        ypos 100
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, 0), Show("phone_text")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, 1), Show("phone_text")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, 2), Show("phone_text")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, 3), Show("phone_text")]

    vbox:
        xpos 1000
        ypos 100
        spacing 50
        # if no varabiles in first part of strings for dialogue this works
        # day 1 we have no texts so day 0 is day 2
        # if string "[player_name]" then error will occur 
        text " ".join(all_phone_text[0][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text " ".join(all_phone_text[1][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text " ".join(all_phone_text[2][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text " ".join(all_phone_text[3][day - 2].split()[0:2]) + "...":
            color "#000000" yanchor(0.5) xpos 15 ypos 50

default phone_time_temp = 0

screen phone_timezone:
    modal True

    if day != 1:
        imagebutton:
            xpos 100
            ypos 100
            idle "/gui/back.png"

            action [Hide("phone_timezone"), Show("phone_text_noti")]

    vbox:
        xpos 1000
        ypos 100
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_timezone"), SetVariable("phone_time_temp", 0),  Show("phone_choose_character")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_timezone"), SetVariable("phone_time_temp", 1), Show("phone_choose_character")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_timezone"), SetVariable("phone_time_temp", 2), Show("phone_choose_character")]

    vbox:
        xpos 1000
        ypos 100
        spacing 50
        # if no varabiles in first part of strings for dialogue this works
        # if string "[player_name]" then error will occur 
        text "Morining":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "Afternoon":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "After Hours":
            color "#000000" yanchor(0.5) xpos 15 ypos 50

screen phone_choose_character:
    modal True

    imagebutton:
        xpos 100
        ypos 100
        idle "/gui/back.png"

        action [Hide("phone_choose_character"), Show("phone_timezone")]

    vbox:
        xpos 1000
        ypos 100
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_choose_character"), SetDict(schedule, phone_time_temp, "carnivore"), Jump("phone_end")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_choose_character"), SetDict(schedule, phone_time_temp, "herbivore"), Jump("phone_end")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_choose_character"), SetDict(schedule, phone_time_temp, "plant"), Jump("phone_end")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_choose_character"), SetDict(schedule, phone_time_temp, "fungus"), Jump("phone_end")]

    vbox:
        xpos 1000
        ypos 100
        spacing 50
        # if no varabiles in first part of strings for dialogue this works
        # if string "[player_name]" then error will occur 
        text "Carnivore-chan":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "Herbivore-chan":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "Plant-chan":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "Fungus-chan":
            color "#000000" yanchor(0.5) xpos 15 ypos 50


define phone_text = ""
define height_text = 0

screen phone_text:
    modal True

    imagebutton:
        xpos 100
        ypos 100
        idle "/gui/back.png"

        action [Hide("phone_text"), Show("phone_text_noti")]
    
    #compose text of three images bottom image is fixed and top moves based on text length
    # middle is strechted with zoom to make it fit size of text

    image "/gui/top.png" xpos 1000 ypos (800 - (24 + 4)*height_text - 20)
    image "/gui/mid.png":
        anchor(0.0, 1.0)
        xpos 1000 ypos 800
        yzoom ((24 + 4)*height_text / 20)
    image "/gui/bot.png" xpos 1000 ypos 800

    # size is pixel height of text + 4 pixel(atleast for size 24) padding added 

    text phone_text:
        yanchor(1.0) color "#ffffff" xpos 1010 ypos 800 size 24


label phone:

    scene iphone_tempremove:
        align (0.5, 0.5)

    if day == 1:
        show screen phone_timezone
    else:
        show screen phone_text_noti

    window hide
    pause

label phone_end:
    jump plan


init python:

    def choose_text(ch):
        # as two day offset
        store.phone_text = store.all_phone_text[ch][store.day - 2]
        store.height_text = store.phone_text.count("\n") + 1
        