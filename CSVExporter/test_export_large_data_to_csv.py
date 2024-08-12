import unittest
import csv
import os
from csv_analyzer_extended import CSVExporter

class TestExportLargeDataToCSV(unittest.TestCase):
    def setUp(self):
        # Generieren Sie eine groﬂe Datenmenge, falls die Datei nicht existiert
        self.file_path = 'large_data.csv'
        self.header = ['Column1', 'Column2', 'Column3']
        self.data = [['Data1', 'Data2', 'Data3'] for _ in range(5000000)]  # 5 Millionen Datens‰tze

        # Wenn die Datei nicht existiert, erstellen Sie sie
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.header)
                writer.writerows(self.data)

    def test_export_large_data_to_csv(self):
        print(f"Exporting large data set to CSV...")
        exporter = CSVExporter(self.data, self.header)
        export_file = 'large_data_export.csv'
        exporter.export_to_csv(export_file)
        self.assertTrue(os.path.exists(export_file))
        print(f"Export completed for large data set to '{export_file}'.")

if __name__ == '__main__':
    unittest.main()
