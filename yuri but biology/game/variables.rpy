DEFAULT_AFFECTION = 0

default player_name = "???"
default player_name_revealed = False

# Affection points 
default carnivore_affection = DEFAULT_AFFECTION
default herbivore_affection = DEFAULT_AFFECTION
default plant_affection = DEFAULT_AFFECTION
default fungus_affection = DEFAULT_AFFECTION

# Day and timeslot tracking
timeslots = ["Dawn", "Morning", "Afternoon", "After Hours", "Night"]

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

# Events
default chocolate_given = False

default carnivore_flag = False
default herbivore_flag = False
default plant_flag = False
default fungus_flag = False

# Fungus locations
locations = ["Classroom", "Library", "Courtyard", "Cafeteria"]
default where_fungus = "Classroom"






