# CONCATENATE VOICES 1 2 3

        if self.concatenate is True:
            one = abjad.Container()
            one.extend(rh_voice_one_measures)
            # print(one)
            # self._rewrite_meter(one, self.time_signatures)
            two = abjad.Container(rh_voice_two_measures)
            # self._rewrite_meter(two, self.time_signatures)
            three = abjad.Container(rh_voice_three_measures)
            # self._rewrite_meter(three, self.time_signatures)
            newVoice = abjad.Voice(
                [one, two, three],
                simultaneous=True)
            voice_one = score['RH_Voice_One']
            # abjad.mutate(voice_one).replace(newVoice)
            voice_one.extend([newVoice])
            # self._rewrite_meter(voice_one, self.time_signatures)
