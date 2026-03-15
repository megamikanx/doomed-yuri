screen eating_caption(msg):
    zorder 100

    frame:
        xalign 0.5
        yalign 0.85
        padding (20, 12)

        text msg size 36 color "#fff"

label event_plant:
    if plant_event_done:
        return

    $ plant_event_done = True

    scene bg_library with dissolve

    $ plant_affection += 1;

    player_thoughts "It's so quiet in here."
    player_thoughts "Plant-chan should be around here somewhere..."

    show plant neutral at center

    plant "H-hello...you came...t-t-take a seat..."
    plant "What parts are you having trouble with?"

    menu:
        "I've been having trouble with maths.":
            pass
        "I've been having trouble with this mechanics question.":
            pass
    
    show plant shy at center

    plant "S-so...you just apply this formula here..."
    plant "For th-this...you might need to brute force it...trial and error..."

    play sound "audio/fly_sound.ogg"

    player_thoughts "A fly...? Well that's annoying."

    window hide

    show plant eat at center
    show screen eating_caption("Mmf...")

    play sound "audio/eat.ogg"
    queue sound "audio/burp.ogg"

    $ renpy.pause(9, hard=True)
    
    hide screen eating_caption

    show plant surprise at center

    window show

    plant "S-S-Sorry!!!! I-I didn't mean to..."

    menu:
        "...":
            show plant neutral at center
            plant "As I was saying...this formula..."

        "What. In the literal fuck.":
            $ plant_affection += 2
            $ freaky = True
            show plant shy at center
            plant "Umm...S-sorry. It’s just a h-habit of mine."
            plant "T-The other girls also think its weird… (╥‸╥)"
        
        "Uhh...natural instinct...I guess.":
            $ plant_affection += 1
            $ freaky = True
            show plant shy at center
            plant "Do you really think so?"
            plant "The other girls think its w-weird."
    
    if freaky:
        show plant megablush at center
        plant "{cps=120}And m-maybe their right but-t… I-I mean its really okay if you think its weird, I’d be okay if you thought I was weird. It's kind of exciting… they call me a bunch of mean names… hehehehe...as they should...{/cps}"
        plant "{cps=130}A-A-And...it's not what people th-think...being called those names...they're like pet names right? Every loves having a pet...too bad plants aren't that much popular when it comes to pets...{/cps}"
        plant "{cps=150}B-But it's just that I would make a great pet...I like being stepped on...being called names...getting tied up...one could say it just makes some part of me tingle...I dunno...the other girls would never understand...{/cps}"
        
        plant "{cps=180}Itsfinethoughtotallydontworryaboutitnobodyhastounderstandnorwilltheyunderstandthisisfinethisisfinethisisfinethisisfinethisisfinet̵̛̘͎̀̈́͛̈́̔͘̚h̶̛̹̺̾͗͋̀͒̕i̷̢̞̺͖͓͆̂͗̒͂s̶̢̜̱̙͍̠̝̮̫̏̀̈́̎i̵̛̱̽s̷͔̫̯̓̓͛̾͗̎̀̇͠͝f̵͈͙̫̬̼̫͔̱̳̓̉͋̇́̓̚͝i̵̘̊̋̑̔͊n̵̗̈́̏̿̅͠e̶̢̖͍͇̠̅̍̓̒͒̿̂͝t̵̛̘͎̀̈́͛̈́̔͘̚h̶̛̹̺̾͗͋̀͒̕i̷̢̞̺͖͓͆̂͗̒͂s̶̢̜̱̙͍̠̝̮̫̏̀̈́̎i̵̛̱̽s̷͔̫̯̓̓͛̾͗̎̀̇͠͝f̵͈͙̫̬̼̫͔̱̳̓̉͋̇́̓̚͝i̵̘̊̋̑̔͊n̵̗̈́̏̿̅͠e̶̢̖͍͇̠̅̍̓̒͒̿̂͝t̵̛̘͎̀̈́͛̈́̔͘̚h̶̛̹̺̾͗͋̀͒̕i̷̢̞̺͖͓͆̂͗̒͂s̶̢̜̱̙͍̠̝̮̫̏̀̈́̎i̵̛̱̽s̷͔̫̯̓̓͛̾͗̎̀̇͠͝f̵͈͙̫̬̼̫͔̱̳̓̉͋̇́̓̚͝i̵̘̊̋̑̔͊n̵̗̈́̏̿̅͠e̶̢̖͍͇̠̅̍̓̒͒̿̂͝t̵̛̘͎̀̈́͛̈́̔͘̚h̶̛̹̺̾͗͋̀͒̕i̷̢̞̺͖͓͆̂͗̒͂s̶̢̜̱̙͍̠̝̮̫̏̀̈́̎i̵̛̱̽s̷͔̫̯̓̓͛̾͗̎̀̇͠͝f̵͈͙̫̬̼̫͔̱̳̓̉͋̇́̓̚͝i̵̘̊̋̑̔͊n̵̗̈́̏̿̅͠e̶̢̖͍͇̠̅̍̓̒͒̿̂͝t̵̛̘͎̀̈́͛̈́̔͘̚h̶̛̹̺̾͗͋̀͒̕i̷̢̞̺͖͓͆̂͗̒͂s̶̢̜̱̙͍̠̝̮̫̏̀̈́̎i̵̛̱̽s̷͔̫̯̓̓͛̾͗̎̀̇͠͝f̵͈͙̫̬̼̫͔̱̳̓̉͋̇́̓̚͝i̵̘̊̋̑̔͊n̵̗̈́̏̿̅͠e̶̢̖͍͇̠̅̍̓̒͒̿̂͝t̵̛̘͎̀̈́͛̈́̔͘̚h̶̛̹̺̾͗͋̀͒̕i̷̢̞̺͖͓͆̂͗̒͂s̶̢̜̱̙͍̠̝̮̫̏̀̈́̎i̵̛̱̽s̷͔̫̯̓̓͛̾͗̎̀̇͠͝f̵͈͙̫̬̼̫͔̱̳̓̉͋̇́̓̚͝i̵̘̊̋̑̔͊{/cps}"

        show plant 4eyes shy at center

        menu:
            "I like you as you are":
                show plant sad at center
                plant "Oh...you're not calling me names?"
            
            "Nevermind, that's crazy. Never look like that in public...ever.":
                $ plant_affection += 2
                show plant happy at center
                plant "H-Hehe...we should study together more often..."
            
            "It might be a bit weird, but I think you’re… unique to me.":
                $ plant_affection += 1
                show plant happy at center
                plant "I wouldn't mind you minding..."
        
    else:
        pass
    
    show plant shy at center
    herbivore "I-I hope I helped...I'll...see you around... 𐔌՞. .՞𐦯"

    hide plant shy with dissolve

    jump plan
    
    return
