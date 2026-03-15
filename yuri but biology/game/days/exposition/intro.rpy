



label intro:

    scene bg_courtyard
    #exposition dump at start of game
    player "It’s my first day at eco-gakuen, this supposedly great school accepting all kinds of different students." 
    player "I had to transfer out of my old school because someone brought in an animal infected with some kind of unknown disease." 
    player "It happened right before an exam I was about to take that I crammed for..."
    player "What a waste of studying amirite."
    player "Anyways the school closed down because most of the staff and students caught the infection and died. And now the school is permanently enclosed by a 20 mile quarantine area." 
    player "So now I’m here I guess. I hear there are some pretty weird people going to eco-gakuen."
    player "Let’s hope that isn’t true…" 
    player "Well here goes. "

    "*opens door*"

    scene bg_classroom

    herbivore "Oh"
    herbivore "You must be the transfer student!"
    herbivore "Weird... you look awfully normal."
    herbivore "Anyways, I’m [herbivore], the class president."
    herbivore "What's your name?"


label name_loop:

    $ player_name = renpy.input("Whats your name:")

    $ player = Character("[player_name]", kind=base_char)

    menu:
        player "Is this my name"

        "Yes":
            herbivore "Nice to meet you [player]-kun"

        "No":
            jump name_loop

    herbivore "Have a seat wherever, {w=0.5} I’ll introduce you to your class-{w=0.35}{nw}"

    carnivore "{size=124}oi oi oi!"
    carnivore "This must be the new transfer student."
    carnivore "You look like you could use some protein.{w} Cmon I’ll show you around the school."
    carnivore "If you didn’t know, this is the classroom."
    player "{i}I knew that{/i}"

    carnivore "It's pretty boring here. [herbivore] always hangs out here.{w} What a freaking nerd."

    herbivore "Shut up Carnivore! You’re embarrassing me in front of [player]-kun! Baka baka"

    scene bg_library

    carnivore "This is the library."
    carnivore "It’s stuffy here isn’t it?{w=1} Absolutely no space to run around at all."

    player "{i}The windows are positioned in a way where sunlight covers every inch of the room.{w=0.5}\n My eyes hurt.{/i}"

    carnivore "[plant] likes to be here a lot.{w=1}\n{size=124}HEY!{w=0.25} You awake?"

    plant "{size=124}Zzz.​​(-_-) zzZ"
    carnivore "{size=124}LAME{w=0.5}{nw}"
    carnivore "{size=124}NEXT!!"

    scene bg_courtyard

    #could add text movement here
    carnivore "This is the courtyard.{w}\n{size=60}You smell that?" 
    carnivore "Ah, I see [fungus] is in her usual spot.\n{w}Yeah I didn’t know students can just buy cigarettes. " 

    fungus "sup.{w=0.5} want one?"

    carnivore "She’s hella weird like that.{w}\nDon’t hang out with her if you don’t want second hand lung problems."

    fungus "brah💀.{w=0.75}\ndont knock it till you try it carni.{w=0.75} my lungs are genuinely fine.{w=0.5} im brooding rn.{w=0.25} dont talk to me."

    carnivore "Alright loser.{w=0.5} See you"

    scene bg_cafeteria

    carnivore "This is the cafeteria." 
    carnivore "This is ma territory,{w=0.25} none of the others stay around for long.{w} And today’s Mystery Meat Monday so they’ll be gone even quicker!!" 
    carnivore "Come sit at my table.{w=0.25} Make sure to be there or else I’ll kill you."

    player "{i}I’ll have free time throughout the day…{w=0.5} I should decide on my schedule.{/i}"

    return

    
