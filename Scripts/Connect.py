#!/usr/bin/python3

import re
import socket
import requests
import time
from ComputerInterface import ComputerInterface


""" The Connect unit walks the user through connecting a new computer to Sam via a web browser. """

def decideActivation(inputData):

    """ Decide whether to activate the unit """

    re.match(r".*connect (a|to (my)?)( new)? (computer|laptop|desktop|phone|tablet|device|machine|box|linux|mac|pc).*", inputData.lower())

def run(io, device, server):

    """ Walk the user through connecting to a new device via Sam. """

    io.speakPhrase("OK. Open a browser on your computer. I would advise for Firefox or Chrome. Tell me when you are done. Also, make sure you are connected to the same Wifi as me.")

    # Wait for the user to be done.

    response = io.listenToPhrase()

    # Shorten the ip

    ip = socket.gethostbyname(socket.getfqdn())

    longVersion = "http://"+ip+":8080/connect"
    #shortened = requests.post("http://api.lyli.fi", json={"url": longVersion}).json()["short-url"]

    # Setup the server

    newDevice = None

    def app(environ, start_response):

        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        
        deviceClass = ComputerInterface.UNKNOWN_DEVICE
        os = ComputerInterface.UNKNOWN_OS

        if "linux" in environ["HTTP_USER_AGENT"].lower():
            deviceClass = ComputerInterface.FOREIGN_DESKTOP
            os = ComputerInterface.LINUX
        elif "mac" in environ["HTTP_USER_AGENT"].lower():
            deviceClass = ComputerInterface.FOREIGN_DESKTOP
            os = ComputerInterface.MACOS
        elif "windows" in environ["HTTP_USER_AGENT"].lower():
            deviceClass = ComputerInterface.FOREIGN_DESKTOP
            os = ComputerInterface.WINDOWS
        elif "android" in environ["HTTP_USER_AGENT"].lower():
            deviceClass = ComputerInterface.FOREIGN_PHABLET
            os = ComputerInterface.ANDROID
        elif "ios" in environ["HTTP_USER_AGENT"].lower():
            deviceClass = ComputerInterface.FOREIGN_PHABLET
            os = ComputerInterface.IOS


        client_ip = None

        try:
            client_ip = environ['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()
        except KeyError:
            client_ip = environ['REMOTE_ADDR']

        global newDevice
        newDevice = ComputerInterface(client_ip, deviceClass, os)

        return [bytes(str(environ), "utf-8")]

    server.addPage("connect", app)

    io.speakPhrase("OK. Now navigate to " + longVersion + ". That is " + longVersion + ".")

    while newDevice == None:
        print(newDevice)
        time.sleep(0.1)

    io.speakPhrase("Great, I've got a connection.")
