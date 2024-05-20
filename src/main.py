import argparse
import os

from note import Note


def main():
    parser = argparse.ArgumentParser(
        prog="notes",
        description="Save and access short notes from the terminal",
    )

    parser.add_argument("label", help="The label associated with the note group")

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

    args = parser.parse_args()

    label = args.label.lower()
    content = args.content
    remove = args.remove
    index = args.index
    copy = args.copy
    where = args.where

    note = Note(label)
    note.open()

    if where:
        filepath = note.get_filepath()
        if not os.path.isfile(filepath):
            print(f"No note file for label '{label}'")
            return

        print(os.path.abspath(note.get_filepath()))
        return

    if copy is not None:
        if copy == "all":
            copy_index = None
        else:
            try:
                copy_index = int(copy) - 1
            except Exception as e:
                print("Index error:", e)
                print("Skipping copy operation")
                return

        try:
            note.to_clipboard(copy_index)
            msg = "Copied "
            if copy_index:
                msg += "entry "
            else:
                msg += "entries "
            msg += "to clipboard"
            print(msg)
            return

        except ValueError as e:
            print("Error:", e)
            return

    if remove is not None:
        try:
            if remove == "last":
                remove_index = None
            else:
                remove_index = int(remove) - 1

            note.remove_entry(remove_index)
            note.write()
        except ValueError as e:
            print("Error:", e)
            print("Skipping remove operation")

    if content is not None and len(content) > 0:
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
        except ValueError as e:
            print("Index must be greater than zero")
            return

    print(note)


main()
