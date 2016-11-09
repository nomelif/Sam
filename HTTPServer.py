#!/usr/bin/python3

"""

This file runs the Sam HTTPD server. It permits Sam to use a foreign computer as a screen. Different parts of Sam should be able to add their own webpages to this on the fly.

Using a server permits defering most calculation and rendering that would require performance onto a more performant and able-batteried device.

"""

from cherrypy import wsgiserver
import threading

class SamServer():

    """ The Sam server works as a HTML5 relay between sam and a remote computer. """

    def __init__(self, port):

        """ This function starts the server, but the server doesn't know how to do anything. """


        self._methods = {}
        self.server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', port), self._app)

        threading.Thread(target=self.server.start).start()
        #self.server.start()

    def _app(self, environ, start_response):

        """ WSGI app: delegate everything to submethods """

        for key in self._methods.keys():
            if environ["PATH_INFO"].split("/")[1] == key:
                return self._methods[key](environ, start_response)
        status = "404 Not Found"
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [b"Page not found"]

    def addPage(self, path, generatePage):

        """ This makes it so that requests for anything under `path` is handled by `generatePage`, which gets all the context data of the app function. """

        self._methods[path] = generatePage

    def removePage(self, path):

        """ Remove the page matching the pathspec `path`. """

    def kill(self):

        """ This function kills the server. """

        pass
