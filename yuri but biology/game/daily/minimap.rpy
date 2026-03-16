

# screen with transparent buttons overlaying background of map
screen map:
    modal True

    if store.curr_timeslot_idx == 0:
        image "/images/timers/morning"+str(day)+".png":
            align(0.5, 0.5)
    if store.curr_timeslot_idx == 1:
        image "/images/timers/afternoon"+str(day)+".png":
            align(0.5, 0.5)
    if store.curr_timeslot_idx == 2:
        image "/images/timers/afterhours"+str(day)+".png":
            align(0.5, 0.5)


    imagebutton:
        idle "/gui/map_transparent_tile_lib.png"
        hover "/gui/map_transparent_tile_lib_black.png"
        anchor(0.5,0.5)
        xpos 650 ypos 460
        at Transform(rotate= -28, alpha=0.25)
        action [Hide("map"), Function(call_event, "plant", "library")]

    imagebutton:
        idle "/gui/map_transparent_tile_class.png"
        hover "/gui/map_transparent_tile_class_black.png"
        anchor(0.5,0.5)
        xpos 1160 ypos 440
        at Transform(rotate= 29, alpha=0.25)
        action [Hide("map"), Function(call_event, "herbivore", "classroom")]

    imagebutton:
        idle "/gui/map_transparent_tile_cafe.png"
        hover "/gui/map_transparent_tile_cafe_black.png"
        anchor(0.5,0.5)
        xpos 650 ypos 775
        at Transform(rotate= 29, alpha=0.25)
        action [Hide("map"), Function(call_event, "carnivore", "cafeteria")]

    imagebutton:
        idle "/gui/map_transparent_tile_court.png"
        hover "/gui/map_transparent_tile_court_black.png"
        anchor(0.5,0.5)
        xpos 1150 ypos 800
        at Transform(rotate= -28, alpha=0.25)
        action [Hide("map"), Function(call_event, "fungus", "courtyard")]


label map:

    scene bg_map:
        anchor(0.5,0.5) pos(960,510) zoom 0.85

    #creates buttons for map
    show screen map

    # makes only map input work
    window hide
    pause

    
init python:

    version = -1

    def call_event(character, location):
        
        # check that 
        if character == last_freetime_girl:
            renpy.show_screen("map")
            renpy.transition(hpunch)
            return
        # gets conversation level
        # timeslots includes dawn where as index starts at morning
        #get number of times this event has been called, and increases tally
        version = freetime_index[character]

        # if fungus also there let player choose to go to her
        if where_fungus[day - 1] == location and not met_fungus:
            renpy.jump("free_"+character+"_fungushere")
        
        #if fungus not in courtyard and choose courtyard
        if where_fungus[day - 1] and character == "fungus":
            renpy.jump("free_fungus_nothere")

        freetime_index[character] += 1

        # jump to event
        #may crash the game as some labels dont exist
        store.last_freetime_girl = character
        renpy.jump("free_"+character+str(version))
        

