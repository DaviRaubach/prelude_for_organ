# -*- encoding: utf-8 -*-
import os
import abjad
from organi.tools import SegmentMaker
from organi.materials.pitches import pitches_II as pitches
from organi.materials.rhythm import rhythm_makers_II as rhythm
from organi.materials.indicators import post_process_II as indicators


time_signatures = [(6, 8)]*12

durations_voice_one = [(6, 8)]*10
durations_voice_four = [(6, 8)]*12

rest_interval_voice_one = "r2"

initial_rest_voice_one = "r2"
initial_rest_voice_four = None

includes = ['../../stylesheets/segment_ii_stylesheet.ily']

segment_maker = SegmentMaker(
    time_signatures=time_signatures,

    post_process_staffgroup=indicators.post_process_staffgroup,

    durations_voice_one=durations_voice_one,
    rhythm_maker_voice_one=rhythm.rhythm_maker_voice_one,
    pitches_voice_one=pitches.chord_voice_one,
    rest_interval_voice_one=rest_interval_voice_one,
    # initial_rest_voice_one=rest_organ,
    make_those_chords_voice_one=True,
    post_process_voice_one=indicators.post_process_voice_one,

    durations_voice_four=durations_voice_four,
    rhythm_maker_voice_four=rhythm.rhythm_maker_voice_four,
    pitches_voice_four=pitches.pitches_voice_four,
    # legato_voice_four=True,
    post_process_voice_four=indicators.post_process_voice_four,

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
