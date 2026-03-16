
label free_herbivore_fungushere:
    scene bg_classroom

    "Both [herbivore] and [fungus] are here. Who do you want to talk to?"
    menu:
        "Both [herbivore] and [fungus] are here. Who do you want to talk to?{fast}"
        "[herbivore]":
            $ store.last_freetime_girl = "herbivore"
            $ freetime_index["herbivore"] += 1
            $ renpy.jump("free_herbivore"+ str(freetime_index["herbivore"] - 1))

        "[fungus]":
            $ meet_fungus = True
            $ store.last_freetime_girl = "fungus"
            $ freetime_index["fungus"] += 1
            $ renpy.jump("free_fungus"+str(freetime_index["fungus"] - 1))



label free_herbivore0:

    scene bg_classroom

    if curr_timeslot_idx != 2:
        show herbivore surprise at center with dissolve
        herbivore "hmm{w=0.25} [player]-kun?{w=0.75} What are doing here?"
        herbivore "Its nice we get to talk more{w=0.5}, but you should really go meet your other classmates"
        jump plan

    show herbivore surprise at center with dissolve
    herbivore "[player]-kun!{w=0.75} How did your first day of school go?"

    show herbivore neutral at center
    herbivore "We have amazing students here don’t we?" 
    menu:
        herbivore "We have amazing students here don’t we?{fast}"

        ". . .":
            show herbivore sad at center
            herbivore "{cps=2}. . .{/cps}"
            herbivore "Yeah-he they’re really {cps=6}. . .{/cps}"
            
        "Yeah I guess they’re cool":
            show herbivore happy at center
            herbivore "They are all unique in their own ways{w=0.25}, and I love every one of them!{w=0.5}"
            show herbivore smug at center
            herbivore "No discrimination or anything!{w=0.75} {size=80}{cps=10}Haha!{/cps}"
        
    show herbivore happy at center
    herbivore "If you need anything or just want to hang out, come by again!" 
    herbivore "As your class prez{w=0.5}, it's my duty to ensure you properly settle in!"
    herbivore "See you!"
    jump plan

    hide herbivore happy with dissolve


label free_herbivore1:

    scene bg_classroom

    show herbivore neutral at center with dissolve

    herbivore "Oh hi, [player]-kun{w=0.25}. How was your day today?"
    if curr_timeslot_idx != 2:
        show herbivore sad at center
        herbivore "I’ve been taking care of this flower in our classroom{w}. But I don't think it will ever bloom{w=0.25}.\nMaybe we aren't considering what it needs?"
        hide herbivore sad with dissolve
        jump plan

    show herbivore happy at center
    herbivore "I’ve been taking care of this flower in our classroom{w=0.25}. When do you think it’ll start blooming?"

    menu:
        herbivore "I’ve been taking care of this flower in our classroom. When do you think it’ll start blooming?{fast}"

        "Looks like just a few more days":
            herbivore "I hope so!"
            hide herbivore happy with dissolve

        "You’re prettier than that useless flower":
            show herbivore shy at center
            herbivore "[player]-kun...!{w=0.5} Thank you{w=1}, {cps=30}I think [player]-kun is{w=0.25} cool{/cps}{cps=15} too . . .{/cps}"
            hide herbivore shy with dissolve
    jump plan


label free_herbivore2:

    scene bg_classroom

    show herbivore neutral at center with dissolve

    herbivore "[player]-kun, how are you doing?"
    show herbivore shy at center
    herbivore "I just wanted to ask you something{cps=5} . . .{/cps}"

    if curr_timeslot_idx != 2:
        show herbivore smug at center
        herbivore "But [carnivore]'s making trouble{w}, damn mea {cps=6}. . .{/cps}{w=0.25}{nw}"
        herbivore "ah. . .{w=0.25} anyway I'll see you later"
        jump plan

    herbivore "What’s your favorite food?"

    menu:
        herbivore "What’s your favorite food?{fast}"

        "Meat":
            show herbivore sad at center
            herbivore "{cps=5}Ah . . haha . . Y{/cps}ou’re joking right{cps=3} . . .{/cps} ?"
            hide herbivore sad with dissolve
        
        "Carrots":
            show herbivore happy at center
            herbivore "Sugoi!!{w=0.25} Me too!"
            herbivore "We have so much in common [player]-kun!{w=0.25} Maybe we’re meant to be together."
            hide herbivore happy with dissolve
    jump plan

label free_herbivore3:

    herbivore "hello"