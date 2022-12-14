import os
import random
import time
import mido
from pythonosc import udp_client


class ReflectionRecreation():
    def __init__(self):
        self.IP = "127.0.0.1"
        self.PORT_TO_MAX = 1001
        self.client = udp_client.SimpleUDPClient(self.IP, self.PORT_TO_MAX)
        self.MIDI_EDIT_ACTIONS = ['no_change','shift_third', 'shift_octave']
        self.EDIT_PROBS  = [0.45, 0.14, 0.41]
        self.MIDI_FILE_NAMES=[i for i in range(1,10+1)]
        self.FILE_SELECTION_PROBS = [1/len(self.MIDI_FILE_NAMES) for i in range(len(self.MIDI_FILE_NAMES))]
        self.current_midi_note = 0


    def play(self):
        while(True):
            try:
                midi_file_selected = random.choices(self.MIDI_FILE_NAMES, self.FILE_SELECTION_PROBS)[0]
                print("-----------------------------------------------------------------------")
                print(f"Using file: {midi_file_selected}.mid")
                midi_data = mido.MidiFile(os.path.join(os.path.dirname(__file__),f'{midi_file_selected}.mid'))
                for msg in midi_data:
                    if msg.is_meta:
                        continue
                    if msg.type == 'note_off':
                        time.sleep(msg.time)
                        print(f"Note duration from file: {msg.time} seconds")
                        self.send_note(self.current_midi_note, 0)
                        continue
                    sleep_dur = random.uniform(0.1, 3)
                    print(f"Adding a rest for {sleep_dur} seconds")
                    time.sleep(sleep_dur)
                    self.current_midi_note = self.process_note(msg.note)
                    self.send_note(self.current_midi_note, 1)
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                break



    def send_note(self, midi_note, note_type):
        self.client.send_message('type', note_type)
        self.client.send_message('note', midi_note)
        print(f'Sending note: {midi_note} and type: {note_type}')
        return

    def process_note(self, midi_note):
        # Select a random edit action
        edit_action = random.choices(self.MIDI_EDIT_ACTIONS, self.EDIT_PROBS)[0]
        if edit_action == 'shift_third':
            return self.shift_third(midi_note)
        elif edit_action == 'shift_octave':
            return self.shift_octave(midi_note)
        else:
            return midi_note

    def shift_third(self, midi_note, mode='major'):
        return midi_note - (4 if mode == 'major' else 3)

    def shift_octave(self, midi_note):
        return midi_note-12



if __name__=='__main__':
    reflection_recreation = ReflectionRecreation()
    reflection_recreation.play()
            
