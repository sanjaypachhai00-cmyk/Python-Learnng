#ASSERT
def add(a, b):
    return a + b


assert add(2, 3) == 5
assert add(10, 20) == 30

print("All tests passed!")


#unittest
import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_more(self):
        self.assertEqual(add(10, 20), 30)

if __name__ == "__main__":
    unittest.main()