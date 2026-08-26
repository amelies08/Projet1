with open('Test.md', 'r') as file:
    for line in file:
        if line == "/test":
            modifiedLines = "TEST"
            file.write(modifiedLines)

#with open('Test.md', 'w') as file:
#    file.write(modifiedLines)