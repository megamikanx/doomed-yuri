default player_name = "???"
default player_name_revealed = False

# Affection points 
default carnivore_affection = 0
default herbivore_affection = 0
default plant_affection = 0
default fungus_affection = 0

# Day and timeslot tracking
define timeslots = ["Dawn", "Morning", "Afternoon", "After Hours", "Night"]

default day = 1
default curr_timeslot_idx = 0

# Free time dialogue tracker
default freetime_index = {
    "plant_morning": 0,
    "plant_afternoon": 0,
    "plant_afterhours": 0,
    "fungus_morning": 0,
    "fungus_afternoon": 0,
    "fungus_afterhours": 0,
    "herbivore_morning": 0,
    "herbivore_afternoon": 0,
    "herbivore_afterhours": 0,
    "carnivore_morning": 0,
    "carnivore_afternoon": 0,
    "carnivore_afterhours": 0,
}

default last_freetime_girl = None

# Ending tracker
default home_early_count = 0 # for bitchless ending

default trigger_bitchless_ending = False
default trigger_bad_ending = False # for bad endings
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
default where_fungus = "Classroom"






