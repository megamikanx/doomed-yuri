default player_name = "???"
default player_name_revealed = False

# Affection points 
default carnivore_affection = 0
default herbivore_affection = 0
default plant_affection = 0
default fungus_affection = 0

default MAX_AFFECTION_DIFF = 4

# Day and timeslot tracking
define timeslots = ["dawn", "morning", "afternoon", "afterhours", "night"]

default day = 1
default curr_timeslot_idx = -1
define schedule = ["","",""]

# Free time dialogue tracker
default freetime_index = {
    "plant": 0,
    "fungus": 0,
    "herbivore": 0,
    "carnivore": 0
}


default last_freetime_girl = None # could be made into list to prevent event girl aswell

# Ending tracker
default home_early_count = 0 # for bitchless ending

default trigger_bitchless_ending = False
default trigger_world_end_ending = False # for bad endings
default trigger_good_ending = False
default trigger_best_ending = False

# Event guards
default chocolate_given = False

default carnivore_event_done = False
default hamster_story = False

default herbivore_event_done = False
default racism = False

default plant_event_done = False
default freaky = True

default fungus_event_done= False
default celebrate_differences = False

# Fungus locations
define locations = ["Classroom", "Library", "Courtyard", "Cafeteria"]
# empty if in courtyard
define where_fungus = ["", "classroom", "cafeteria", "library", ""]
define met_fungus = False






