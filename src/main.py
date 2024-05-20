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
        nargs="?",
        const="1",
        help="Remove an entry from the specified note group",
    )

    args = parser.parse_args()

    label = args.label.lower()
    print("Label:", label)
    content = args.content
    print("Content:", content)
    remove = args.remove
    print("Remove:", args.remove)

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
        note.add_entry(content)

    note.write()

    print(note)


main()
