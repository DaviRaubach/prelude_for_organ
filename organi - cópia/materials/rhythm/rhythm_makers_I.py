import abjad
import abjadext.rmakers as rmakers

selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))

rhythm_maker_voice_one = rmakers.stack(
    rmakers.talea(
        [3, 2, 1],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

rhythm_maker_voice_two = rmakers.stack(
    rmakers.talea(
        [3, 1, 2],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

rhythm_maker_voice_three = rmakers.stack(
    rmakers.talea(
        [1, 2, 3],  # counts
        8,  # denominator
        ),
    rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )
    # 3 _ _ 2 _ 1 3 _ _ 2 _ 1 3 _ _ 2 _ 1
    #         3 _ _ 1 2 _


rhythm_maker_voice_four = rmakers.stack(
    rmakers.talea(
        [3, 1, 2],  # counts
        8,  # denominator
        ),
    #rmakers.beam(),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )

initial_rest_voice_one = None
initial_rest_voice_two = r"r8"
initial_rest_voice_three = r"r2"
