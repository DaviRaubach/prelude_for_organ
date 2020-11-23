# -*- encoding: utf-8 -*-
import os
import abjad
from organi.tools import SegmentMaker
from organi.materials.pitches import pitches_IV as pitches
from organi.materials.rhythm import rhythm_makers_IV as rhythm
from organi.materials.indicators import post_process_IV as indicators


time_signatures = [(6, 8)]*15

durations_voice_two = [(6, 8)]*14
durations_voice_four = [(6, 8)]*14

durations_voice_five = [(6, 8)]*12

initial_rest_voice_four = r"r4."
initial_rest_voice_five = r"s2."


includes = ['../../stylesheets/segment_ii_stylesheet.ily']

segment_maker = SegmentMaker(
    time_signatures=time_signatures,

    post_process_staffgroup=indicators.post_process_staffgroup,

    durations_voice_two=durations_voice_two,
    rhythm_maker_voice_two=rhythm.rhythm_maker_voice_two,
    pitches_voice_two=pitches.pitches_voice_two,
    post_process_voice_two=indicators.post_process_voice_two,


    durations_voice_four=durations_voice_four,
    rhythm_maker_voice_four=rhythm.rhythm_maker_voice_four,
    pitches_voice_four=pitches.pitches_voice_four,
    post_process_voice_four=indicators.post_process_voice_four,
    initial_rest_voice_four=initial_rest_voice_four,

    durations_voice_five=durations_voice_five,
    rhythm_maker_voice_five=rhythm.rhythm_maker_voice_five,
    pitches_voice_five=pitches.pitches_voice_five,
    initial_rest_voice_five=initial_rest_voice_five,
    rest_interval_voice_five="s1*3",
    make_those_chords_voice_five=True,
    post_process_voice_five=indicators.post_process_voice_five,

    includes=includes,
    collect=True,
    )

if __name__ == '__main__':
    lilypond_file, _ = segment_maker()
    illustration_path = os.path.join(
        os.path.dirname(__file__),
        'Illustration.pdf',
        )
    abjad.persist(lilypond_file).as_pdf(illustration_path)
    abjad.system.IOManager.open_file(illustration_path)
