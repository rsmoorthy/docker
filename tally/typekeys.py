# Type keys and specify shift key up/down

import subprocess
import sys
import argparse
import time
import os

class TypeKeys:
    def __init__(self, *args, **kwargs):
        self.shift = False
        self.name = 'Tally.ERP 9'
        self.window = 0
        if 'WID' in os.environ:
            self.window = os.environ['WID']
        if 'WINDOWID' in os.environ:
            self.window = os.environ['WINDOWID']
        self.chars = {}
        for x in range(ord('A'), ord('Z')+1):
            self.chars[chr(x)] = True
        for x in range(ord('a'), ord('z')+1):
            self.chars[chr(x)] = False
        for x in [' ', ',', '.', '/', ';', "'", '[', ']', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '\\']:
            self.chars[x] = False
        for x in ['<', '>', '?', ':', '"', '{', '}', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '|']:
            self.chars[x] = True

        self.keys = ["BackSpace", "Escape", "Return", "Down", "Up", "Left", "Right"]

    def init(self):
        if not self.window:
            self.window = self.runxdo(["xdotool", "search", "--name", "%s" % (self.name)])
        self.stop_shift()

    def runxdo(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out

    def start_shift(self):
        if self.shift == True:
            return
        self.runxdo(["xdotool", "keydown", "--window", "%s" % (self.window), "Shift"])
        self.shift = True

    def stop_shift(self):
        if self.shift == False:
            return
        self.runxdo(["xdotool", "keyup", "--window", "%s" % (self.window), "Shift"])
        self.shift = False

    def type(self, str):
        if str in self.keys:
            self.runxdo(["xdotool", "key", "--delay", "%s" % (self.delay), "--window", "%s" % (self.window), "%s" % (str)])
            return

        for x in list(str):
            if self.chars[x]:
                self.start_shift()
            else:
                self.stop_shift()
            self.runxdo(["xdotool", "type", "--delay", "%s" % (self.delay), "--window", "%s" % (self.window), "%s" % (x)])
        self.stop_shift()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="string to type")
    parser.add_argument("--ender", help="Key to press at the end", default=None)
    parser.add_argument("--delay", help="delay between characters", default=1)
    parser.add_argument("--window", help="window id")
    parser.add_argument("--sleep", type=float, help="sleep time after commands", default=0.1)
    args = parser.parse_args()
    tk = TypeKeys()
    if args.delay:
        tk.delay = args.delay
    if args.window:
        tk.window = args.window
    tk.init()
    tk.type(args.string)
    if(args.ender):
        tk.type(args.ender)
    time.sleep(args.sleep)
