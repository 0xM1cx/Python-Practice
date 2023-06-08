from pyttsx3 import init

engine = init()
def main(eng):
    # words = "Nigger"
    # eng.say(words)
    # eng.runAndWait()


    vol = eng.getProperty('volume')
    print(vol)
    eng.setProperty('volume', 2.0)

    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say('I see a Nigger')
        engine.save_to_file('I see a Nigger' , 'test.mp3')
    engine.runAndWait()


main(engine)