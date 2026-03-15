define base_char = Character(color="#FFFFFF", ctc="ctc", ctc_pause="ctc", ctc_position="fixed")

# Player
define player = Character("[player_name]", kind=base_char)
define player_thoughts = Character(None, what_italic = True, kind = base_char)

# Heroines
define carnivore = Character("Carnivore-chan", color = "#db3a1a", image = "carnivore_default", kind = base_char)
define herbivore = Character("Herbivore-chan", color = "#f06ec0", image = "herbivore_default", kind = base_char)
define plant = Character("Plant-chan", color = "#1c9e21", image = "plant_default", kind = base_char)
define fungus = Character("Fungus-chan", color = "#845d8f", image = "fungus_default", kind = base_char)


 