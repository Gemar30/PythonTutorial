#./ go to current folder
PLACEHOLDER = "[name]"

with open("/Users/gemarusi/Documents/GitHub/PythonTutorial/100DaysofPython/mail-merge-project-start/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("/Users/gemarusi/Documents/GitHub/PythonTutorial/100DaysofPython/mail-merge-project-start/Input/Letters/starting_letter.docx", "r") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode = "w") as completed_letter:
            completed_letter.write(new_letter)
