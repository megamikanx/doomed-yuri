

# dont need if this label is needed could be conslidated

label plan:
    $ go_next()

    pause


init python:

    def go_next():
        if schedule[curr_timeslot_idx]:
            renpy.jump("event_"+schedule[curr_timeslot_idx]) # call anyevent on any day issue
            print("infinte test make sure this is not seen")
            return
        
        renpy.jump("map")
        

