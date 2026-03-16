
label free_plant_fungushere:
    scene bg_library

    "Both [plant] and [fungus] are here. Who do you want to talk to?"
    menu:
        "Both [plant] and [fungus] are here. Who do you want to talk to?{fast}"
        "[plant]":
            $ store.last_freetime_girl = "plant"
            $ freetime_index["plant"+"_"+timeslots[store.curr_timeslot_idx + 1]] += 1
            $ renpy.jump("free_plant"+ str(freetime_index["plant"+"_"+timeslots[store.curr_timeslot_idx + 1]] - 1))

        "[fungus]":
            $ meet_fungus = True
            $ store.last_freetime_girl = "fungus"
            $ freetime_index["fungus"+"_"+timeslots[store.curr_timeslot_idx + 1]] += 1
            $ renpy.jump("free_fungus"+str(freetime_index["fungus"+"_"+timeslots[store.curr_timeslot_idx + 1]] - 1))

    
    jump plan


label free_plant0:
    scene bg_library

    plant "{size=124}a-aah"
    if curr_timeslot_idx == 0:
        plant "{cps=15}G-G-Go{/cps}od Morning,{w=0.25} {cps=15}s-so{/cps}rry I didn’t see you there"
    else:
        plant "Hello {cps=10}s-so{/cps}rry I didn’t see you there"
    
    plant "Have you come to study too?"
    menu:
        plant "Have you come to study too?{fast}"

        "Yeah i’m looking for a book":
            plant "{cps=7}o-o-o{/cps}h{w=1}, I hope you find it then..."
            jump plan

        "Yeah can you help me with my work":
            if curr_timeslot_idx == 0:
                plant "{cps=15}a-a-a{/cps}h, you {cps=5}c-can{/cps}{cps=30} sit here if you want...{/cps}"
            else:
                plant "Sorry {w=0.25}, its not really a good time{w=0.25}, I'm really tired..."
                plant "I could help you another time though"
    
    jump plan

label free_plant1:
    scene bg_library

    if curr_timeslot_idx == 0:
        plant "{cps=10}Rodents and{/cps}{w=0.25}{cps=3}... h{/cps}mm{cps=3}...{/cps}{w=0.1} {cps=30}Garden Bugs with...{w=0.25} no{cps=3}...{/cps}"
        menu:
            plant "Rodents and... hmm... Garden Bugs with... no...{fast}"

            "There's a book on leaf eaters over there":
                plant "That's not what I was looking for..."
                jump plan

            "There’s a book on flying bugs over there":
                plant "{cps=15}T-Th{/cps}anks [player]-kun, {cps=3}...{/cps}{w=0.1} do you want t-to read it together?"
                jump plan

    else:
        plant "{cps=3}{size=124}Z{size=100}Zzz{size=64}zzz...{/cps}"
    jump plan

label free_plant2:
    scene bg_library

    if curr_timeslot_idx == 0:
        plant "*sleeping quietly in sun rays*"
        menu:
            plant "*sleeping quietly in sun rays*{fast}"

            "*put blank over her*":
                plant "{cps=5}hmm...{/cps} [player]-kun… what are you doing?{w=0.2} why did you wake me?"
                jump plan

            "*open curtain more*":
                plant "{cps=3}{size=124}Z{size=100}Zzz{size=64}zzz...{/cps}"
                jump plan

    else:
        "{w=1}No ones here{cps=3}...{/cps}"
    jump plan
