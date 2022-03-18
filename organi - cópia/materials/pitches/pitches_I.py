import abjad
# import abjadext.rmakers as rmakers
# CHORD ZERO
chord_zero_organ = abjad.Chord(
    "<cs' fs' g' c'' e'' g'' af''>1"
)

# CHORD ORIGINAL
original_chord = abjad.pitch.PitchSegment(
    "cqs' f' gs' c'' e'' ftqs'' gqs''"
    + " gs'' b'' cs''' ctqs''' f''' fs''' ftqs'''  gs'''"
    )

original_chord_semitones = "cs' fs' g' c'' e'' g'' af'' b'' cs''' d''' f''' fs''' g'''  af'''"

# VOICE ONE
chord_voice_one = abjad.pitch.PitchSegment(
    "cs' fs' g' c'' e'' g'' af'' b'' cs''' d''' f''' fs''' g'''  af'''"
)
chord_voice_one = chord_voice_one.retrograde()

chord_voice_one = abjad.pitch.PitchSegment(
    "af''' g''' fs''' " +
    "f''' d''' cs''' " +
    "b'' af'' g'' " +
    "e'' c'' g' " +
    "fs' cs' gs"
    )

# ###### TRANSPOSITION ###### #
# chord_voice_one = chord_voice_one.transpose(n=-12)


# print(chord_voice_one)
# VOICE FOUR
chord_voice_four = chord_voice_one.rotate(n=-4)
chord_voice_four = chord_voice_four[:-3]

# VOICE TWO
pitches_voice_two = abjad.pitch.PitchSegment(
    "f' af' c'' e'' fs'' g''"
    )
pitches_voice_two = abjad.pitch.PitchSegment.retrograde(pitches_voice_two)

# VOICE THREE
pitches_voice_three = abjad.pitch.PitchSegment(
    "f' af' c'' e'' fs'' g''"
    )
invert = abjad.Inversion()
pitches_voice_three = invert(pitches_voice_three)
pitches_voice_three = pitches_voice_three.transpose(n=12)

# pitches_voice_two_num = []
# for pitch in pitches_voice_one:
#    pitches_voice_two_num.append(abjad.NamedPitch(pitch).number)
# print(pitches_voice_one_num)
# [0.5, 5, 8, 12, 16, 18.5, 19.5, 20, 23, 25, 25.5, 29, 30, 30.5, 32]


# PITCHES IN HERTZ FOR ELECTRONIC EXPLORATION
original_chord.hertz
pitches_voice_one_hertz = [
    269.2917795270241,
    349.2282314330039,
    415.3046975799451,
    523.2511306011972,
    659.2551138257398,
    761.6721736854058,
    806.9635580201107,
    830.6093951598903,
    987.7666025122483,
    1108.7305239074883,
    1141.2188080928886,
    1396.9129257320155,
    1479.9776908465376,
    1523.3443473708119,
    1661.2187903197805]

# make clusters test ----------------------------------------------------------
# pitches = abjad.pitch.PitchSegment("cs' fs' g' c'' e'' g'' af''")
# pitches_num = []
# for pitch in pitches:
#     pitches_num.append(abjad.NamedPitch(pitch).number)
#
# chords = []
# for x, y, z in zip(pitches_num, pitches_num[1:], pitches_num[2:]):
#     chord_1 = (x)
#     chord_2 = (x, y)
#     chord_3 = (x, y, z)
#     chord_4 = (y, z)
#     chord_5 = (z)
#     chords.append(chord_1)
#     chords.append(chord_2)
#     chords.append(chord_3)
#     chords.append(chord_4)
#     chords.append(chord_5)
# chords
# chords_abjad = []
#
# for chord in chords:
#     for chords_ii in chords[:1]:
#         if isinstance(chord, int):
#             abjad_note = abjad.Note(chord, (1, 4))
#             chords_abjad.append(abjad_note)
#             if isinstance(chord_ii, tuple):
#                 set(chord).intersection(set(chord_ii))
#
#         if isinstance(chord, tuple):
#             abjad_chord = abjad.Chord(chord, abjad.Duration(1, 4))
#             chords_abjad.append(abjad_chord)
#
# for chord_ab in chords_abjad:
#     for chord_i, chord_ii in zip(chords, chords[1:]):
#         if isinstance(chord_i, int) and isinstance(chord_ii, tuple):
#             list = [chord_i]
#             same_note = set(list).intersection(set(chord_ii))
#             abjad.attach(abjad.Tie(), chord_ab)
#
# for chord_i, chord_ii in zip(chords, chords[1:]):
#         if isinstance(chord_i, int):
#             if chord_i not in chord_ii:
#                 print("chord_ii has not chord_i note")
#             else:
#                 print("chord_ii has chord_i note")
#                 # abjad.attach(abjad.Tie(), chord_ab)
#         if isinstance(chord_i, tuple):
#             pass# same_note = set(chord_i).intersection(set(chord_ii))
#             # abjad.attach(abjad.Tie(), chord_ab)
#
# stack = []
# stack = rmakers.stack(
#     rmakers.note(),
# )
# divisions = [(1, 4), (1, 4), (5, 8), (5, 8)]
# music = stack(divisions)
#
# music = abjad.Voice(music)
#
# leaves = abjad.select(music).leaves()
# leaves
# for leaf, chord in zip(leaves, chords):
#     if isinstance(chord, tuple):
#         new_leaf = abjad.Chord()
#         new_leaf.written_duration = leaf.written_duration
#         new_leaf.written_pitches = chord
#     else:
#         new_leaf = abjad.Note()
#         new_leaf.written_duration = leaf.written_duration
#         new_leaf.written_pitch = chord
#     abjad.mutate(leaf).replace(new_leaf)
#
# abjad.show(music)
