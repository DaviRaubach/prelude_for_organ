import abjad
import abjadext.rmakers as rmakers
import evans
import random

# THOSE CHORDS IN VOICE FIVE (once was one)
rhythm_maker_voice_five = rmakers.stack(
    rmakers.talea(
        [2, 1, 3],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

# MATERIAL FROM SEGMENT 2 AND 3
# REST LIST
rest_list = evans.e_dovan_cycle(
    n=2, iters=16, first=1, second=1, modulus=5)
rest_list.sort(reverse=True)

# NOTE LIST VOICE TWO
note_list_voice_two = [4, 1]
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

# NOTE LIST VOICE FOUR
# (3 ,8) delay
# 4 _ _ _ 1 4 _ _ _ 1 4 _ _ _ 1 4 _ _ _ 1
#       3 _ _ 1 1 3 _ _

note_list_voice_four = [3, 1, 1]
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

print(note_and_rest_voice_four)
# TALEA RHYTHM MAKER
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))
rhythm_maker_voice_two = rmakers.stack(
    rmakers.talea(
        note_and_rest_voice_two,  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )

rhythm_maker_voice_four = rmakers.stack(
    rmakers.talea(
        note_and_rest_voice_four,  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )
