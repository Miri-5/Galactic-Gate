import speech_recognition

def speechtr():
    mikrofon = speech_recognition.Microphone()
    record = speech_recognition.Recognizer()
    with mikrofon as mik:
        record.adjust_for_ambient_noise(mik)
        voice = record.listen(mik)
        try:
            return record.recognize_google(voice,language = "tr-TR")
        except:
            return "voice tanınamadı, dediğini anlayamadım"



def speechen():
    mikrofon = speech_recognition.Microphone()
    record = speech_recognition.Recognizer()
    with mikrofon as mik:
        record.adjust_for_ambient_noise(mik)
        voice = record.listen(mik)
        try:
            return record.recognize_google(voice,language = "en-US")
        except:
            return "i don't understand"
        
def speechaz():
    mikrofon = speech_recognition.Microphone()
    record = speech_recognition.Recognizer()
    with mikrofon as mik:
        record.adjust_for_ambient_noise(mik)
        voice = record.listen(mik)
        try:
            return record.recognize_google(voice,language = "az-AZ")
        except:
            return "Səs tanınmadı"
        

if __name__== "__main__" :
    print("Dinlemeye başlayın.")
    print(speechen())

