import speech_recognition as sr


class SpeechService:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8

    def listen(self):

        with sr.Microphone() as source:

            print("NOVA: Listening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.7
            )

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

            except sr.WaitTimeoutError:

                return None

        print("NOVA: Processing...")

        try:

            text = self.recognizer.recognize_google(
                audio
            )

            return text

        except sr.UnknownValueError:

            return None

        except sr.RequestError as error:

            print(
                f"Speech recognition service error: {error}"
            )

            return None