import argparse
import os

NOTE_PATH = "notes/"


def read_note_file(label):
    file_path = os.path.join(NOTE_PATH, label + ".md")
    print(f"{file_path} exists: {os.path.isfile(file_path)}")


def main():
    parser = argparse.ArgumentParser(
        prog="notes",
        description="Save and access short notes from the terminal",
    )

    parser.add_argument("label", help="The label associated with the note group")

    parser.add_argument("-c", "--content", nargs="*", help="The content of the note")

    parser.add_argument(
        "-r",
        "--remove",
        nargs="?",
        const="1",
        help="Remove an entry from the specified note group",
    )

    args = parser.parse_args()

    print("Label:", args.label)
    print("Content:", args.content)
    print("Remove:", args.remove)

    read_note_file("test")


main()
