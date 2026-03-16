

# dont need if this label is needed could be conslidated

label plan:
    "accessed plan"
    $ go_next()

    pause


init python:

    def go_next():
        store.curr_timeslot_idx += 1

        if store.curr_timeslot_idx == 3:
            store.day += 1
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
        

