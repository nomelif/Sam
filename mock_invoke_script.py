#!/usr/bin/python

import importlib

""" This file invokes the sript passed as a parameter with a mock IO device. """

class MockIOInterface():

    """ This class interfaces a CLI to a script for debug purposes. """

    def listenToPhrase(self):

        """Read a line from CLI, mocks listening for a phrase through a microphone."""
        return input(">>> ")

    def listenToAudio(self):

        """Return the path given through CLI. This should be a path to an audio file. Mocks recording raw audio data through the microphone."""

        return input("[path to audio file] >>> ")

    def speakPhrase(self, sentence):

        """Prints the given sentence to CLI. Mocks speaking it out loud."""

        print("[spoken] " + sentence)

    def askQuestion(self, question):

        """Asks a question over the CLI. Mocks asking it out loud."""

        self.speak(question)
        return self.listenToPhrase()

from HTTPServer import SamServer

script = input("Script: ")


server = SamServer(8080)

invocation = input("Invoke with phrase: ")

run = importlib.import_module("Scripts." + script).run


run(MockIOInterface(), None, server)

