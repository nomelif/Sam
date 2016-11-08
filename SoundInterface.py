#!/usr/bin/python3

"""

This file defines Sam's interaction with the user.

"""

class InputDevice:

    """

    This class tells the main executable when the user does an action. It also allows capturing raw audio.

    """

    def __init__(self, onSpoken, onInterrupted):

        """

        * `onSpoken`: method to call when the user has finished uttering something. It is called with a string representation of the input.
        * `onInterrupted`: method to call when something using the microphone get's killed or Sam starts speaking while still waiting for user input.
        * `onNotUnderstood`: method to call when the speech to text fails to provide a string.

        """

        self.onSpoken = onSpoken
        self.onInterrupted = onInterrupted

    def startListening(self):

        """ This method makes the input device start listening to the microphone in hopes of speech. `self.onSpoken` or `self.onNotUnderstood` may be called at some point in the future. Returns `None`. Does not handle errors thrown by the microphone interface."""

        pass

    def startRecording(self):

        """ This method starts recording raw audio and stops whenever Sr sees fit or when `killMicrophone` is called. This either returns the path to a temporary file containing the recording or throws whatever error the microphone api throws at this. """

        pass

    def killMicrophone(self):

        """ This method kills the microphone if something was being recorded. It returns `True` if the microphone was running or `False` if it was not. If the microphone was running because of a call to `startListening`, `onInterrupted` is called. If the microphone was running because of a call to `startRecording` it finishes it's job and `startRecording` returns as expected."""

class OutputDevice:

""" This class handles sound through the speakers. """

    def __init__(self, onInterrupted):

        """

        * `onInterrupted`: method to call when the user starts speaking over Sam or Sam needs to abruptly stop because of an internal function.

        """

        self.onInterrupted = onInterrupted

    def speak(self, sentence):

        """This function speaks (if not interrupted) a vocal message. It returns `None`."""

        pass

    def _parseText(self, sentence):

        """This function tries to make spoken text more digestible to the TTS engine. This returns the parsed text."""

class SoundInterface():

    """ This class should hopefully allow using `InputDevice` and `OutputDevice` in a safe way. """

    def __init__(self, onSpeechGotten, onListenInterrupted, onSpeakInterrupted):

        """ This init basically creates both the `InputDevice` and `OutputDevice` """

        self.inDevice = InputDevice(onSpeechGotten, onListenInterrupted)
        self.outDevice = OutputDevice(onSpeakInterrupted)

    def listenToPhrase(self):
        
        """ This method gets the input device to start listening to a phrase. It kills the OutputDevice and the InputDevice's previous jobs. """

    def listenToAudio(self):

        """ This method gets the input device to start listening to raw audio. It kills the OutputDevice and the InputDevice's previous jobs. """

    def speak(self, sentence):

        """ This function makes the output device speak a sentence. This kills all the previous jobs. """

    def askQuestion(self, question):

        """ This function asks a question, waits for the answer and returns it. If no intelligible answer is found, returns `None`. """
