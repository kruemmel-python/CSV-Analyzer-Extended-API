import os
from csv_analyzer_extended import CSVAnalyzer, CSVExporter
import sqlite3

# Erstelle den Ordner 'testoutput', falls er nicht existiert
output_dir = 'testoutput'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialisiere den CSVAnalyzer mit einer CSV-Datei
analyzer = CSVAnalyzer("test_data.csv")

# Lade die Daten
header, data = analyzer.header, analyzer.data

# Initialisiere den CSVExporter mit den analysierten Daten
exporter = CSVExporter(data, header)

# Exportiere in verschiedene Formate mit Print-Befehlen
print("Exportiere in CSV...")
exporter.export_to_csv(os.path.join(output_dir, 'output.csv'))
print("CSV wurde erstellt.")

print("Exportiere in JSON...")
exporter.export_to_json(os.path.join(output_dir, 'output.json'))
print("JSON wurde erstellt.")

print("Exportiere in Excel...")
exporter.export_to_excel(os.path.join(output_dir, 'output.xlsx'))
print("Excel wurde erstellt.")

print("Exportiere in HTML...")
exporter.export_to_html(os.path.join(output_dir, 'output.html'))
print("HTML wurde erstellt.")

print("Exportiere in Parquet...")
exporter.export_to_parquet(os.path.join(output_dir, 'output.parquet'))
print("Parquet wurde erstellt.")

print("Exportiere in Markdown...")
exporter.export_to_markdown(os.path.join(output_dir, 'output.md'))
print("Markdown wurde erstellt.")

print("Exportiere in LaTeX...")
exporter.export_to_latex(os.path.join(output_dir, 'output.tex'))
print("LaTeX wurde erstellt.")

print("Exportiere in PDF...")
exporter.export_to_pdf(os.path.join(output_dir, 'output.pdf'))
print("PDF wurde erstellt.")

# Exportiere in eine SQLite-Datenbank
print("Exportiere in SQLite-Datenbank...")
conn = sqlite3.connect(os.path.join(output_dir, 'output.db'))
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS data_table (' + ', '.join([f'"{col}" TEXT' for col in header]) + ')')
exporter.export_to_sql('data_table', cursor)
conn.commit()
conn.close()
print("SQLite-Datenbank wurde erstellt.")

# Weitere Exportformate
print("Exportiere in XML...")
exporter.export_to_xml(os.path.join(output_dir, 'output.xml'))
print("XML wurde erstellt.")

print("Exportiere in YAML...")
exporter.export_to_yaml(os.path.join(output_dir, 'output.yaml'))
print("YAML wurde erstellt.")

print("Exportiere in Feather...")
exporter.export_to_feather(os.path.join(output_dir, 'output.feather'))
print("Feather wurde erstellt.")

print("Exportiere in HDF5...")
exporter.export_to_hdf5(os.path.join(output_dir, 'output.hdf5'))
print("HDF5 wurde erstellt.")

print("Exportiere in MessagePack...")
exporter.export_to_msgpack(os.path.join(output_dir, 'output.msgpack'))
print("MessagePack wurde erstellt.")

print("Exportiere in Pickle...")
exporter.export_to_pickle(os.path.join(output_dir, 'output.pickle'))
print("Pickle wurde erstellt.")

print("Erstelle SQLite-Dump...")
exporter.export_to_sqlite_dump(os.path.join(output_dir, 'output.sqlite.dump'))
print("SQLite-Dump wurde erstellt.")

print("Exportiere in CSV-Zip...")
exporter.export_to_csv_zip(os.path.join(output_dir, 'output.csv.zip'))
print("CSV-Zip wurde erstellt.")

# Mehrere Excel-Blätter
print("Exportiere in Excel mit mehreren Blättern...")
exporter.export_to_excel_multi_sheet(os.path.join(output_dir, 'output_multi_sheet.xlsx'), ['Sheet1', 'Sheet2'])
print("Excel mit mehreren Blättern wurde erstellt.")

# Komprimierte Formate
print("Exportiere in CSV-Gzip...")
exporter.export_to_csv_gzip(os.path.join(output_dir, 'output.csv.gz'))
print("CSV-Gzip wurde erstellt.")

print("Exportiere in CSV-Bzip2...")
exporter.export_to_csv_bzip2(os.path.join(output_dir, 'output.csv.bz2'))
print("CSV-Bzip2 wurde erstellt.")
