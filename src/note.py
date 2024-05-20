class Note:
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
