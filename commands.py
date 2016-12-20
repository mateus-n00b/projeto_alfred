class Commands():
    """Here you'll put a list of your commands."""
    def __init__(self):
        self = None
    def getCommand(self):
        # Add your commands in the dict
        # {howToCallIt:command}
        return {'firefox': 'firefox &',
                'music':'totem &'}



# Debug
# a = Commands()
# dic = a.getCommand()
# print dic['firefox']
