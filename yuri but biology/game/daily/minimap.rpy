

# screen with transparent buttons overlaying background of map
screen map:
    modal True


    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 100 ypos 100
        at Transform(rotate= -15)
        action [Hide("map"), Jump("intro")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 800 ypos 800
        at Transform(rotate= -15)
        action [Hide("map"), Jump("intro")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 800 ypos 100
        at Transform(rotate= 15)
        action [Hide("map"), Jump("intro")]


label map:

    camera:
        perspective True # allows for rotation though not needed

    show screen map

    # makes only map input work
    window hide
    pause

    
