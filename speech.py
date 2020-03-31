import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
second = 30
print('encoding...')
myrecording = sd.rec(int(second * fs), samplerate = fs, channels =2)
sd.wait()
write('output.wav',fs,myrecording)
# importing libraries 
import speech_recognition as sr 
  
import os 
  
from pydub import AudioSegment 
from pydub.silence import split_on_silence 
  

def silence_based_conversion(path = "alice-medium.wav"): 
  
  
    song = AudioSegment.from_wav(path) 
  
    
    fh = open("recognized.txt", "w+") 
          
     
    
    chunks = split_on_silence(song, 
        
        min_silence_len = 500, 
  
        
        silence_thresh = -16
    ) 
  
   
    try: 
        os.mkdir('audio_ha') 
    except(FileExistsError): 
        pass
  
    
    os.chdir('audio_ha') 
  
    i = 0

    for chunk in chunks: 
              
        
        chunk_silent = AudioSegment.silent(duration = 10) 
  
        
        audio_chunk = chunk_silent + chunk + chunk_silent 
  
        
        print("saving ha{0}.wav".format(i)) 
        
        audio_chunk.export("./ha{0}.wav".format(i), bitrate ='192k', format ="wav") 
  
       
        filename = 'ha'+str(i)+'.wav'
  
        print("Processing ha "+str(i)) 
  
       
        file = filename 
  
       
        r = sr.Recognizer() 
  
      
        with sr.AudioFile(file) as source: 
            
            r.adjust_for_ambient_noise(source) 
            audio_listened = r.listen(source) 
  
        try: 
            
            rec = r.recognize_google(audio_listened) 
            
            fh.write(rec+". ") 
  
        
        except sr.UnknownValueError: 
            print("Could not understand audio") 
  
        except sr.RequestError as e: 
            print("Could not request results.") 
  
        i += 1
  
    os.chdir('..') 
  
  
if __name__ == '__main__': 
          
    print('Enter the audio file path') 
  
    path = input() 
  
    silence_based_conversion(path) 

