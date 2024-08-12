import unittest
import os
import csv
from csv_analyzer_extended import CSVExporter

class TestExportToMarkdown(unittest.TestCase):
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

    def test_export_to_markdown(self):
        print(f"Exporting data to Markdown...")
        exporter = CSVExporter(self.data, self.header)
        export_file = 'exported_data.md'
        exporter.export_to_markdown(export_file)
        self.assertTrue(os.path.exists(export_file))

        # Verifizieren, dass die Markdown-Datei korrekt erstellt wurde
        print(f"Export completed for data to '{export_file}'.")

if __name__ == '__main__':
    unittest.main()
