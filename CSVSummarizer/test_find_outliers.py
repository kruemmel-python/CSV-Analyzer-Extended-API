import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestFindOutliers(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_find_outliers(self):
        col = self.header[7]  # PLZ as an example
        outliers = self.summarizer.find_outliers(col)
        print(f"Outliers in '{col}': {outliers}")
        self.assertGreater(len(outliers), 0)

if __name__ == '__main__':
    unittest.main()
