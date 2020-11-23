import abjad


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
def ring_modulation(pitches, sum=True, chords=False):
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


# VOICE ONE
pitches_voice_one = abjad.pitch.PitchSegment(
    "c'' g' fs' cs' " +  # bell chord (lower notes)
    "b ds cs c b, a, gs, e, ef, c,"  # ring modulation chord
    )

# ORIGINAL CHORD
pitches = []
original_chord = abjad.pitch.PitchSegment(
    "cqs' f' gs' c'' e'' ftqs'' gqs''"
    + " gs'' b'' cs''' ctqs''' f''' fs''' ftqs'''  gs'''"
    )
pitches = ring_modulation(original_chord, sum=False)
pitches = [abjad.NamedPitch.from_hertz(_) for _ in pitches]
# abjad.show(abjad.pitch.PitchSegment(pitches))
num_pitches = [abjad.NamedPitch(_).number for _ in pitches]

# STAFFGROUP TO VERIFY THE NOTES IN ring_modulation
G_staff = abjad.Staff()
F_staff = abjad.Staff()
notes_range = abjad.pitch.PitchRange("[C4, +inf]")
for note in pitches:
    test = note in notes_range
    if test is True:
        # note = abjad.Note(note, (1, 1))
        G_staff.append(abjad.Note.from_pitch_and_duration(note, (1, 1)))
    else:
        # note = abjad.Leaf(note, (1, 1))
        F_staff.append(abjad.Note.from_pitch_and_duration(note, (1, 1)))
abjad.attach(abjad.Clef("treble^8"), G_staff[0])
abjad.attach(abjad.Clef("bass_8"), F_staff[0])
staff = abjad.StaffGroup([G_staff, F_staff], lilypond_type="PianoStaff")
# abjad.f(staff)

# NO MICROTONAL
for item, i in zip(num_pitches, range(len(num_pitches))):
    if isinstance(item, float):
        item = item - 0.5
        num_pitches[i] = item

# num_pitches.sort()
# maker = abjad.LeafMaker()
# num_pitches_notes = maker(num_pitches, (1, 1))
# num_pitches_notes = abjad.Staff(num_pitches_notes)
# num_pitches_score = abjad.LilyPondFile.new(music=num_pitches_notes)
# abjad.f(num_pitches_score)

pitch_range = abjad.PitchRange("[C2, G7]")
# abjad.show(pitch_range)
pitches = []
for pitch in num_pitches:
    test = pitch in pitch_range
    if test is True:
        pitches.append(pitch)
    else:
        pass

pitches = abjad.pitch.PitchSegment(pitches)

# VOICE FOUR
pitches_voice_four = pitches.retrograde()
pitches_voice_four = pitches_voice_four.rotate(n=15)


# pitches_voice_four = pitches_voice_four[15:]
# abjad.show(pitches_voice_four)

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
