import argparse
import os

from note import Note


def list_labels(list_arg):
    if not list_arg:
        return False

    def remove_extension(file):
        return file.split(".")[0]

    labels = list(
        sorted(
            map(
                remove_extension,
                filter(lambda path: path[-3:] == ".md", os.listdir(Note.NOTE_PATH)),
            )
        )
    )
    print("Existing labels:")
    for label in labels:
        print("-", label)

    return True


def delete_note(delete_arg, note):
    if not delete_arg:
        return False

    answer = input(f"This command will delete all notes under '{
        note.label}'. Confirm? (Y/N): ")

    if answer == "Y":
        note.delete()
        print(f"Deleted notes under label '{note.label}'")
        return True

    return False


def print_filepath(where_arg, note):
    if not where_arg:
        return False

    filepath = note.get_filepath()
    if not os.path.isfile(filepath):
        print(f"No note file for label '{note.label}'")
        return True

    print(os.path.abspath(note.get_filepath()))
    return True


def copy(copy_arg, note):
    if not copy_arg:
        return False

    if copy_arg == "all":
        copy_index = None
    else:
        try:
            copy_index = int(copy_arg) - 1
        except Exception as e:
            print("Index error:", e)
            print("Skipping copy operation")
            return False

    try:
        note.to_clipboard(copy_index)
        msg = "Copied "
        if copy_index is not None and copy_index >= 0:
            msg += "entry "
        else:
            msg += "entries "
        msg += "to clipboard"
        print(msg)
        return True

    except ValueError as e:
        print("Error:", e)
        return True


def remove_entry(remove_arg, note):
    if not remove_arg:
        return

    try:
        if remove_arg == "last":
            remove_index = None
        else:
            remove_index = int(remove_arg) - 1

        note.remove_entry(remove_index)
        note.write()
    except ValueError as e:
        print("Error:", e)
        print("Skipping remove operation")


def add_entry(content, index, note):
    if content is None or len(content) == 0:
        return

    content = " ".join(content)

    if index is not None:
        try:
            index = int(index) - 1
        except Exception as e:
            print("Index error:", e)
            print("Adding entry to end of list")
            index = None

    try:
        note.add_entry(content, index)
        note.write()
    except ValueError:
        print("Index must be greater than zero")
        return


def main():
    parser = argparse.ArgumentParser(
        prog="notes.py",
        description="Save and access short notes from the terminal",
    )

    parser.add_argument(
        "label",
        nargs="?",
        default=None,
        help="The label associated with the note group",
    )

    parser.add_argument("content", nargs="*", help="The content of the note")

    parser.add_argument(
        "-r",
        "--remove",
        metavar="index",
        nargs="?",
        const="last",
        help="The position from which to remove an entry",
    )

    parser.add_argument(
        "-i",
        "--index",
        help="The position where the new entry will be inserted",
        metavar="index",
    )

    parser.add_argument(
        "-c",
        "--copy",
        metavar="index",
        nargs="?",
        const="all",
        help="Copy an entry to the clipboard. If no index is specified, copy all entries",
    )

    parser.add_argument(
        "-w", "--where", action="store_true", help="Print the location of the note file"
    )

    parser.add_argument(
        "-d",
        "--delete",
        action="store_true",
        help="Delete the note file identified by 'label'",
    )

    parser.add_argument(
        "-l", "--list", action="store_true", help="List all existing labels"
    )

    args = parser.parse_args()

    if list_labels(args.list):
        return

    if args.label is None:
        parser.print_usage()
        return

    label = args.label.lower()

    note = Note(label)
    note.open()

    if delete_note(args.delete, note):
        return

    if print_filepath(args.where, note):
        return

    if copy(args.copy, note):
        return

    remove_entry(args.remove, note)

    add_entry(args.content, args.index, note)

    print(note)


main()
