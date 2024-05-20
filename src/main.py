import argparse

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
        const="1",
        help="The position from which to remove an entry",
    )

    parser.add_argument(
        "-i",
        "--index",
        help="The position where the new entry will be inserted",
        metavar="index",
    )

    args = parser.parse_args()

    label = args.label.lower()
    content = args.content
    remove = args.remove
    index = args.index

    note = Note(label)
    note.open()

    if remove is not None:
        try:
            remove_index = int(remove)
            note.remove_entry(remove_index - 1)
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
        except ValueError as e:
            print("Index must be greater than zero")
            return

    note.write()

    print(note)


main()
