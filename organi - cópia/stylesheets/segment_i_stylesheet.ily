\version "2.21.0"
\include "/Users/Davi/github/organi/organi/stylesheets/box.ily"
#(set-default-paper-size "letter" 'portrait)
#(set-global-staff-size 12)

\header {
    tagline = ##f
    title = ##f
    subtitle = ##f
    composer = ##f
}

\paper {
  #(set-paper-size "a4")
system-system-spacing = #'((basic-distance . 20)
       (minimum-distance . 1)
       (padding . 10)
       (stretchability . 1))
  top-margin = 12
  left-margin = 16
  right-margin = 12
  bottom-margin = 8
}

\layout {
  \accidentalStyle piano-cautionary
  \context {
    \Global
    \grobdescriptions #all-grob-descriptions
  }
  \context {
    \Voice
    \consists \musicBoxerEngraver % for spans
    \consists \boxEngraver
    %   default settings:
    \override MusicBoxer.layer = -10
    \override Box.layer = -10
    \once \override Box.acknowledge-script-interface = ##f
    \once \override Box.acknowledge-finger-interface = ##f
    \once \override MusicBoxer.acknowledge-script-interface = ##f
    \once \override MusicBoxer.acknowledge-finger-interface = ##f

    %\override MusicBoxer.outside-staff-priority = #10000
    % \override Box.outside-staff-priority = #10000
  }
  \context{
    \Staff
    \numericTimeSignature

    \override Tie.details = #'((ratio . 0.333)
  (center-staff-line-clearance . 0.6)
  (tip-staff-line-clearance . 0.45)
  (note-head-gap . 1)
  (stem-gap . 0.35)
  (height-limit . 1.0)
  (horizontal-distance-penalty-factor . 10)
  (same-dir-as-stem-penalty . 8)
  (min-length-penalty-factor . 26)
  (tie-tie-collision-distance . 0.45)
  (tie-tie-collision-penalty . 25.0)
  (intra-space-threshold . 1.25)
  (outer-tie-vertical-distance-symmetry-penalty-factor . 10)
  (outer-tie-length-symmetry-penalty-factor . 10)
  (vertical-distance-penalty-factor . 7)
  (outer-tie-vertical-gap . 0.25)
  (multi-tie-region-size . 3)
  (single-tie-region-size . 4)
  (between-length-limit . 1.0))
  }
  \context {
    \Score

    \override BarLine.X-extent = #'(0 . 0)
		\override BarLine.bar-extent = #'(-2 . 2)
		\override BarLine.hair-thickness = #0.9
		\override BarLine.thick-thickness = #8
		%\override BarLine.stencil = ##f

    \override Beam.breakable = ##t
		\override Beam.concaveness = #10000
		\override Beam.beam-thickness = #0.6
    \override Beam.length-fraction = #1.3

    \override Clef.layer = -1
		\override Clef.whiteout-style = #'outline
  	\override Clef.whiteout = 1
		%{ \override Clef.X-extent = #'(0 . 0) %}
		\override DynamicText.font-size = #-2
		\override DynamicLineSpanner.staff-padding = 4.5
        %{ \override DynamicLineSpanner.Y-extent = #'(-1.5 . 1.5) %}
		%{ \override Hairpin.bound-padding = #1.5 %is this necessary? %}
		\override Glissando.breakable = ##t
		%{ \override Glissando.thickness = #2 %}
		\override Glissando.thickness = #1.8
		\override Stem.thickness = #0.5
    \override Staff.thickness = #0.5

    %\override MetronomeMark.font-size = 1.2
    \override MetronomeMark.outside-staff-padding = #3

    \override TextSpanner.outside-staff-padding = #3

    \override RehearsalMark.padding = #'10

    \override SpacingSpanner.strict-grace-spacing = ##t
    \override SpacingSpanner.strict-note-spacing = ##t
    \override SpacingSpanner.uniform-stretching = ##t

    %\override StaffGrouper.staff-staff-spacing = #'((basic-distance . 23) (minimum-distance . 23) (padding . 8))

    \override Stem.stemlet-length = #1.15
		\override StemTremolo.slope = #0.3
		%{ \override StemTremolo.shape = #'rectangle %}
		\override StemTremolo.shape = #'beam-like
		%{ \override StemTremolo.flag-count = #3 %}
		\override StemTremolo.beam-thickness = #0.3

    \override TupletBracket.bracket-visibility = ##t
    \override TupletBracket.minimum-length = #3
    \override TupletBracket.padding = #2
		%{ \override TupletBracket.staff-padding = #1.5 %}
		\override TupletBracket.staff-padding = #2
    \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
		\override TupletBracket.direction = #down
		\override TupletNumber.font-size = #1.5
    \override TupletNumber.text = #tuplet-number::calc-fraction-text
		autoBeaming = ##f
		%{ subdivideBeams = ##t %}
		proportionalNotationDuration = #(ly:make-moment 1 30)
        tupletFullLength = ##t
  }
}
