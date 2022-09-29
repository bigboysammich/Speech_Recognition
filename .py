import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

while True:
    print("Getting ambient noise levels")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("Say something!")
    while True:
        with m as source: audio = r.listen(source)
        print("Processing")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            print("User said: {}".format(value))

            if str(value) == "up":
                print("Input Successful")

            elif str(value) =="down":
                print("Input Successful")

            else:
                print("Invalid Input")

        except sr.UnknownValueError:
            print("Unknown input or could not hear")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
if KeyboardInterrupt:
        pass
