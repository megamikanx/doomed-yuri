label event_carnivore1:
    if carnivore_event_done:
        return

    $ carnivore_event_done = True

    scene bg_cafeteria with dissolve

    show carnivore neutral at center with dissolve

    carnivore "Oh, look who decided to show up."
    carnivore "So you realized who’s in charge around here. Heh…"

    $ carnivore_affection += 1;

    carnivore "Look at all this meaty goodness! Take a big bite!"

    player_thoughts "She's really keen on eating it with me...what do I do?"

    menu:
        "This shit look so ass.":
            show carnivore angry
            carnivore "Huh??? You got a bone to pick?"
            carnivore "No wonder you’re scrawny. More to myself then I guess!"

        "That looks delicious! Lemme have some.":
            $ carnivore_affection += 2
            $ hamster_story = True
            show carnivore happy
            carnivore "So you have good taste too, I see… heh."
            carnivore "It kinda tastes like hamster. Y’know I had a hamster once."

            player "What?"
            with vpunch
        
        "What's this made of?":
            $ hamster_story = True
            show carnivore shy
            carnivore "You know what? It tastes a lot like hamster."
            carnivore "Not that I would know..."
            carnivore "It's totally not like I've eaten a hamster before."

            player_thoughts "..."
            player_thoughts "Yeah...she's definitely eaten a hamster before."

    show carnivore neutral

    if hamster_story:
        player "Mind elaborating?"

        show carnivore shy

        carnivore "He was a class pet. He was so fat...everybody loved the damn thing."
        carnivore "Don't get me wrong. I liked him too!"

        show carnivore angry
        carnivore "Until one day, I just...needed some more protein."
        carnivore "...And he was just there."

        show carnivore shy
        carnivore "That's why all the other girls treat me like shit."
        carnivore "They'll never understand."

        show carnivore angry
        carnivore "I bet you think that's messed up too."

        menu:
            "Yeah, that's hella messed up.":
                carnivore "This is what I get for being vulnerable. Normies."
                with hpunch
            
            "You did what you had to do.":
                $ carnivore_affection += 2
                show carnivore happy
                carnivore "I knew you would understand! You've got great taste, underling."

        player_thoughts "What a story..."
        
    else:
        pass
    
    show carnivore happy
    carnivore "Time for class! See ya!"

    hide carnivore with dissolve

    jump plan
    return
