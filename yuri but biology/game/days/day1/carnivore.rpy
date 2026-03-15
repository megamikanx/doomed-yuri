
label free_carnivore_fungushere:
    scene bg_cafeteria

    "Both [carnivore] and [fungus] are here. Who do you want to talk to?"
    menu:
        "Both [carnivore] and [fungus] are here. Who do you want to talk to?{fast}"
        "[carnivore]":
            $ freetime_index["carnivore"+"_"+timeslots[store.curr_timeslot_idx + 1]] += 1
            $ renpy.jump("free_carnivore"+ str(freetime_index["carnivore"+"_"+timeslots[store.curr_timeslot_idx + 1]] - 1))

        "[fungus]":
            $ freetime_index["fungus"+"_"+timeslots[store.curr_timeslot_idx + 1]] += 1
            $ renpy.jump("free_fungus"+str(freetime_index["fungus"+"_"+timeslots[store.curr_timeslot_idx + 1]] - 1))


label free_carnivore0:

    carnivore "0"
    jump plan


label free_carnivore1:

    carnivore "1"
    jump plan

label free_carnivore2:

    carnivore "2"
    jump plan

label free_carnivore3:

    carnivore "3"
    jump plan