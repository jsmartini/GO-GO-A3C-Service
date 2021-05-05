from dataclasses import dataclass

@dataclass
class StateDicts:
    #obj for passing pytorch statedicts
    sdict = None

@dataclass
class SystemUpdate:
    #obj for passing system states
    update = dict()