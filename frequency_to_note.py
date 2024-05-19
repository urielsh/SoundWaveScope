import math

def frequency_to_note(frequency):
    try:
        A4_frequency = 440
        SEMITONE_RATIO = 2 ** (1/12)
        NOTES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

        semitones_from_A4 = 12*math.log2(frequency / A4_frequency)
        rounded_semitones = round(semitones_from_A4)
        octave = 4 + (rounded_semitones + 9) // 12
        note_index = (rounded_semitones + 9) % 12 
        note_name = NOTES[note_index]

        return f"{note_name}{octave}"
    except Exception as e:
        print (f"Notes calculation failed: {e}")
        return None
    
print(frequency_to_note(440))

