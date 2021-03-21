# Imports
import fileinput
import re
import os

# ----------------------------------------------------------------------------
# Input Variables

# Group marker must start with comment trigger
commentTrigger = ';'

# ----------------------------------------------------------------------------
# Variables
fileToSearchDirectory = r'.\FilesToEdit'

# ----------------------------------------------------------------------------
# Helpers
# Formatting Helper: Gets filePath from file Name and Directory


def getFilePath(fileDirectory, fileName):
    return r'{filePath}\{fileName}'.format(filePath=fileDirectory, fileName=fileName)


# ----------------------------------------------------------------------------
# Main Code/ Algorithm
# Loop through all files to be editted
for fileName in os.listdir(fileToSearchDirectory):
    # Open current file
    filePath = getFilePath(fileToSearchDirectory, fileName)
    with fileinput.FileInput(filePath, inplace=True) as file:
        # Loop through all lines
        for line in file:
            # If line is a commentTrigger line, edit it
            if line[0] == commentTrigger:
                # ------------------------------------------------------------------------
                # Input: how to format new Line
                # Trimmed off the last 'new line' part of the editted line and added on a new tail
                print(line[0:-1]+';\n', end='')
                # ------------------------------------------------------------------------
            # Write line as if if it is not a trigger line
            else:
                print(line, end='')
