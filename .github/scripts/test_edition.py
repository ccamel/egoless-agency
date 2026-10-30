import unittest

from edition import render, roman


class EditionTest(unittest.TestCase):
    def test_roman_numbers(self):
        for number, expected in (
            (1, "i"),
            (4, "iv"),
            (9, "ix"),
            (42, "xlii"),
            (1999, "mcmxcix"),
            (4000, "mmmm"),
        ):
            self.assertEqual(roman(number), expected)
        with self.assertRaises(ValueError):
            roman(0)

    def test_render_requires_one_marker(self):
        self.assertEqual(
            render("a <!-- edition --> b", 4),
            'a <span class="edition">edition iv</span> b',
        )
        for html in ("no marker", "<!-- edition --><!-- edition -->"):
            with self.assertRaises(ValueError):
                render(html, 1)


if __name__ == "__main__":
    unittest.main()
