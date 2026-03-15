

# screen with transparent buttons overlaying background of map
screen map:
    modal True


    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 100 ypos 100
        at Transform(rotate= -15)
        action [Hide("map"), Function(call_event, "plant", "library")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 800 ypos 800
        at Transform(rotate= -15)
        action [Hide("map"), Function(call_event, "fungus", "courtyard")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 800 ypos 100
        at Transform(rotate= 15)
        action [Hide("map"), Function(call_event, "herbivore","classroom")]

    imagebutton:
        idle "/gui/player.png" # placeholder transparent image
        hover "/gui/tile.png"
        xpos 100 ypos 800
        at Transform(rotate= 15)
        action [Hide("map"), Function(call_event, "carnivore", "cafeteria")]


label map:

    scene bg_static

    #creates buttons for map
    show screen map

    # makes only map input work
    window hide
    pause

    
init python:

    version = -1

    def call_event(character, location):
        # gets conversation level

        # timeslots includes dawn where as index starts at morning
        #get number of times this event has been called, and increases tally
        version = freetime_index[character+"_"+timeslots[store.curr_timeslot_idx + 1]]

        # if fungus also there let player choose to go to her
        if where_fungus[day - 1] == location:
            renpy.jump("free_"+character+"_fungushere")
        
        if where_fungus[day - 1] and character == "fungus":
            renpy.jump("free_fungus_nothere")

        freetime_index[character+"_"+timeslots[store.curr_timeslot_idx + 1]] += 1

        # jump to event
        #may crash the game as some labels dont exist
        renpy.jump("free_"+character+str(version))
        

