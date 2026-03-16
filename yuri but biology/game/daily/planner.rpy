

# dont need if this label is needed could be conslidated

label plan:
    $ go_next()

    pause

screen click_sfx:
    # left mouse button release
    key "mouseup_1" action Play("sound", "audio/click.ogg")

init python:

    def go_next():
        store.curr_timeslot_idx += 1

        if store.curr_timeslot_idx == 3:
            store.day += 1
            if are_you_bitchless():
                return

            if store.day == 6:
                end_game()
                return

            store.curr_timeslot_idx = -1
            store.schedule = ["","",""]
            store.meet_fungus = False
            store.last_freetime_girl = None
            renpy.jump("phone")


        # if scheduled an event jump to it
        if schedule[store.curr_timeslot_idx]:
            # this has not delay to it making it feel jawing
            renpy.jump("event_"+schedule[store.curr_timeslot_idx]+str(day)) # call anyevent on any day issue
            
            print("infinte test make sure this is not seen")
            return
        
        #otherwise choose from map
        renpy.jump("map")

    def are_you_bitchless():
        all_affection = [carnivore_affection, herbivore_affection, plant_affection, fungus_affection]
        # need to be filled
        return False
        

    def end_game_natural():
        all_affection = [carnivore_affection, herbivore_affection, plant_affection, fungus_affection]
        
        #if max and min affection levels are too different get respective ending
        if (max(all_affection) - min(all_affection)) > MAX_AFFECTION_DIFF:
            renpy.jump("world_end_ending")
        else:
            renpy.jump("good_ending")
        
        

