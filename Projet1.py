import mistletoe

modifiedLines = []

with open('Test.md', 'r') as markdownFile:
    readFile = markdownFile.readlines()
    for line in readFile:
        modifiedLine = []
        if line.find('/') != -1:
            for letter in line:
                modifiedLine.append(letter)
            modifiedLine[0] = '<input type="checkbox"> <label>'
            if line.find('\n') != 0:
                modifiedLine[-1] = ('</label><br>')
            else:
                modifiedLine.append('</label><br>')
            modifiedLine.append('\n')
            modifiedLines.append("".join(modifiedLine))
        else:
            modifiedLines.append(line)

with open('Test.md', 'w') as markdownFile:
    markdownFile.write("".join(modifiedLines))

with open('Test.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)
    print(rendered)