#!/usr/local/bin/python3.7
# -*- encoding: utf-8 -*-

import os
import abjad
from organi.tools import SegmentMaker
from organi.materials.pitches import pitches_IV_end as pitches
from organi.materials.rhythm import rhythm_makers_IV_end as rhythm
from organi.materials.indicators import post_process_IV_end as indicators

# SEGMENT 4 FINAL PART

time_signatures = [(6, 8)]*4

durations_voice_two = [(6, 8)]*4
durations_voice_three = [(6, 8)]*4
durations_voice_four = [(6, 8)]*4

includes = ['../../stylesheets/segment_ii_stylesheet.ily']

segment_maker = SegmentMaker(
    time_signatures=time_signatures,

    post_process_staffgroup=indicators.post_process_staffgroup,
    
    post_process_voice_one=indicators.post_process_voice_one,
    
    durations_voice_two=durations_voice_two,
    rhythm_maker_voice_two=rhythm.rhythm_maker_voice_two,
    pitches_voice_two=pitches.pitches_voice_two,
    post_process_voice_two=indicators.post_process_voice_two,

    durations_voice_three=durations_voice_three,
    rhythm_maker_voice_three=rhythm.rhythm_maker_voice_three,
    pitches_voice_three=pitches.pitches_voice_three,
    post_process_voice_three=indicators.post_process_voice_three,

    durations_voice_four=durations_voice_four,
    rhythm_maker_voice_four=rhythm.rhythm_maker_voice_four,
    pitches_voice_four=pitches.pitches_voice_four,
    post_process_voice_four=indicators.post_process_voice_four,
    post_process_electronics=indicators.post_process_electronics,
    
    make_measures_pitched=True,

    includes=includes,
    collect=True,
    )

if __name__ == '__main__':
    lilypond_file = segment_maker.run()
    illustration_path = os.path.join(
        os.path.dirname(__file__),
        'Illustration.pdf',
        )
    abjad.persist(lilypond_file).as_pdf(illustration_path)
    abjad.system.IOManager.open_file(illustration_path)
