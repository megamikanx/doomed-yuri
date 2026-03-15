transform silhouette:
    matrixcolor TintMatrix("#000") * SaturationMatrix(0.0)

transform normal_look:
    matrixcolor None

label event_herbivore:
    if herbivore_event_done:
        return

    $ herbivore_event_done = True

    scene bg_classroom with dissolve

    $ herbivore_affection += 1;

    player_thoughts "I wonder what kind of flowers Herbivore-chan is into..."
    player_thoughts "Maybe dandelions? She's quite the shy type."

    show herbivore neutral at center, silhouette
    with dissolve

    mystery "Nom nom...crunch crunch..."

    player_thoughts "What's that sound?"

    show herbivore surprise at center, normal_look
    with Dissolve(0.4)

    herbivore "[player_name]-kun?!"
    herbivore "I didn't expect anyone to be here! You weren't supposed to see that!"

    show herbivore shy at center, normal_look

    herbivore "Oh no...I'm super embarrassed..."
    herbivore "You must think I'm weird now, don't you?"

    menu:
        "Did you just eat that flower?":
            herbivore "Please don't tell the others..."
            herbivore "I promise it won't happen again!"

        "You hungry?":
            $ herbivore_affection += 1
            $ racism = True
            show herbivore angry at center, normal_look
            herbivore "Now you're just making fun of me!"

        "It's okay. I understand.":
            $ herbivore_affection += 2
            $ racism = True
            show herbivore surprise at center, normal_look
            herbivore "Really?"
            show herbivore happy at center, normal_look
            herbivore "Thank you, [player_name]-kun...I always knew we had something in common."

    show herbivore neutral at center, normal_look

    if racism:
        player "But why is this a secret?"

        show herbivore shy at center, normal_look

        herbivore "If it were Plant-chan, she wouldn't have been so chill about it."
        herbivore "But honestly..."

        show herbivore smug at center, normal_look

        herbivore "She's just a plant. Why would I care?"
        herbivore "They're just dumb useless organisms. Zero thoughts or feelings."
        herbivore "The same goes for carnivores. Stupid mutts controlled by their desire to eat."
        herbivore "And don't even get me started on that good for nothing fungus..."

        player "..."

        show herbivore surprise at center, normal_look

        herbivore "Did I really just say all that?!"

        show herbivore shy at center, normal_look

        herbivore "Plant-chan's going to be so angry if she hears about this..."
        herbivore "You're not gonna tell her...are you?"
        herbivore "I'm sorry, [player_name]-kun! Forget that you heard!"

        menu:
            "Just wait til she hears about this.":
                show herbivore smug at center, normal_look
                herbivore "Well, humans are no better anyways."
                herbivore "Good luck with your mid ass molars."
    
            "Are you...racist?":
                $ herbivore_affection += 1
                show herbivore surprise at center, normal_look
                herbivore "Wh-what?! It's not like my statements are racially motivated or anything..."

            "It's okay, I 100 percent agree with you. Herbivores for the win!":
                $ herbivore_affection += 2
                show herbivore happy at center, normal_look
                herbivore "Wow...[player_name]-kun...I feel like I can finally be myself when I'm around you."
                herbivore "Arigatogozaimasu :3"

        show herbivore angry at center, normal_look

        herbivore "And [player_name]-kun, I think I should warn you..."
        herbivore "Don’t stay too close to carnivore chan, those animals...they're feral."

        show herbivore sad at center, normal_look
        herbivore "The orphanage...it was so cold and lonely..."

        player_thoughts "I think I've had enough of a talk with her today..."
        
    else:
        pass
    
    show herbivore shy at center, normal_look
    herbivore "It was nice meeting you here. I think I'm going to head home. Bye!"

    hide herbivore shy with dissolve

    return
