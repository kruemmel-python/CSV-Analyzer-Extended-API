import unittest
from csv_analyzer_extended import CSVSummarizer
import csv

class TestCalculateZScores(unittest.TestCase):
    def setUp(self):
        self.data = self._load_test_data()
        self.header = self.data[0]
        self.summarizer = CSVSummarizer(self.data[1:], self.header)

    def _load_test_data(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def test_calculate_z_scores(self):
        col = self.header[7]  # PLZ as an example
        z_scores = self.summarizer.calculate_z_scores(col)
        print(f"Z-Scores for '{col}': {z_scores[:10]}...")  # print only first 10 for brevity
        self.assertIsNotNone(z_scores)

if __name__ == '__main__':
    unittest.main()
