import abjad
import random
from organi.tools.see_pitches import see_pitches

# RECURSES TO MODIFY PITCH SEGMENTS
# A C B D C E
def permut_thirds(pitches):
    pitch_list = []
    i = 0
    pitch_list.append(pitches[i])
    while i < len(pitches) - 2:
        i = i + 2
        note = pitches[i]
        pitch_list.append(note)
        i = i - 1
        note = pitches[i]
        pitch_list.append(note)
    return pitch_list


# FREQ_B - FREQ_A AND FREQ_B + FREQ_A
def ring_modulation(pitches, sum=True, chords=False, hertz=False):
    if hertz is True:
        pitches_in = pitches
    else:
        pitches_in = pitches.hertz
    
    pitches_out = []
    if sum is True and chords is False:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            pitches_out.append(new_pitch_A)
            pitches_out.append(pitch1)
            new_pitch_B = pitch1 + pitch2
            pitches_out.append(new_pitch_B)
    if sum is False and chords is False:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            pitches_out.append(new_pitch_A)
            new_pitch_B = pitch1 + pitch2
            pitches_out.append(new_pitch_B)
    if sum is True and chords is True:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            new_pitch_B = pitch1 + pitch2
            new_pitch_A = abjad.NamedPitch.from_hertz(new_pitch_A)
            new_pitch_B = abjad.NamedPitch.from_hertz(new_pitch_B)
            pitch1 = abjad.NamedPitch.from_hertz(pitch1)
            chord = abjad.Chord([new_pitch_A, pitch1, new_pitch_B], (1, 1))
            pitches_out.append(chord)
    if sum is False and chords is True:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            new_pitch_B = pitch1 + pitch2
            new_pitch_A = abjad.NamedPitch.from_hertz(new_pitch_A)
            new_pitch_B = abjad.NamedPitch.from_hertz(new_pitch_B)
            chord = abjad.Chord([new_pitch_A, new_pitch_B], (1, 1))
            print(chord)
            pitches_out.append(chord)
    return pitches_out


# ORIGINAL CHORD
pitches = []
original_chord = abjad.pitch.PitchSegment(
    "cqs' f' gs' c'' e'' ftqs'' gqs''"
    + " gs'' b'' cs''' ctqs''' f''' fs''' ftqs'''  gs'''"
    )
    
pitches = ring_modulation(original_chord, sum=True)
pitches = [abjad.NamedPitch.from_hertz(_) for _ in pitches]
num_pitches = [abjad.NamedPitch(_).number for _ in pitches]

# see_pitches(num_pitches)

# NO MICROTONAL
for item, i in zip(num_pitches, range(len(num_pitches))):
    if isinstance(item, float):
        item = item - 0.5
        num_pitches[i] = item

# see_pitches(num_pitches)

# THREE VOICES - THREE PITCH RANGES

pitches_low = []
pitches_middle = []
pitches_treble = []

low_range = abjad.pitch.PitchRange("[F3, B4]")
middle_range = abjad.pitch.PitchRange("[C5, B5]")
treble_range = abjad.pitch.PitchRange("[C6, G7]")

for note in num_pitches:
    test1 = note in low_range
    test2 = note in middle_range
    test3 = note in treble_range
    if test1 is True:
        pitches_low.append(note)
    if test2 is True:
        pitches_middle.append(note)
    if test3 is True:
        pitches_treble.append(note)


# see_all_pitches = pitches_low + [-20] + pitches_middle + [-20] + pitches_treble
del pitches_treble[0:3]

# DESISTI: pitches_low = original_chord_semitones do segment_1 e mais algumas do original chord + ring modulation abaixo

pitches_low = "f c' ef' e' c'' bf' b' c'' ef'' e'' bf''"



pitches_low = abjad.pitch.PitchSegment(pitches_low)
pitches_middle = abjad.pitch.PitchSegment(pitches_middle)
pitches_treble = abjad.pitch.PitchSegment(pitches_treble)



# VOICE TWO
pitches_voice_two = pitches_treble
print("pitches 2 =" + str(pitches_voice_two))

# VOICE THREE
pitches_voice_three = pitches_middle
print("pitches 3 =" + str(pitches_voice_three))

# VOICE FOUR
pitches_voice_four = pitches_low
print("pitches 4 =" + str(pitches_voice_four))

# PITCHES LOW PRECISA SER O ACORDE DO INÍCIO SEI LA
# TODO: COPIAR ACORDE DO INICIO PARA VOICE_FOUR

# ORIGINAL CHORD + RING MODULATION em ordem ascendente
# \new Voice
# {
#     gqf,,,4
#     c,,4
#     f,,4
#     fs,,4
#     c,4
#     eqf,4
#     e,4
#     af,4
#     a,4
#     b,4
#     cs4
#     cs4
#     ef4
#     bqs4
#     cqs'4
#     f'4
#     af'4
#     c''4
#     ef''4
#     e''4
#     gqf''4
#     gqf''4
#     gqs''4
#     af''4
#     bf''4
#     b''4
#     cs'''4
#     dqf'''4
#     d'''4
#     f'''4
#     f'''4
#     fs'''4
#     gqf'''4
#     g'''4
#     af'''4
#     aqs'''4
#     c''''4
#     cs''''4
#     ef''''4
#     fqs''''4
#     fs''''4
#     g''''4
# }
