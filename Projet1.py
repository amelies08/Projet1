import mistletoe


def checklistMD(fileName):
    """ This function changes the symbol / of a markdown file into a checkbox.
    
    Args: 
        fileName (str): name of the markdown file that contains the checklist (without the .md)
    """

    modifiedLines = [] # Empty list to put the lines of the file read

    with open(fileName + '.md', 'r') as markdownFile: # Open the file to read it
        readFile = markdownFile.readlines() # Read the file line by line
        for line in readFile:
            modifiedLine = [] # Empty list to put the characters of the line
            if line.find('/') != -1: # If the character "/" is found in the line
                for letter in line:
                    modifiedLine.append(letter) # The character is added to modifiedLine
                    modifiedLine[0] = '<input type="checkbox"> <label>' # A checkbox is added at the beginning of the line
                if line.find('\n') != 0: # If there is an enter at the end of the line
                    modifiedLine[-1] = ('</label><br>') # Replace it to indicate the end of the text of the checkbox
                else: # If there is no enter at the end of the line
                    modifiedLine.append('</label><br>') # Add the indicator for the end of the checkbox's text
                modifiedLine.append('\n') # Add an enter at the end of the line
                modifiedLines.append("".join(modifiedLine)) # Join all the character in modifiedLine in one string and add it to modifiedLines
            else: # If the character "/" isn't found
                modifiedLines.append(line) # Add the full line to modifiedLines

    with open(fileName + 'MD.md', 'w') as markdownFile: # Open a new markdown file to write in it
        markdownFile.write("".join(modifiedLines)) # Insert all the lines in modifiedLines in the file

    with open(fileName + 'MD.md', 'r') as fin: # Open the new markdown file to read it
        rendered = mistletoe.markdown(fin) # Use mistletoe to change the markdown file into a html string

    with open(fileName + '.html', 'w') as htmlFile: # Open a new html file to write in it
        htmlFile.write(rendered) # Put the html string into a html file

checklistMD("Test") # Exemple of the call of the function