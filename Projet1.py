import mistletoe


def convertir_diapositive(fichier_md, fichier_html):
    """
    Convertit un fichier Markdown contenant des 'Slide::'
    en un fichier HTML contenant une div par diapositive.
    """

     # Ouvre le fichier Markdown en mode lecture
    with open(fichier_md, 'r', encoding='utf-8') as contenu:
         # Lit tout le contenu du fichier et le stock dans une variable
        texte = contenu.read()

    # Séparer les diapositives à chaque 'Slide::'
    slides = texte.split("Slide::")

    # CSS des diapositives, gestion de la couleur et de la taille de la diapositive
    css = """
    <style>
        .slide {
            background-color: rgb(158, 193, 230);
            width: 100vw;
            height: 70vh;
        }
    </style>
    """
    # Variable qui stock le contenu HTML 
    resultat = ""

    # Convertir chaque slide en HTML
    for slide in slides:
        # Place le contenu HTML dans une div ayant la classe "slide"
        slide = '<div class="slide">' + slide + '</div>'

        # Ajoute la diapositive au résultat final
        resultat += slide

    with open(fichier_html, 'w') as fichier:
        fichier.write(resultat)

    return fichier_html


def checklistMD(fileName_md):
    """ This function changes the symbol / of a markdown file into a checkbox.
    
    Args: 
        fileName_md (str): name of the markdown file that contains the checklist
    """

    modifiedLines = [] # Empty list to put the lines of the file read

    with open(fileName_md, 'r') as markdownFile: # Open the file to read it
        readFile = markdownFile.readlines() # Read the file line by line
        for line in readFile:
            modifiedLine = [] # Empty list to put the characters of the line
            if line.find('/') != -1: # If the character "/" is found in the line
                counter = 0
                for letter in line:
                    modifiedLine.append(letter) # The character is added to modifiedLine
                if modifiedLine[0] == "/":
                    modifiedLine[0] = '<input type="checkbox"> <label>' # A checkbox is added at the beginning of the line
                    if line.find('\n') != 0: # If there is an enter at the end of the line
                        modifiedLine[-1] = ('</label><br>') # Replace it to indicate the end of the text of the checkbox
                    else: # If there is no enter at the end of the line
                        modifiedLine.append('</label><br>') # Add the indicator for the end of the checkbox's text
                    modifiedLine.append('\n') # Add an enter at the end of the line
                modifiedLines.append("".join(modifiedLine)) # Join all the character in modifiedLine in one string and add it to modifiedLines
            else: # If the character "/" isn't found
                modifiedLines.append(line) # Add the full line to modifiedLines

    modifiedText = "".join(modifiedLines) # Join all the lines from modifiedLines into one string

    with open(fileName_md, 'w') as file:
        file.write(modifiedText)

    return fileName_md


# Appelle la fonction avec le fichier Markdown en entrée
# et le fichier HTML qui sera créé en sortie
file_html = convertir_diapositive("Test.md", "TEST.html")

file_html = checklistMD(file_html) # Exemple of the call of the function

rendered = mistletoe.markdown(file_html) # Use mistletoe to change the markdown file into a html string

# Écrire le résultat dans le fichier HTML
with open(file_html, 'w', encoding='utf-8') as fout:
    # Écrit le CSS et toutes les diapositives dans le fichier HTML
    fout.write(rendered)
