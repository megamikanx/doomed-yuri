define base_char = Character(color="#FFFFFF", ctc="ctc", ctc_pause="ctc", ctc_position="fixed")

# Player
define player = Character("[player_name]", kind=base_char)
define player_thoughts = Character("[player_name]", what_italic = True, kind = base_char)

#Name used in text for colour
define carnivore = "{color=#db3a1a}Carnivore-chan{/color}" 
define herbivore = "{color=#f06ec0}Herbivore-chan{/color}" 
define plant = "{color=#1c9e21}Plant-chan{/color}" 
define fungus = "{color=#845d8f}Fungus-chan{/color}"


# Heroines
define mystery = Character("???", kind = base_char)
define carnivore = Character(carnivore, color = "#db3a1a", image = "carnivore_default", kind = base_char)
define herbivore = Character(herbivore, color = "#f06ec0", image = "herbivore_default", kind = base_char)
define plant = Character(plant, color = "#1c9e21", image = "plant_default", kind = base_char)
define fungus = Character(fungus, color = "#845d8f", image = "fungus_default", kind = base_char, what_prefix="{cps=15}", what_suffix="{/cps}")


 