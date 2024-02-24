import re
from datetime import datetime

import aiohttp

import discord

class Plural:
    def __init__(self, **attr):
        iterator = attr.items()
        self.name, self.value = next(iter(iterator))

    def __str__(self):
        v = self.value
        if v > 1 or v == 0:
            if self.name in ["Day", "message"]:
                return "%s %ss" % (self.value, self.name)
            elif self.name in ["became"]:
                return "%ss" % self.name
            return "%s %ss" % (self.value, self.name)
        if self.name in ["became"]:
            return "%s" % self.name
        return "%s %s" % (self.value, self.name)