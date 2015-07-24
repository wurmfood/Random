#!/usr/bin/env python3

import os


# Clear the screen regardless of the OS.
# This will go away once we are storing data better.
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

