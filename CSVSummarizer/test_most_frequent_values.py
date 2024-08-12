import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestMostFrequentValues(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_most_frequent_values(self):
        col = self.header[0]
        result, frequency = self.summarizer.most_frequent_values(col)
        print(f"Most frequent value in '{col}': {result} with frequency {frequency}")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
