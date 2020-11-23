import abjad
import abjadext.rmakers as rmakers
import random
import organi


voz = abjad.Voice()
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))
rhythm = rmakers.stack(
    rmakers.talea(
        [7, 7, 7, 7],  # counts
        8,  # denominator
        ),
    # rmakers.beam(),
    rmakers.denominator((1, 8)),
    rmakers.extract_trivial(),
    # rmakers.tie(selector),
    )
divisions = [(4, 8)]*7
measures = rhythm(divisions)
voz = abjad.Voice(measures) # NEED TO PUT IN A CONTAINER TO SEPARATE WELL THE LOGICAL TIES
logical_ties = abjad.select(voz).leaves().logical_ties(pitched=True)
logical_ties



voz_time = abjad.Voice("s2 s2 s2 s2 s2 s2 s2 s2 s2 s2 s2 s2 s2 s2 s4 s1")
abjad.Staff(voz, voz_time)

time_signatures = []
for item in divisions:
    time_signatures.append(abjad.TimeSignature(item))

abjad.attach(time_signatures[0])
abjad.mutate(measures[:]).split(divisions, cyclic=True)


abjad.show(measures)
selector = abjad.select(measures).leaves()
selector
select = selector.group_by_measure()
for time, measure in zip(time_signatures, measures):
    abjad.mutate(measure).rewrite_meter(time, maximum_dot_count=2,)




score = organi.ScoreTemplate()
score = score()
this = score['Piano_Staff'][0][1]
this.append("c,,4")
abjad.attach(abjad.TimeSignature((3, 4)), this[0])

staff_change = abjad.StaffChange(score['LH_Staff'])
abjad.attach(staff_change, rh_staff[i])
abjad.f(this)



staff_group = abjad.StaffGroup()
staff1 = abjad.Staff("e4 f g f e")
staff2 = abjad.Staff("c4 d e d c")
staff_group.extend([staff1, staff2])
selection = abjad.select(staff_group[1]).leaves().logical_ties(pitched=True)
length = len(selection)
for lo, i in zip(selection, range(length)):
    pass


def _make(music):
    del music[-1]
    abjad.attach(abjad.Fermata(), music[-1])
    return music




one = [abjad.Note("gs'''4."), abjad.Note("g'''4"), abjad.Note("fs'''8")]
one = abjad.Container(one)
two = [abjad.Note("gs'8"), abjad.Note("g'4."), abjad.Note("fs'4")]
two = abjad.Container(two)
voice = abjad.Voice([one, two], simultaneous=True)

voice2 = abjad.Voice()
voice2.extend([voice])

abjad.show(voice2)

pitches = abjad.pitch.PitchSegment("c'' e'' g'' c''' e''' g'''")
pitches = pitches.retrograde()
pitches_num = []
for pitch in pitches:
    pitches_num.append(abjad.NamedPitch(pitch).number)


divisions = [(6, 8)]*4
selector = abjad.select().tuplets()[:-1]
selector = selector.map(abjad.select().note(-1))
rhythm_maker1 = rmakers.stack(
    rmakers.talea(
        [3, 2, 1],  # counts
        8,  # denominator
        ),
    rmakers.beam(),
    rmakers.extract_trivial(),
    rmakers.tie(selector),
    )

rhythm = rhythm_maker1(divisions)
time = abjad.TimeSignature((6, 8))
abjad.attach(time, rhythm[0])

voice = abjad.Voice("d'4. d'8 ~ <d' f'>4")
leaves = abjad.select(voice).leaves().logical_ties()
leaves
for item in leaves[1][1].written_pitches:
    if item == leaves[0][0].written_pitch:
        print("is")

chords = []

for x, y, z in zip(pitches, pitches[1:], pitches[2:]):
    tie = abjad.Tie()
    for i, leave in zip(range(5), leaves):
        i = i+1
        if i == 1:
            note = abjad.Note(x, (1, 4))
            note.written_duration = leave.written_duration
            abjad.attach(tie, note)
            chords.append(note)
        if i == 2:
            chord = abjad.Chord((x, y), (1, 4))
            chord.written_duration = leave.written_duration
            abjad.attach(tie, chord)
            chords.append(chord)
        if i == 3:
            chord = abjad.Chord((x, y, z), (1, 4))
            chord.written_duration = leave.written_duration
            abjad.attach(tie, chord)
            chords.append(chord)
        if i == 4:
            chord = abjad.Chord((y, z), (1, 4))
            chord.written_duration = leave.written_duration
            abjad.attach(tie, chord)
            chords.append(chord)
        if i == 5:
            note = abjad.Note(z, (1, 4))
            note.written_duration = leave.written_duration
            abjad.attach(tie, note)
            chords.append(note)
time = abjad.TimeSignature((6, 8))
abjad.attach(time, chords[0])
voice = abjad.Voice(chords, name="Voice")
staff = abjad.Staff([voice])
abjad.show(staff)

list1 = [1, 2]
list2 = [2, 1, 3]

set(list1) & set(list2)

time_signature = [(3, 8)]
abjad_time_signature = abjad.TimeSignature((3, 8))
voice = abjad.Staff()
chord = abjad.Chord("c e", (1, 4))
chord2 = abjad.Chord("c e g", (1, 4))
voice.append(chord)
voice.append(chord2)
abjad.attach(abjad.Tie(), voice[0])
abjad.f(voice)
abjad.mutate(voice[:]).split(time_signature, cyclic=True)
abjad.select(voice).leaves().group_by_measure()
abjad.mutate(voice).rewrite_meter(abjad_time_signature)
abjad.f(voice)

chord = abjad.Chord("c e ", (1, 8))
lit = r"d2 r2 c'''2"
voice = abjad.Voice()
voice.append(chord)
chord2 = abjad.Chord("c e ", (1, 8))
voice.append(chord2)
voice


def make_time_signatures(time_signature, times):
    time_signatures = []
    for i in range(times):
        time_signatures.append(time_signature)
    return time_signatures

time_signatures = make_time_signatures((4,4), 10)
time_signatures


list = []
one = (4, 4)
two = (6, 8)
three = [two] * 4
list.append(one)
list.extract
print(three)

itens = 0, 1, 2, 0
for item in itens:
    if item == 0:
        random.seed(10)
        print(random.randint(1, 50))
        random.seed(30)
        print(random.randint(1, 50))
    else:
        random.seed(3)
        print(random.randint(1, 50))
