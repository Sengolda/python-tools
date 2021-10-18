import unittest
from pytools.copying_doc import copy_doc
from pytools.valid_url import check_url
from pytools.valid_email import check_email
from pytools.finding import find


class TestCase(unittest.TestCase):
    def test_copydoc(self):
        def func1_with_doc():
            """this has a doc."""
        

        @copy_doc(func1_with_doc)
        def func1():
            return

        self.assertEqual(func1_with_doc.__doc__, func1.__doc__)
    

    def test_valid_url(self):
        url = check_url("https://google.com")
        url2 = check_url("e")
        self.assertEqual(url, True)
        self.assertEqual(url2, False)
    

    def test_valid_email(self):
        e = check_email("user123@github.com")
        e2 = check_url("e")
        self.assertEqual(e, True)
        self.assertEqual(e2, False)
    

    def test_find(self):
        seq = ["e"]
        x = find(lambda x: "e" in x, seq)
        y = find(lambda x: "y" in x, seq)
        self.assertEqual(x, "e")
        self.assertEqual(y, None)



if __name__ == "__main__":
    unittest.main()
