# -*- encoding: utf-8 -*-
import os
import abjad
import organi.materials.pitches.pitches_V as pitches_V

pitches = pitches_V.staff_group

if __name__ == '__main__':
    illustration_path = os.path.join(
        os.path.dirname(__file__),
        'illustration.pdf',
        )
    abjad.persist(pitches).as_pdf(illustration_path)
    abjad.system.IOManager.open_file(illustration_path)
