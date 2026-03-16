transform surprise_shake:
    xoffset 0
    yoffset 0
    ease 0.03 xoffset -12
    ease 0.03 xoffset 12
    ease 0.03 xoffset -10
    ease 0.03 xoffset 10
    ease 0.03 xoffset -6
    ease 0.03 xoffset 6
    ease 0.03 xoffset 0

label free_carnivore_fungushere:
    scene bg_cafeteria

    play sound "audio/freetime_event.ogg"

    "Both [carnivore] and [fungus] are here. Who do you want to talk to?"
    menu:
        "Both [carnivore] and [fungus] are here. Who do you want to talk to?{fast}"
        "[carnivore]":
            $ store.last_freetime_girl = "herbivore"
            $ freetime_index["carnivore"] += 1
            $ renpy.jump("free_carnivore"+ str(freetime_index["carnivore"] - 1))

        "[fungus]":
            $ meet_fungus = True
            $ store.last_freetime_girl = "fungus"
            $ freetime_index["fungus"] += 1
            $ renpy.jump("free_fungus"+str(freetime_index["fungus"] - 1))


label free_carnivore0:
    scene bg_cafeteria
    play sound "audio/freetime_event.ogg"
    show carnivore neutral at center
    with dissolve
    carnivore "Well look who's here."

    show carnivore happy 
    with dissolve
    carnivore "You got any food on ya? I'm so hungry I could eat a cow."

    menu:
        "Scram!":
            show carnivore angry with dissolve
            carnivore "Baka! It's not like I was starving or anything!"

        "I've got leftover canned tuna from earlier...":
            $ carnivore_affection += 2
            show carnivore smug, surprise_shake
            carnivore "TUNA?!"
            carnivore "ONE CAN OF TUNA, 20 GRAMS OF PROTEIN!"

            show carnivore happy with dissolve
            carnivore "I knew you wouldn't disappoint me, underling."

            player_thoughts "Protein is that important, I guess..."

    jump plan

label free_carnivore1:
    scene bg_cafeteria
    play sound "audio/freetime_event.ogg"
    show carnivore angry with dissolve

    carnivore "{size=+12}ARE YOU KIDDING ME?{/size}"
    carnivore "{size=+12}A PROMISE WAS MADE...AND NOT KEPT!!{/size}"

    hide carnivore angry
    player "What's up?"

    show carnivore angry with dissolve
    carnivore "{size=+12}THE LUNCH LADY PROMISED 2 FRIED EGGS TO WHOEVER GOT IN LINE FIRST{/size}"
    carnivore "{size=+12}AND SHE GAVE IT TO THAT PRICK FUNGUS INSTEAD!{/size}"
    carnivore "{size=+15}SHE WAS ONLY FIRST BECAUSE SHE DITCHED!{/size}"

    menu:
        "Too slow! What can you say, she was faster.":
            carnivore "Huh?! You're siding with her too?!"
            carnivore "Watch your back..."
            player_thoughts "I should really get going..."

        "Yeah, stand up for your rights.":
            $ carnivore_affection += 2
            show carnivore smug with dissolve
            carnivore "Totally. Gotta show them who's boss!"
            player_thoughts "But does it really matter that much...?"


    jump plan

label free_carnivore2:
    scene bg_cafeteria
    play sound "audio/freetime_event.ogg"
    show carnivore neutral at center
    with dissolve
    carnivore "Oi oi oi! It seems you can’t get enough of me underling!"
    carnivore "Whaddya want this time?"

    show carnivore happy with dissolve
    carnivore "Oh actually, I went through the lunch line too many times."
    show carnivore angry with dissolve
    carnivore "They banned me from getting more. Woe is me!"
    carnivore "I’ve had 19 pounds of meat in a single sitting and am still starving!"
    carnivore "I might die of starvation! Curse my endless gluttony!"
    show carnivore smug with dissolve 
    carnivore "But you’ve just arrived… could you get in line and bring me some more food?"

    menu:
        "Alright, alright, I'm not hungry anyway.":
            $ carnivore_affection += 1
            show carnivore happy with dissolve
            carnivore "I knew I could count on you, underling!"

        "Nuh-uh you big back! You’re done for the day! God created a layer of hell solely for sinners like you!":
            show carnivore angry with dissolve
            carnivore "Fine then, you ungrateful peasant! I guess I’ll just sit here and die then!"
            show carnivore smug with dissolve 
            carnivore "Or… perhaps I’ll eat something else…"
            
            player_thoughts "I really should get going..."

    jump plan

label free_carnivore3:
    scene bg_cafeteria
    play sound "audio/freetime_event.ogg"
    show carnivore happy at center
    with dissolve
    carnivore "OI OI!!!!"
    player "...????"

    show carnivore smug with dissolve
    carnivore "Glad you came underling."
    carnivore "I'm here to challenge you to an eating competition!!!"

    menu:
        "Bring it on. I'll smoke you.":
            $ carnivore_affection += 1
            show carnivore happy with dissolve
            carnivore "That's the spirit!!"
            
            scene bg_cafeteria with fade

            player "Mmmf...can't...eat...anymore..."
            
            show carnivore smug with dissolve
            carnivore "You know what underling? I'm impressed."
            carnivore "Chugging the hot dog in liquid form with water? That's some strategy right there."

            player "I don't get it...how is she still fine?!"
        
        "Sure...let's get this over with.":
            show carnivore angry with dissolve
            carnivore "Not the attitude I'm looking for...but it'll do."

            scene bg_cafeteria with fade
            player "I'm done. Can't eat anymore."
            show carnivore neutral with dissolve
            carnivore "WHAT?! You had two!!!!!"
            player "Yeah. And I'm full."
            show carnivore angry with dissolve
            carnivore "I give you the honor of competing against ME, and these are the energy levels you give me?"
            carnivore "Hmmph."
            
    jump plan