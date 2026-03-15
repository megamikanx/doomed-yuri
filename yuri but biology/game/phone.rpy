
default NOTI_HEIGHT = 100

screen phone_text_noti:
    modal True

    vbox:
        xpos 1000
        ypos 100
        imagebutton:
            idle "/gui/tile.png"
            action [Hide("phone_text_noti"), Show("phone_text")]
        imagebutton:
            idle "/gui/tile.png"
        imagebutton:
            idle "/gui/tile.png"
        imagebutton:
            idle "/gui/tile.png"

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


screen phone_text:
    modal True

    imagebutton:
        xpos 100
        ypos 100
        idle "/gui/back.png"

        action [Hide("phone_text"), Show("phone_text_noti")]
    
    #compose text of three images bottom image is fixed and top moves based on text length
    # middle is strechted with zoom to make it fit size of text
    




label phone:

    scene iphone_tempremove:
        align (0.5, 0.5)

    show screen phone_text_noti


    window hide
    pause


