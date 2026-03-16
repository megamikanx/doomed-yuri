define base_char = Character(color="#FFFFFF")

# Player
define player = Character("[player_name]", kind=base_char)
define player_thoughts = Character("[player_name]", what_italic = True, kind = base_char)

#Name used in text for colour
define carnivore = "{color=#db3a1a}Carnivore-chan{/color}" 
define herbivore = "{color=#9e005c}Herbivore-chan{/color}" 
define plant = "{color=#136100}Plant-chan{/color}" 
define fungus = "{color=#5a006e}Fungus-chan{/color}"


# Heroines
define mystery = Character("???", kind = base_char)
define carnivore = Character(carnivore, color = "#db3a1a", image = "carnivore_default", kind = base_char)
define herbivore = Character(herbivore, color = "#9e005c", image = "herbivore_default", kind = base_char)
define plant = Character(plant, color = "#136100", image = "plant_default", kind = base_char)
define fungus = Character(fungus, color = "#5a006e", image = "fungus_default", kind = base_char, what_prefix="{cps=15}", what_suffix="{/cps}")


 