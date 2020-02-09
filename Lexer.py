"""
import Command
def lex(root):
    commands = []

    while root.below is not None:
        commands.append(root.command)
        root = root.below

    return commands
"""
def getTokens(path):
    raw = open(path)
    lines = raw.split("\n")
    words = sum(((line.split(" ")+[";"]) for line in lines), [])
    return words

