#coding: UTF-8
class Commands():
    """Here you'll put a list of your commands."""
    def __init__(self):
        self = None
    def getCommand(self):
        # Add your commands in the dict
        # {howToCallIt:command}
        return {'firefox': 'firefox &',
                'music':'totem &',
		        'metallica':'totem ~/Música/Metallica\ \(Black\ Album\)\ -\ 1991/ &'
		}



# Debug
# a = Commands()
# dic = a.getCommand()
# print dic['firefox']
