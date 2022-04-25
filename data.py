import json


def initData():
    N = 0
    L = 0

    with open('files/config.json') as config:
        templates = json.load(config)

    for section, commands in templates.items():
        if (section == 'N'):
            N = commands
        if (section == 'L'):
            L = commands

    return [N, L]

