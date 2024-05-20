# Notes

A simple program for creating notes / lists in the terminal.

Notes are grouped under a label, and can be copied to the clipboard.

## Installation

1. Install pipenv if not already present:

```
$ python -m pip install pipenv
```

2. Clone the respository
3. Install the dependencies using pipenv:

```
$ pipenv install
```

7. Run the program:

```
$ pipenv run python src/notes.py ...
```

10. Or using the .sh file:
```
$ ./notes.sh test Adding a new entry to the test label!
```

## Dependencies

- Pyperclip - [GitHub](https://github.com/asweigart/pyperclip)


## Usage

### Adding a new note to a group

To add a new note to a group, you just have to give two arguments:
The label under which the note will be saved, and the contents of the note.

```
$ ./notes.sh label_name This is a note saved under the 'label_name' label!

[1]: This is a note saved under the label_name label!
```

The current state of the label will be echoed to the terminal as a numbered list.

---

### Printing a group:

To print all the notes added to a label you can omit the contents argument.

```
$ ./notes.sh todo

[1]: Review the study material
[2]: Write script for the presentation
[3]: Send email confirming meetup time
```

---

### Adding a note at a specific position

You can use the -i / --index option to tell the program at which position the new note should be added.

This index value is equivalent to the numbers listed when printing a group, so it starts at 1.

```
$ ./notes.sh todo Fix the data in the slides -i 3

[1]: Review the study material
[2]: Write script for the presentation
[3]: Fix the data in the slides
[4]: Send email confirming meetup time
```

---

### Removing a note

To remove a note you can use the -r / --remove option, passing the index of the note to be removed.

If no index is passed, the last note is removed.

```
$ ./notes.sh todo -r 1

[1]: Write script for the presentation
[2]: Fix the data in the slides
[3]: Send email confirming meetup time
```

---

### Replacing a note / editing

By combining the -i and -r options, the contents of a note can be replaced. This is because the removal happens before insertion.

```
$ ./notes.sh todo "Fix the data in the slides # 5 and 7" -i 2 -r 2

[1]: Write script for the presentation
[2]: Fix the data in the slides # 5 and 7
[3]: Send email confirming meetup time
```

---

### Copying a note to the clipboard

The -c / --copy option allows for the contents of a label to be sent to the clipboard.

If no index value is passed to it, all of the notes are copied.

```
$ ./notes.sh todo -c 3

Copied entry to clipboard
```

Clipboard state:  
> \[3\]: Send email confirming meetup time

```
$ ./notes.sh todo -c

Copied entries to clipboard
```

Clipboard state:  
> \[1\]: Write script for the presentation  
> \[2\]: Fix the data in the slides # 5 and 7  
> \[3\]: Send email confirming meetup time  

---

### Printing the location of a note file

Notes are saved in the notes/ directory, as markdown files called \[label_name\].md

You can print the location of a specific label's file using the -w / --where option.

```
$ ./notes.sh todo -w

[path to the project]/notes/todo.md
```

---

### List existing labels

If you need a reminder of the current labels that contain notes, you can use the -l / --list option.

This option does not require a label argument.

```
$ ./notes.sh -l

Existing labels:
- install
- label_name
- reminder
- todo
```

---

### Deleting all entries under a label

To delete all entries under a label and remove the associated markdown file, use the -d / --delete option.

A confirmation will be required before the file is deleted.

```
$ ./notes.sh todo -d

This command will delete all notes under 'todo'. Confirm? (Y/N): Y
Deleted notes under label 'todo'

$ ./notes.sh -l

- install
- label_name
- reminder
```

