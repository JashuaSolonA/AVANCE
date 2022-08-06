
import sounddevice as sd
import numpy as np
import threading 

class Chord_maker:
    def __init__(self):
        self.notes_dictionary = {"cromatic":{"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11},
                                    "alter":{"C#":1,"Db":1,"D#":3,"Eb":3,"F#":6,"Gb":6,"G#":8,
                                            "Ab":8,"A#":10,"Bb":10}}
        self.interval = {"2major":2,"3minor":3,"3major":4,"fourth":5,"4augm":6,"fifth":7,"5augm":8}
        
        self.triads = {"Maj":["3major","fifth"],
                        "m":["3minor","fifth"],
                        "sus2":["2major","fifth"],
                        "sus4":["fourth","fifth"],
                        "dim":["3minor","4augm"],
                        "aug":["3major","5augm"],
                        "+":["3major","5augm"]}

    def get_frecuency(self,note,octave):
        expo=(octave-4)*12+(note-10)
        return 440 * ((2**(1/12))**expo)
    
    def play(self,frequency,time,framerate=44100):
        t = np.linspace(0,time/1000,int(framerate*time/1000))
        wave = np.sin(2* np.pi * frequency * t)
        sd.play(wave,framerate)
        sd.wait()

    def play_chord(self,chord):
        threards=[]
        for note in chord:
            freq=self.get_frecuency(note,4)
            th=threading.Thread(target=lambda:self.play(freq,1000))
            th.start()
            threards.append(th)    
        
        for thread in threards:
            thread.join()
    
    def strip_chord(self,chord):
        if "#" in chord or "b" in chord:  #alter
            root, rest = chord[:2] , chord.split(chord[:2])[1]
            root=self.notes_dictionary['alter'][root]
        else: 
            root, rest = chord[0] , chord.split(chord[0])[1]
            root=self.notes_dictionary['cromatic'][root]
        return root, rest

    def third_and_fifth(self,rest):
        for i in self.triads.keys():
            if i in rest:
                return self.triads[rest]
            else:
                return self.triads["Maj"] 

    def get_chord(self,chord):
        root , rest = self.strip_chord(chord)
        triads = self.third_and_fifth(rest)
        return [root] + [(root + self.interval[x]) % 12 for x in triads]

if __name__ == "__main__":
   c= Chord_maker()
   c.get_chord("Dm","Cm")
  