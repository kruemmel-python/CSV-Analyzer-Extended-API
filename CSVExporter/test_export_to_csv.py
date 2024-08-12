import unittest
import os
from csv_analyzer_extended import CSVExporter

class TestExportToCSV(unittest.TestCase):
    def setUp(self):
        self.file_path = 'data.csv'
        self.header = ['Column1', 'Column2', 'Column3']
        self.data = [['Data1', 'Data2', 'Data3'], ['Data4', 'Data5', 'Data6']]  # Beispielhafte Daten

        # Wenn die Datei nicht existiert, erstellen Sie sie
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.header)
                writer.writerows(self.data)

    def test_export_to_csv(self):
        print(f"Exporting data to CSV...")
        exporter = CSVExporter(self.data, self.header)
        export_file = 'exported_data.csv'
        exporter.export_to_csv(export_file)
        self.assertTrue(os.path.exists(export_file))

        # Verifizieren, dass die CSV-Datei korrekt erstellt wurde
        with open(export_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertEqual(len(lines) - 1, len(self.data))  # Subtrahiere 1 für die Header-Zeile
            print(f"Export completed for data to '{export_file}'.")

if __name__ == '__main__':
    unittest.main()
