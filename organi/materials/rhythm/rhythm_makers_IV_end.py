import abjad
import abjadext.rmakers as rmakers
import random

# NOTE LIST VOICE FOUR SEGMENT IV END
# 4 _ _ _ 1 4 _ _ _ 1 4 _ _ _ 1 4 _ _ _ 1
#       3 _ _ 2 _ 3 _ _ 2 _
#           2 _ 2 _ 2 _ 2 _ 2      


# 4 _ _ _ 4 _ \ _ _ 1 3 _ _ \ 1 3 _ _ 1 2 _ 1 2 _ 1 1
# 1 2 _ 1 2 _ \ 1 3 _ _ 1 3 \ _ _ 1 2 _ 1 2 _ 1 1
# 2 _ 3 _ _ 4 \ _ _ _ 1 3 _ \ _ 1 2 _ 1 2 _ 1 1

# TALEA RHYTHM MAKER
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))
rhythm_maker_voice_two = rmakers.stack(
    rmakers.talea(
        [4, 3, 1, 3, 1, 3, 1, 2, 1, 2, 1, 1],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )

rhythm_maker_voice_three = rmakers.stack(
    rmakers.talea(
        [1, 2, 1, 2, 1, 3, 1, 3, 1, 2, 1, 2, 1, 1],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )
    
rhythm_maker_voice_four = rmakers.stack(
    rmakers.talea(
        [2, 3, 4, 1, 3, 1, 2, 1, 2, 1, 1],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )
