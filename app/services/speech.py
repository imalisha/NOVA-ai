import speech_recognition as sr


class SpeechService:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8

    # =========================================================
    # NORMAL COMMAND LISTENING
    # =========================================================

    def listen(self):

        with sr.Microphone() as source:

            print("NOVA: Listening...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
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

        return self.recognize(audio)

    # =========================================================
    # SPEECH RECOGNITION
    # =========================================================

    def recognize(self, audio):

        try:

            text = self.recognizer.recognize_google(
                audio
            )

            print(
                f"NOVA: Recognized: {text}"
            )

            return text

        except sr.UnknownValueError:

            return None

        except sr.RequestError as error:

            print(
                f"NOVA: Speech recognition service error: {error}"
            )

            return None

    # =========================================================
    # WAKE WORD
    # =========================================================

    def listen_for_wake_word(self):

        with sr.Microphone() as source:

            print(
                "NOVA: Waiting for 'hello nova'..."
            )

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=3,
                    phrase_time_limit=4
                )

            except sr.WaitTimeoutError:

                return False

        text = self.recognize(audio)

        if not text:

            return False

        text = text.lower().strip()

        wake_words = [
            "hello nova",
            "hey nova",
            "hello, nova",
            "hey, nova",
            "nova"
        ]

        for wake_word in wake_words:

            if wake_word in text:

                print(
                    "NOVA: Wake word detected!"
                )

                return True

        return False