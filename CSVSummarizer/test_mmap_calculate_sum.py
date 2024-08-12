import unittest
from csv_analyzer_extended import CSVSummarizer

class TestMmapCalculateSum(unittest.TestCase):
    def setUp(self):
        self.header = ["Land", "Vorname", "Nachname", "Geschlecht", "Email", "Telefonnummer", "Straße", "PLZ", "Ort"]
        self.summarizer = CSVSummarizer([], self.header)

    def test_mmap_calculate_sum(self):
        col = "PLZ"  # PLZ as an example
        total_sum = self.summarizer.mmap_calculate_sum(col, 'data.csv')
        print(f"Mmap Sum of '{col}': {total_sum}")
        self.assertIsNotNone(total_sum)

if __name__ == '__main__':
    unittest.main()
