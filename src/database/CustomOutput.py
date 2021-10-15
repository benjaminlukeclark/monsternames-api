#############################################################################################
#   Module to output different coloured messages on the console                             #
#                                                                                           #
#                                                                                           #
#   Author: Benjamin Clark                                                                  #
#   Purpose: Provide functions to output different coloured texts to the console.           #
#            Practical use is for debugging and user feedback purposes.                     #
#                                                                                           #
#                                                                                           #
#                               Requirements                                                #
#                                                                                           #
#   Python 3.8.1                                                                            #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

# Output a message in red to display an error
def OutputError(message):
    print('\033[1;31m {0} \033[1;m'.format(message))
# Output a message in green to display a success message
def OutputSuccess(message):
    print('\033[1;32m {0} \033[1;m'.format(message))
# Output a message in white for an informational message
def OutputInfo(message):
    print('\033[1;37m {0} \033[1;m'.format(message))