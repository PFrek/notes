import os
import pyperclip


class Note:
    NOTE_PATH = "notes/"

    def __init__(self, label):
        self.label = label
        self._entries = []

    def add_entry(self, entry, index=None):
        if len(entry) == 0:
            raise ValueError("Entry cannot be empty")

        if index is None:
            index = len(self._entries)

        if index < 0:
            raise ValueError("Index must be greather or equal to zero")

        self._entries.insert(index, entry)

    def add_entries(self, entries, index=None):
        if len(entries) == 0:
            raise ValueError("Entries cannot be empty")

        if index is None:
            index = len(self._entries)

        for entry in entries[-1::-1]:
            self.add_entry(entry, index)

    def remove_entry(self, index=None):
        if len(self._entries) == 0:
            return

        if index is None:
            self._entries.pop()
            return

        if index < 0 or index >= len(self._entries):
            raise ValueError("Index out of bounds")

        self._entries.pop(index)

    def to_clipboard(self, index=None):
        if len(self._entries) == 0:
            return

        if index is None:
            pyperclip.copy(f"{self}")
            return

        if index < 0 or index >= len(self._entries):
            raise ValueError("Index out of bounds")

        pyperclip.copy("[" + str(index + 1) + "]: " + self._entries[index] + "\n")

    def __repr__(self):
        if len(self._entries) == 0:
            return f"No entries under label '{self.label}'"

        num_entries = len(self._entries)
        max_width = len(str(num_entries))
        s = ""
        for i in range(len(self._entries)):
            s += "[" + str(i + 1).rjust(max_width, " ") + "]: "
            s += self._entries[i]
            s += "\n"

        return s[:-1]

    def get_filepath(self):
        return os.path.join(Note.NOTE_PATH, self.label + ".md")

    def _read_note_file(self, label):
        self.label = label
        file_path = self.get_filepath()

        if not os.path.isfile(file_path):
            return ""

        contents = ""
        with open(file_path, "r") as f:
            contents = f.read()

        return contents

    def _extract_entries(self, contents):
        start = contents.find("1.")

        return list(filter(lambda entry: len(entry) > 0, contents[start:].split("\n")))

    def _remove_indexes(self, entries):
        return list(map(lambda entry: entry[entry.find(".") + 2 :], entries))

    def open(self, label=None):
        if label:
            self.label = label
        else:
            label = self.label

        contents = self._read_note_file(label)
        entries = self._extract_entries(contents)
        if len(entries) > 0:
            entries = self._remove_indexes(entries)
            self.add_entries(entries)

    def write(self):
        file_path = os.path.join(Note.NOTE_PATH, self.label + ".md")

        with open(file_path, "w") as f:
            f.write(f"# {self.label}\n\n")

            for i in range(len(self._entries)):
                f.write(f"{i+1}. {self._entries[i]}\n")
