import Command


def lex(root):
    commands = []

    while root.below is not None:
        commands.append(root.command)
        root = root.below

    return commands
