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
        * `onInterrupted`: method to call when the user interrupts Sam when Sam is talking. The sound is killed before this is called.
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

        """ This method kills the microphone if something was being recorded. It returns `True` if the microphone was running or `False` if it was not. If the microphone was running because of a call to `startListening`, `onInterrupted` is called. If the microphone was running because of a call to `startRecording` it finishes it's job and `startRecording` returns as expected.
