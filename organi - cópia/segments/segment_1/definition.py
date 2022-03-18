#!/usr/local/bin/python3.7
# -*- encoding: utf-8 -*-
import os
import abjad
from organi.tools import SegmentMaker
from organi.materials.pitches import pitches_I as pitches
from organi.materials.rhythm import rhythm_makers_I as rhythm
from organi.materials.indicators import post_process_I as indicators

# SEGMENT 1

rest_organ = abjad.Rest("r1")
abjad.attach(abjad.Fermata("verylongfermata"), rest_organ)

durations_voice_one = [(6, 8)]*8
durations_voice_four = [(6, 8)]*8


time_signatures = (4, 4), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8), (6, 8)

includes = ['../../stylesheets/stylesheet.ily']

segment_maker = SegmentMaker(
    time_signatures=time_signatures,

    durations_voice_one=durations_voice_one,
    rhythm_maker_voice_one=rhythm.rhythm_maker_voice_one,
    pitches_voice_one=pitches.chord_voice_one,
    initial_rest_voice_one=rest_organ,
    make_those_chords_voice_one=True,
    post_process_voice_one=indicators.post_process_voice_one,

    durations_voice_four=durations_voice_four,
    rhythm_maker_voice_four=rhythm.rhythm_maker_voice_four,
    pitches_voice_four=pitches.chord_voice_four,
    initial_rest_voice_four=[abjad.Rest((4, 4)), abjad.Rest((2, 4))],
    make_those_chords_voice_four=True,
    post_process_voice_four=indicators.post_process_voice_four,

    # chords_voice_one_elec=None,
    post_process_electronics=indicators.post_process_electronics,

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
# score = segment_maker.run()
# abjad.show(score)
#
# voice_one = score['RH_Voice_One']
# global_staff = score['Global_Context']
#
# # print(score['RH_Voice_One'][-9:])
# del voice_one[-9:]
# # abjad.f(score['RH_Voice_One'])
#
# voice_one[-1].written_duration = (1, 2)
# abjad.attach(abjad.Fermata(), voice_one[-1])
#
# # print(score['LH_Voice_Four'][-3:])
# del score['LH_Voice_Four'][-3:]
# # abjad.f(score['LH_Voice_Four'])
# score['LH_Voice_Four'][-1].written_duration = (1, 2)
# abjad.attach(abjad.Fermata(), score['LH_Voice_Four'][-1])
#
# abjad.attach(
#     abjad.Markup("Open Flutes 8'", direction=abjad.Up),
#     voice_one[0])
# abjad.attach(
#     abjad.MetronomeMark((1, 4), (22, 45), "Estatic"), voice_one[0])
#
# accel_text_span = abjad.LilyPondLiteral(
#     r'\override TextSpanner.bound-details.left.text = "accelerando poco a poco"' + " " +
#     r"\override TextSpanner.style = #'dashed-line" + " " +
#     r"\startTextSpan")
#
# abjad.attach(accel_text_span, voice_one[3])
# stop_accel_text_span = abjad.StopTextSpan(command=r"\stopTextSpan")
#
# abjad.attach(stop_accel_text_span, voice_one[8])
#
# # add midi instruments
# # organ_group = score['Piano_Staff']
# # abjad.setting(organ_group).midi_instrument = abjad.scheme.Scheme(
# #     'Flute', force_quotes=True)
# # abjad.attach(abjad.instruments.Flute(), organ_group[0][0][0])
# # abjad.show(score)
# # abjad.f(score)
# # lilypond_file = segment_maker.compile(score, includes)
# lilypond_file = abjad.LilyPondFile.new(
#     score,
#     includes=includes,
#     )
#
# # abjad.show(lilypond_file)
# lilypond_file.includes
# # midi_block = abjad.Block(name="midi")
# # layout_block = abjad.Block(name="layout")
# # lilypond_file["score"].items.append(layout_block)
# # lilypond_file["score"].items.append(midi_block)
#
# if __name__ == '__main__':
#     lilypond_file, _ = segment_maker()
#     illustration_path = os.path.join(
#         os.path.dirname(__file__),
#         'Illustration.pdf',
#         )
#     abjad.persist(lilypond_file).as_pdf(illustration_path)
#     abjad.system.IOManager.open_file(illustration_path)
# else:
#     illustration_path = os.path.join(
#         os.path.dirname(__file__),
#         'Illustration.pdf',
#         )
#     abjad.persist(lilypond_file).as_pdf("./segments/segment_i/Illustration.pdf")
#     abjad.system.IOManager.open_file("./segments/segment_i/Illustration.pdf")
