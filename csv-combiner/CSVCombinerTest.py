import unittest
import CSVCombiner as CSV
import argparse


class MyTestCase(unittest.TestCase):
    csvCombiner = CSV.CSVCombiner()
    parser = argparse.ArgumentParser()
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
