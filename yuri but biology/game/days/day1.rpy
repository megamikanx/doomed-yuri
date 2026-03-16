label start:
    jump intro

label day1_morning:
    scene bg_static with dissolve
    centered "Day 1  ·  Morning"
    jump map


label day1_afternoon:
    scene bg_static with dissolve
    centered "Day 1  ·  Afternoon"
    # go_next() already fired event_carnivore1 before reaching here
    # if the player had scheduled it – so this only runs for free time.
    jump map


label day1_afterhours:
    scene bg_static with dissolve
    centered "Day 1  ·  After Hours"
    jump map


init python:

    SLOT_NAMES = ["morning", "afternoon", "afterhours"]

    def go_next():
        store.curr_timeslot_idx += 1

        # end of day
        if store.curr_timeslot_idx == 3:
            store.day += 1

            if are_you_bitchless():
                renpy.jump("bitchless_ending")
                return

            if store.day == 7:         
                end_game()
                return

            store.curr_timeslot_idx  = -1
            store.schedule           = ["", "", ""]
            store.meet_fungus        = False
            store.last_freetime_girl = None
            renpy.jump("phone")
            return

        # ── scheduled event for this slot ───────────────────
        name = store.schedule[store.curr_timeslot_idx]
        if name:
            renpy.jump("event_" + name + str(store.day))
            return

        # ── free slot: show title card then map ─────────────
        slot       = SLOT_NAMES[store.curr_timeslot_idx]
        slot_label = "day" + str(store.day) + "_" + slot
        if renpy.has_label(slot_label):
            renpy.jump(slot_label)
        else:
            renpy.jump("map")

    def are_you_bitchless():
        all_aff = [
            store.carnivore_affection,
            store.herbivore_affection,
            store.plant_affection,
            store.fungus_affection,
        ]
        return sum(all_aff) == 0

    def end_game():
        all_aff = [
            store.carnivore_affection,
            store.herbivore_affection,
            store.plant_affection,
            store.fungus_affection,
        ]
        if (max(all_aff) - min(all_aff)) > store.MAX_AFFECTION_DIFF:
            renpy.jump("world_end_ending")
        else:
            renpy.jump("good_ending")
