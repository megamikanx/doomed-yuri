
define name = "You"

define p = Character(name)
define herb = Character("Herbivore-chan")

#Introduction


label intro:
    # added interdimate dialogue that should be changed
    scene introbg:
        align (0.5, 0.5)
    #Setup
    p "It’s my first day at eco- high school."
    p "The sun is shining, plants are blooming, animals are playing and fungi are growing."
    p "But in 1 week this ecosystem could fall apart"
    p "Unless we save it."

    #Start of school
    herb "Oh"
    herb "You must be the transfer student!" 
    herb "Weird.. you look awfully normal."
    herb "Anyways, I’m Herbivore chan, the class president."
    herb "Whats your name?"

label naming_loop:
    $ name = renpy.input("Your name: ") + "-kun"

    $ p = Character(name)

    menu:
        p "Is this your name?"

        "Yes":
            herb "Hello [name]"

        "No":
            jump naming_loop

    return