##Determine weather a give sring is Unique or Not

import unittest

def isUnique(myString):
    chars={}
    for char in myString:
        if char in chars:
            return False
        chars[char] = True
    return True

class Test(unittest.TestCase):
    trueData = [('abcdef'),(''),('asdfghj') ]
    falseData = [('asaas'),('srgas')]

    def test_unique(self):
        for test_string in self.trueData:
            actual = isUnique(test_string)
            self.assertTrue(actual)

        for test_string in self.falseData:
            actual = isUnique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()