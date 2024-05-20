from src.note import Note
import unittest
import sys

sys.path.append("../src")


class TestNote(unittest.TestCase):
    def test_add_entry(self):
        n1 = Note("Test")

        n1.add_entry("Hello there")
        n1.add_entry("Hows it going")
        n1.add_entry("Im in the middle", 1)
        n1.add_entry("Im at the start", 0)

        self.assertEqual(
            n1._entries,
            ["Im at the start", "Hello there", "Im in the middle", "Hows it going"],
        )

    def test_add_entries(self):
        n1 = Note("Test")

        n1.add_entries(["1", "2", "3", "4"])

        n1.add_entries(["1.1", "1.2", "1.3"], 1)

        self.assertEqual(n1._entries, ["1", "1.1", "1.2", "1.3", "2", "3", "4"])

    def test_repr_empty(self):
        n1 = Note("Test")

        s = f"{n1}"

        self.assertEqual(s, "No entries under label 'Test'")

    def test_repr_many_entries(self):
        n1 = Note("Test")

        n1.add_entries(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12",
            ],
        )

        s = f"{n1}"

        self.assertEqual(
            s,
            """[ 1]: 1
[ 2]: 2
[ 3]: 3
[ 4]: 4
[ 5]: 5
[ 6]: 6
[ 7]: 7
[ 8]: 8
[ 9]: 9
[10]: 10
[11]: 11
[12]: 12""",
        )


if __name__ == "__main__":
    unittest.main()
