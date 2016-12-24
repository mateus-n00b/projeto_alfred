#coding: UTF-8
#  Commands for the alfred.py program
#  Do not remove the 'hashtag,' signal
#
# Mateus-n00b, Dezembro 2016
#
# Version 1.0
# Licence GPL
# -==============================================
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
,'clear':'clear'
#,
                }



# Debug
# a = Commands()
# dic = a.getCommand()
# print dic['firefox']
