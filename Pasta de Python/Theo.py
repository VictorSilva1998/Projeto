import pyttsx3

voz = pyttsx3.init()
vozes = voz.getProperty ("voices")
voz.setProperty("voice", vozes[0].id)
texto = "Meu nome é Victor. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10."
voz.say (texto)
voz.runAndWait()