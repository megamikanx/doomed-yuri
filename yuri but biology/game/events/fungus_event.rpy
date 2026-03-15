image bg william_video = Movie(play="movies/william.webm")
image bg violence_video = Movie(play="movies/violence.webm")

transform shrug:
    ease 0.08 yoffset -4
    ease 0.08 yoffset 0

label event_fungus:
    if fungus_event_done:
        return

    $ fungus_event_done = True
    $ fungus_affection += 1;

    scene bg_lobby with dissolve

    play music "audio/crowd.ogg"

    show fungus neutral at center with dissolve

    fungus "yo"
    fungus "sup"

    show fungus surprise at center

    window hide
    $ renpy.movie_cutscene("videos/william.webm")
    window show

    show fungus neutral at center with dissolve

    fungus "lmao? the fuck. was that."

    scene bg_lobby with dissolve

    stop music fadeout 2.0

    menu:
        "I don't know, but stealing public property is wrong.":
            show fungus surprise
            fungus "don't you regularly steal paper from the school printer?"
            fungus "wtv. to each their own 🤷"

        "lmao":
            $ fungus_affection += 1
            $ celebrate_differences = True
            show fungus happy at center, shrug
            fungus "anyways, want popcorn?"
        
        "It's been so long...":
            $ fungus_affection += 2
            $ celebrate_differences = True
            show fungus happy at center

            fungus "I bet u emote in the bathroom in your free time"
            show fungus smile at center
            fungus "dw I've done that"

            player_thoughts "I'm pretty sure it's just you..."

    show fungus neutral

    fungus "I got snacks. let's head inside."

    scene bg_theater with fade

    if celebrate_differences:
        player_thoughts "Jeez...when is the movie starting?"

        show fungus neutral at center

        fungus "damn, really just should've came here later..."
        fungus "this is like the 20th ad."

        fungus "welp guess we just yap."
        fungus "how's school?"

        menu:
            "Everybody gets along so well. I love this place!":
                show fungus surprise at center
                fungus "...u did speak to the other girls right?"
                fungus "sometimes you're such a man."

                player_thoughts "...What does that mean?"
                player_thoughts "Dunno. Can't be bothered to ask."
            
            "Dunno...everyone's nice but they're always beefing.":
                $ fungus_affection += 1
                show fungus happy at center
                fungus "you said it i didn't"
                fungus "although i was about to."

                show fungus smile at center

                fungus "yea...it gets heated sometimes."
                fungus "but it'd be sad if even one of us were missing."
                fungus "circle of life type shi 🙌"
            
            "Lowkey, nobody is normal here. What's wrong with everybody?" if plant_event_done and carnivore_event_done and herbivore_event_done:
                $ fungus_affection += 2
                show fungus happy at center
                
                fungus "I see you've been diligent the past few days."
                fungus "but we gotta make the game interesting somehow."

                player_thoughts "Is this just a game for her...?"
        
    else:
        pass

    show fungus surprise at center
    fungus "oh, movie's starting."
    
    scene bg_theater with fade

    player_thoughts "It was a good movie...worth the wait."

    show fungus happy at center
    fungus "what a movie. my favorite part was- "
    show fungus surprise with dissolve

    play music "audio/boo.ogg"
    $ renpy.pause(1, hard=True)
    
    window hide
    $ renpy.movie_cutscene("videos/violence.webm")
    stop music
    window show

    show fungus surprise at center

    fungus "dafuq"

    hide fungus with dissolve

    return

