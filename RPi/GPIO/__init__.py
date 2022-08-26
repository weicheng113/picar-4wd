OUT = None
IN = None
FALLING = None
RISING = None
BOTH = None
PUD_UP = None
PUD_DOWN = None


def setmode(BCM):
    raise NotImplementedError()


def setwarnings(param):
    raise NotImplementedError()


def setup(_pin, mode, pull_up_down=None):
    raise NotImplementedError()


def input(_pin):
    raise NotImplementedError()


def output(_pin, value):
    raise NotImplementedError()


def add_event_detect(_pin, trigger, callback):
    raise NotImplementedError()