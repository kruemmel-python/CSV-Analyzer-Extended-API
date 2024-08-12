import unittest
from csv_analyzer_extended import CSVSummarizer

class TestMmapCalculateMax(unittest.TestCase):
    def setUp(self):
        self.header = ["Land", "Vorname", "Nachname", "Geschlecht", "Email", "Telefonnummer", "Straße", "PLZ", "Ort"]
        self.summarizer = CSVSummarizer([], self.header)

    def test_mmap_calculate_max(self):
        col = "PLZ"  # PLZ as an example
        max_value = self.summarizer.mmap_calculate_max(col, 'data.csv')
        print(f"Mmap Max of '{col}': {max_value}")
        self.assertIsNotNone(max_value)

if __name__ == '__main__':
    unittest.main()
