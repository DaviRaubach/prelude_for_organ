import abjad
import abjadext.rmakers as rmakers
import evans
import random

# THOSE CHORDS IN VOICE TWO
rhythm_maker_voice_one = rmakers.stack(
    rmakers.talea(
        [3, 2, 1],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

# NEW MATERIAL
# REST LIST
rest_list = evans.e_dovan_cycle(
    n=2, iters=16, first=1, second=1, modulus=8)
rest_list.sort(reverse=True)

# NOTE LIST
note_list = [4, 1]
non_cyc_generator = evans.CyclicList(lst=note_list, continuous=False, count=1)
new_note_list = non_cyc_generator(r=40)
new_note_list

# NOTE + REST = TALEA
note_and_rest = []
note_sublist = []
random.seed(4)
N = random.randrange(4)+1
for n in range(0, len(new_note_list), N):
    random.seed(n+2)
    print(random.randrange(4)+1)
    note_sublist.append(new_note_list[n:n+random.randrange(4)+1])
note_sublist
note_and_rest = []
for rest, note_group in zip(rest_list, note_sublist):
    note_and_rest.append(-rest)
    for i, elem in enumerate(note_group):
        note_and_rest.append(note_group[i])

# TALEA RHYTHM MAKER
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))
rhythm_maker_voice_four = rmakers.stack(
    rmakers.talea(
        note_and_rest,  # counts
        8,  # denominator
        ),
    rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )
