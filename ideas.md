# Ideas

List of ideas for the first Boot.dev personal project

## 1. notes

A program used to take short notes in the terminal, and list them

Example: 

```
$ notes todo Add new search functionality

New entry added to 'todo' label

$ notes todo

[1] Review docs
[2] Write tests
[3] Add new search functionality

$ notes todo -r 1

Removed entry #1 from 'todo' label

$ notes todo

[1] Write tests
[2] Add new search functionality
```

## 2. dice roller

Roll dice in the terminal

Example:

```
$ roll 1d6

[1d6] : 5

$ roll 1d20+5

[1d20+5] : 23
```

### 3. Project Templater

Easily create new projects based on a directory template

Example:

```
$ ptemp python -n new_python_project

Creating new project directory using 'python' template

$ ls -a new_python_project

src/  .gitignore  ./main.sh
```

Also copy contents of current folder to templates folder

Example:

```
$ ptemp new_template --add src_dir/

New template 'new_template' created based on contents of src_dir/

$ ptemp new_template --add another_dir/

Template 'new_template' already exists. To update its contents use --update

```

