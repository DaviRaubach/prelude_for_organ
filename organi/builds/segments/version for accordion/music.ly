\version "2.23.3"
\language "english"
#(set-global-staff-size 13)

#(ly:set-option 'relative-includes #t)  
\include "stylesheet.ily"



\layout {
  \context {
    \Score
    \denies "Electronic_Staff"
    markFormatter = #format-mark-box-alphabet
    \override StaffGrouper.staff-staff-spacing =
    #'((basic-distance . 2)
      (minimum-distance . 11)
      (padding . 1)
      (stretchability . 9))
    
     \override StaffGrouper.staffgroup-staff-spacing =
    #'((basic-distance . 15)
      (minimum-distance . 1)
      (padding . 1)
      (stretchability . 15))
  }
}

\paper {
  top-margin = 12
  bottom-margin = 12
  max-systems-per-page = 6
}

\score {
    \include "segments.ily"
    \layout { }
  \midi { }
}