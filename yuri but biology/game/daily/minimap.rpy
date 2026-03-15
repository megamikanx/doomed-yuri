

# screen with transparent buttons overlaying background of map
screen map:
    modal True


    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 100 ypos 100
        at Transform(rotate= -15)
        action [Hide("map"), Function(call_event, "plant")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 800 ypos 800
        at Transform(rotate= -15)
        action [Hide("map"), Function(call_event, "fungus")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 800 ypos 100
        at Transform(rotate= 15)
        action [Hide("map"), Function(call_event, "herbivore")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 800 ypos 100
        at Transform(rotate= 15)
        action [Hide("map"), Function(call_event, "carnivore")]


label map:

    camera:
        perspective True # allows for rotation though not needed

    show screen map

    # makes only map input work
    window hide
    pause

    
init python:

    def call_event(character):
        # timeslots includes dawn where as index starts at morning
        #get number of times this event has been called, and increases tally
        version = freetime_index[character+"_"+timeslots[curr_timeslot_idx + 1]]
        freetime_index[character+"_"+timeslots[curr_timeslot_idx + 1]] =+ 1

        #currently crashes the game as some labels dont exist
        #renpy.jump(character+"_"+timeslots[curr_timeslot_idx + 1]+str(version))
        renpy.jump(start)
