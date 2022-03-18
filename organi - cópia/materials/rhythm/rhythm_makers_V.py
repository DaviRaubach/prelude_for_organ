import abjad
import abjadext.rmakers as rmakers
import evans
import random


# estrutura

# 4 _ _ _ 1 4 _ _ _
#   2 _ 3 _ _ 2 _ _
#     3 _ _ 2 _ _ 3

# x
# x y 
# x y z
# x z
# 

selector = abjad.select().tuplets()[1:]
selector = selector.map(abjad.select().note(1))

last_leaf = abjad.select().leaf(-6)
nonlast_tuplets = abjad.select().tuplets()[:-1]

rhythm_maker_voice_one = rmakers.stack(
    rmakers.even_division([8], extra_counts=[0, 1]),
    rmakers.tie(abjad.select().leaves().get([0], 2)),
    rmakers.rewrite_sustained(),
    # rmakers.beam(),
    # rmakers.extract_trivial(),
    )

# rmakers.stack(rmakers.tuplet([(2, 2, 2), (2, 2, 2, 2)]), rmakers.beam(), rmakers.extract_trivial(),)

rhythm_maker_voice_four = rmakers.stack(
    rmakers.even_division([8], extra_counts=[0, 1]),
    rmakers.force_rest(abjad.select().leaves().get([0])),
    rmakers.tie(abjad.select().leaves().get([1], 2)),
    rmakers.rewrite_sustained(),
    # rmakers.beam(),
    # rmakers.extract_trivial(),
    )
    # rmakers.tuplet(
    # [(1, 2, 2, 1), (1, 2, 2, 2, 1)],), 
    # rmakers.force_rest(abjad.select().leaves().get([0])),
    # rmakers.tie(abjad.select().leaves().get([3], 4)),
    # rmakers.beam(),
    # rmakers.rewrite_sustained(),
    # rmakers.extract_trivial(),
    


rhythm_maker_voice_one_old = rmakers.stack(
    rmakers.talea(
        [1],  # counts
        4,
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

rhythm_maker_voice_two = rmakers.stack(
    rmakers.talea(
        [2, 3],  # counts
        8, # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

rhythm_maker_voice_three = rmakers.stack(
    rmakers.talea(
        [3, 2],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

rhythm_maker_voice_four_old = rmakers.stack(
    rmakers.talea(
        [1],  # counts
        4,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )
# MATERIAL FROM SEGMENT 2 AND 3
# REST LIST
rest_list = evans.e_dovan_cycle(
    n=2, iters=16, first=1, second=1, modulus=3)
rest_list.sort(reverse=True)

# NOTE LIST VOICE TWO
note_list_voice_two = [3, 1]
non_cyc_generator = evans.CyclicList(lst=note_list_voice_two, continuous=False, count=1)
new_note_list_voice_two = non_cyc_generator(r=40)

# NOTE + REST = TALEA VOICE TWO
note_and_rest_voice_two = []
note_sublist_voice_two = []
random.seed(4)
N = random.randrange(4)+1
for n in range(0, len(new_note_list_voice_two), N):
    random.seed(n+2)
    note_sublist_voice_two.append(new_note_list_voice_two[n:n+random.randrange(4)+1])
note_and_rest_voice_two = []
for rest, note_group in zip(rest_list, note_sublist_voice_two):
    note_and_rest_voice_two.append(-rest)
    for i, elem in enumerate(note_group):
        note_and_rest_voice_two.append(note_group[i])


note_list_voice_four = [2, 1, 1]
non_cyc_generator = evans.CyclicList(lst=note_list_voice_four, continuous=False, count=1)
new_note_list_voice_four = non_cyc_generator(r=40)

# NOTE + REST = TALEA VOICE FOUR
note_and_rest_voice_four = []
note_sublist_voice_four = []
random.seed(4)
N = random.randrange(4)+1
for n in range(0, len(new_note_list_voice_four), N):
    random.seed(n+2)
    note_sublist_voice_four.append(new_note_list_voice_four[n:n+random.randrange(4)+1])
note_and_rest_voice_four = []
for rest, note_group in zip(rest_list, note_sublist_voice_four):
    note_and_rest_voice_four.append(-rest)
    for i, elem in enumerate(note_group):
        note_and_rest_voice_four.append(note_group[i])
