
default NOTI_HEIGHT = 100

screen phone_text_noti:
    modal True

    vbox:
        xpos 1000
        ypos 100
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, carnivore), Show("phone_text")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, herbivore), Show("phone_text")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, plant), Show("phone_text")]
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Function(choose_text, fungus), Show("phone_text")]

    vbox:
        xpos 1000
        ypos 100
        spacing 61
        #zoom 1 is 100
        text "cow":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "meoe":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "meoe":
            color "#000000" yanchor(0.5) xpos 15 ypos 50
        text "meoe":
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

    show screen phone_text_noti


    window hide
    pause






init python:

    def choose_text(character):
        store.phone_text = "Monka dumbass bitch\n Illsee you in hell\n crazy racist\n dumbass"
        store.height_text = phone_text.count("\n") + 1
        