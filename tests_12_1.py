import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        ch = Runner('Человек')
        for i in range(10):
            ch.walk()
        self.assertEqual(ch.distance, 50)
    def test_run(self):
        c = Runner('Машина')
        for i in range(10):
            c.run()
        self.assertEqual(c.distance, 100)

    def test_challenge(self):
        ch = Runner('Человек')
        c = Runner('Машина')
        for i in range(10):
            ch.walk()
            c.run()
        self.assertNotEqual(ch.distance, c.distance)

if __name__ == "__main__":
    unittest.main()

