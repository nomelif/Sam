#!/usr/bin/python3

"""

This file runs the Sam HTTPD server. It permits Sam to use a foreign computer as a screen. Different parts of Sam should be able to add their own webpages to this on the fly.

Using a server permits defering most calculation and rendering that would require performance onto a more performant and able-batteried device.

"""

from cherrypy import wsgiserver

class SamServer():

    """ The Sam server works as a HTML5 relay between sam and a remote computer. """

    def __init__(self, port):

        """ This function starts the server, but the server doesn't know how to do anything. """

        pass

    def addPage(self, path, generatePage):

        """ This makes it so that requests for anything under `path` is handled by `generatePage`, which gets all the context data of the app function. """

    def removePage(self, path):

        """ Remove the page matching the pathspec `path`. """

    def kill(self):

        """ This function kills the server. """

        pass
