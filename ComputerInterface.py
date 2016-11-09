#!/usr/bin/python3

""" This file provides an interface to a foreign device """

class ComputerInterface():

    """ This class provides an interface to a foreign device. """

    def __init__(self, ip, deviceClass, OS):

        self.ip = ip
        self.deviceType = deviceClass
        self.os = OS

    SUPPORTED_DESKTOP = 0

    """A desktop with the Sam client installed."""


    FOREIGN_DESKTOP = 1

    """A desktop without the Sam client installed."""


    SUPPORTED_PHABLET = 2

    """A phablet with the Sam client installed."""


    FOREIGN_PHABLET = 3

    """A phablet without the Sam client installed."""


    UNKNOWN_DEVICE = 4

    """A device that Sam doesn't directly support."""


    def deviceClass():

        """ This function tells what type of device Sam is connected to. Possible values are `ComputerInterface.SUPPORTED_DESKTOP`, `ComputerInterface.FOREIGN_DESKTOP`, `ComputerInterface.SUPPORTED_PHABLET`, `ComputerInterface.FOREIGN_PHABLET` and `ComputerInterface.UNKNOWN_DEVICE`. """

        return self.deviceType

    def hasClientInstalled():

        """ This function tells whether the connected device has a Sam client installed. `True` if it has, `False` otherwise."""

        pass


    WINDOWS = 0
    
    """Some version of the Windows operating system."""


    LINUX = 1

    """Some distribution of the GNU/Linux operating system (excluding Android)."""


    MACOS = 2

    """Some version of the macOS or OS X operating systems."""


    FOREIGN_UNIX_DESKTOP = 3

    """Some Unix desktop of an unknown description."""


    ANDROID = 4

    """Some version of the Android operating system."""


    IOS = 5


    """Some version of the iOS operating system."""


    UNKNOWN_OS = 6


    """Some operating system that we do not know."""


    def getOS():

        """ This function tells what operating system the connected device is running. It can return `ComputerInterface.WINDOWS`, `ComputerInterface.LINUX`, `ComputerInterface.MACOS`, `ComputerInterface.FOREIGN_UNIX_DESKTOP`, `ComputerInterface.ANDROID`, `ComputerInterface.IOS`, `ComputerInterface.UNKNOWN`. """

        return self.os

    def passCommand(command):

        """ Pass a command on the other operating system. May fail if the OS doesn't have the Sam client installed. Access to a Unix-like command prompt is guaranteed. Return immediately. Return whether it was possible to run the command."""


    def commandAsRoot(command):

        """ Pass a command as root. May fail if the OS doesn't habe the Sam client installed. Access to a Unix-like command prompt is guaranteed. Return immediately. Return whether it was possible to run the command. If root permissions couldn't be aquired, return `False`. Asking for root is done graphically. """

    def spawnBrowser(url):

        """ Open a new browser window (on desktop oses supporting this) or a new tab (mainly on mobile devices) pointing at the `url` given. """
