import unittest
import CSVCombiner as CSVCombinerClass
import argparse
from unittest.mock import Mock
from unittest.mock import patch
my_mock = Mock()


class MyTestCase(unittest.TestCase):
    parser = argparse.ArgumentParser()
    csvCombiner = CSVCombinerClass.CSVCombiner()
    list = ['./fixtures/clothing.csv', './fixtures/accessories.csv', './fixtures/household_cleaners.csv', '']
    @patch('CSVCombiner.input')
    def test_something(self,mock_input):
        mock_input.return_value = list
        self.assertEqual(True,self.csvCombiner.main())  # add assertion here


if __name__ == '__main__':
    unittest.main()
