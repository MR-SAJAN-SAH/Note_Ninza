import pyttsx3

class TextToSpeech:
    def __init__(self):
        """
        Initialize the text-to-speech engine.
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)  # Speed of speech (words per minute)
        self.engine.setProperty("volume", 1.0)  # Volume level (0.0 to 1.0)

    def play_summary(self, text):
        """
        Play the provided text as speech.
        :param text: Text to be spoken
        """
        if not text:
            print("No text provided for speech.")
            return

        # Queue the text for speech
        self.engine.say(text)
        print("Playing summary...")

        # Block until speech is complete
        self.engine.runAndWait()


# Example usage
if __name__ == "__main__":
    tts = TextToSpeech()
    tts.play_summary("This is a test summary.")