import unittest

from lint_commits import valid_message


class CommitMessageTest(unittest.TestCase):
    def test_symbols_only(self):
        for symbol in ("¶", "≈", "∷"):
            for ending in ("", "\n"):
                self.assertTrue(valid_message((symbol + ending).encode()))
        for message in ("", "Fix layout", "≈ ", "≈\n\n", "≈\n\nbody\n", "≈∷\n"):
            self.assertFalse(valid_message(message.encode()))


if __name__ == "__main__":
    unittest.main()
