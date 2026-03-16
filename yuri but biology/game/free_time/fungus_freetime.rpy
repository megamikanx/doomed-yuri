

label free_fungus_nothere:
    "{cps=3}. . . .{/cps}"
    "no one is here"
    jump plan


label free_fungus0:
    scene bg_courtyard

    play sound "audio/freetime_event.ogg"

    player_thoughts "Funny seeing Fungus-chan here...she's got something in her hand."
    player_thoughts "Is that...an orange? Maybe a mandarin...?"

    show fungus neutral at center
    with dissolve

    fungus "sheng ri kuai le"

    menu:
        "Sorry, I don't speak Mandarin.":
            $ fungus_affection += 2
            show fungus happy with dissolve
            fungus "FINALLY someone who gets it. Plant-chan got offended last time."

            player_thoughts "I guess her culture is not our costume..."

        "What?":
            show fungus angry with dissolve 
            fungus "nvm. seeya."

            player_thoughts "Oh...she was having a mandarin...and speaking Mandarin...very punny."
    
    jump plan

label free_fungus1:
    scene bg_courtyard
    play sound "audio/freetime_event.ogg"
    player_thoughts "Can't believe I overslept on the first week...wait...is that Fungus-chan?"
    player_thoughts "What's that in her mouth? Green...toast...?"

    show fungus neutral at center
    fungus "aaaa...jigoku jigoku~~"

    menu:
        "Is that...mold?!":
            show fungus angry at center
            fungus "imma hold your hand when I say this...it's green onion."

            player_thoughts "Dang...totally embarrassed myself."

        "Bro really said jigoku out loud.":
            $ fungus_affection += 2
            show fungus happy at center
            fungus "says the guy playing a dating sim :P"

            player_thoughts "What is she saying..."

    jump plan

label free_fungus2:
    scene bg_courtyard
    play sound "audio/freetime_event.ogg"
    show fungus neutral at center 
    with dissolve
    fungus "~🎵🎵🎵"

    player_thoughts "Ah...Fungus-chan is on reels again..."
    player_thoughts "Should I talk to her?"

    menu:
        "You ruined my FYP.":
            show guy meme at center 
            with dissolve

            show fungus neutral at center
            with dissolve

            fungus "jeez u just don't know game"

            player_thoughts "Does she just watch brainrot all day?"

        "Did I really catch you liking a satosugu reel?":
            $ fungus_affection += 2
            show fungus surprise at center

            show fungus neutral at center
            with dissolve

            fungus "shhh twin...this is between you and me..."

            player_thoughts "I guess she's into yaoi."

    jump plan

label free_fungus3:
    scene bg_courtyard
    play sound "audio/freetime_event.ogg"
    show fungus neutral at center
    with dissolve
    fungus "meow"

    menu:
        "meow":
            $ fungus_affection += 2
            fungus "ayyyy"
            player_thoughts "ichi ni san..."
        
        "What?":
            show fungus angry
            fungus "bruh."
            player_thoughts "Did I piss her off?"

    jump plan




    
    
    