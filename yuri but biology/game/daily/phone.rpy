
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


image notifaction:
    "/gui/tile.png"

screen phone_text_noti:
    modal True

    imagebutton:
        xpos 100
        ypos 100
        idle "/gui/back.png"
        at Transform(xzoom = -1.0)

        action [Hide("phone_text_noti"), Show("phone_timezone")]

    #for tiles
    vbox:
        xpos 1000
        ypos 100
        #carni
        imagebutton:
            idle "notifaction"
            action [Hide("phone_text_noti"), Function(choose_text, 0), Show("phone_text")]
        #herbi
        imagebutton:
            idle "notifaction"
            action [Hide("phone_text_noti"), Function(choose_text, 1), Show("phone_text")]
        #plant
        imagebutton:
            idle "notifaction"
            action [Hide("phone_text_noti"), Function(choose_text, 2), Show("phone_text")]
        #fungus
        imagebutton:
            idle "notifaction"
            action [Hide("phone_text_noti"), Function(choose_text, 3), Show("phone_text")]

    # for chibi heads
    vbox:
        xpos 1000
        ypos 100
        #carni
        imagebutton:
            idle "/images/sprites/carnivore_chibi.png" at Transform(zoom=0.2)
            action [Hide("phone_text_noti"), Function(choose_text, 0), Show("phone_text")]
        #herbi
        imagebutton:
            idle "notifaction"
            action [Hide("phone_text_noti"), Function(choose_text, 1), Show("phone_text")]
        #plant
        imagebutton:
            idle "/images/sprites/plant_chibi.png" at Transform(zoom=0.2)
            action [Hide("phone_text_noti"), Function(choose_text, 2), Show("phone_text")]
        #fungus
        imagebutton:
            idle "notifaction"
            action [Hide("phone_text_noti"), Function(choose_text, 3), Show("phone_text")]

    vbox:
        xpos 1075
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

#screen for a given persons text

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



#screen for choosing when to have event

default sch_time_temp = -1
default sch_time = -1
default sch_name = ""
default chosen_time0 = False
default chosen_time1 = False
default chosen_time2 = False

screen phone_timezone:
    modal True

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

        action [SetDict(schedule, sch_time, sch_name)]


    


#screen for choosing which character to have the event with

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
            action [Hide("phone_choose_character"), SetDict(schedule, sch_time, "carnivore"), Jump("phone_end")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_choose_character"), SetDict(schedule, sch_time, "herbivore"), Jump("phone_end")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_choose_character"), SetDict(schedule, sch_time, "plant"), Jump("phone_end")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_choose_character"), SetDict(schedule, sch_time, "fungus"), Jump("phone_end")]

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


#handles phone logic

label phone:

    scene bg_phone

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
        