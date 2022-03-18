# -*- encoding: utf-8 -*-
import os
import abjad
from organi.tools import SegmentMaker

# TIME SIGNATURES
time_signatures = [(4, 4)]

# ORGAN NOTATION
rest_organ = abjad.Rest("r1")
abjad.attach(abjad.Fermata("verylongfermata"), rest_organ)
rest_organ_voice_four = abjad.Rest("r1")

# CHORD ZERO ELECTRONICS
chord_zero_electronics = abjad.Chord(
    "<cqs' f' gs' c'' e'' ftqs'' gqs'' gs''" +
    " b'' cs''' ctqs''' f''' fs''' ftqs''' gs'''>1")

# laisses vibrer
laissez_vibrer = abjad.LaissezVibrer()
abjad.attach(laissez_vibrer, chord_zero_electronics)

# tempo mark
mark = abjad.MetronomeMark(None, None, "Statico")
abjad.attach(mark, chord_zero_electronics)

# fermata
abjad.attach(abjad.Fermata("verylongfermata"), chord_zero_electronics)

# remove includes to collect segments
includes = ['../../stylesheets/stylesheet.ily']

segment_maker = SegmentMaker(
    time_signatures=time_signatures,
    chords_voice_one_elec=chord_zero_electronics,
    initial_rest_voice_one=rest_organ,
    initial_rest_voice_four=rest_organ_voice_four,
    includes=includes,

    )

if __name__ == '__main__':
    lilypond_file, _ = segment_maker()
    illustration_path = os.path.join(
        os.path.dirname(__file__),
        'Illustration.pdf',
        )
    abjad.persist(lilypond_file).as_pdf(illustration_path)
    abjad.system.IOManager.open_file(illustration_path)
