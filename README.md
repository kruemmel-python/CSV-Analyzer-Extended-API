### README.md für `csv_analyzer_extended` API

---

## Übersicht

Die `csv_analyzer_extended`-API ist eine umfassende Python-Bibliothek, die entwickelt wurde, um CSV-Daten effizient zu verarbeiten, zu analysieren und zu manipulieren. Diese Bibliothek unterstützt verschiedene Datenverarbeitungsoperationen, einschließlich Filterung, Sortierung, Zusammenfassung und Export in verschiedene Formate. Zusätzlich integriert sie fortschrittliche Funktionen wie Multiprocessing und speicher-mapping-Operationen, um große Datensätze effizient zu verarbeiten.

---

## Installation

Um die `csv_analyzer_extended`-API zu installieren, entpacken Sie einfach die bereitgestellte `csv_analyzer_extended-1.1.zip` Datei und führen Sie folgenden Befehl aus:

```bash
pip install csv_analyzer_extended-1.1.zip
```
Die aktuellste Version ist direkt über pip installierbar:

https://pypi.org/project/csv-analyzer-extended/1.2/
```bash
pip install csv-analyzer-extended==1.2
```
---

## Module Übersicht

### 1. `summarizer.py`
Die `CSVSummarizer`-Klasse bietet Funktionen zur Berechnung verschiedener Statistiken und Zusammenfassungen für CSV-Daten, wie zum Beispiel:

- **most_frequent_values**: Findet den häufigsten Wert in einer Spalte.
- **find_outliers**: Ermittelt Ausreißer mittels Interquartilsabstand (IQR).
- **calculate_sum**, **calculate_max**, **calculate_min**: Grundlegende Aggregationsfunktionen.
- **calculate_mean**, **calculate_median**, **calculate_mode**: Maßzahlen der zentralen Tendenz.
- **calculate_variance**, **calculate_std_dev**: Streuungsmaße.
- **parallel_calculate_sum**: Nutzt Multiprocessing zur Beschleunigung der Summenberechnung.
- **mmap_calculate_sum**, **mmap_calculate_max**: Verwendet speicher-mapping für effiziente Verarbeitung großer Dateien.

### 2. `analyzer.py`
Die `CSVAnalyzer`-Klasse bietet verschiedene Analysefunktionen, wie zum Beispiel:

- **analyze_and_export**: Analysiert eine Spalte und exportiert die Ergebnisse als CSV.
- **incremental_median**: Berechnet den Median inkrementell.
- **calculate_std_dev**, **calculate_variance**: Maße der Streuung.
- **calculate_correlation**: Berechnet Pearson- oder Spearman-Korrelation.
- **linear_regression**: Führt eine lineare Regressionsanalyse durch.
- **parallel_analyze_column**: Analysiert Daten mit mehreren Threads.
- **memory_mapped_analyze**: Analysiert Daten mittels speicher-mapping.
- **index_column**: Erstellt einen Index für schnelleren Datenzugriff.

### 3. `filter.py`
Die `CSVFilter`-Klasse bietet Filter- und erweiterte Abfragefunktionen:

- **filter_by_numeric_range**, **filter_by_text_pattern**, **filter_by_date_range**: Filtert Zeilen basierend auf Bedingungen.
- **normalize_column**, **rank_column**: Daten-Normalisierung und Ranking.
- **inner_join**, **left_join**, **right_join**, **full_outer_join**: Verknüpft Datensätze miteinander.
- **group_by**: Gruppiert Daten nach einer bestimmten Spalte und wendet eine Aggregationsfunktion an.
- **set_operations**: Mengenoperationen wie Vereinigung, Schnittmenge und Differenz.
- **pivot**, **unpivot**: Transformiert Daten zwischen langen und breiten Formaten.
- **time_series_forecast**: Grundlegende Prognosemethoden für Zeitreihen.

### 4. `sorter.py`
Die `CSVSorter`-Klasse behandelt Sortieroperationen:

- **sort_by_column**: Sortiert Daten nach einer einzelnen Spalte.
- **multi_column_sort**: Sortiert Daten nach mehreren Spalten.
- **parallel_sort**: Nutzt Multiprocessing für paralleles Sortieren.

### 5. `exporter.py`
Die `CSVExporter`-Klasse bietet Funktionen zum Exportieren von Daten:

- **export_to_csv**, **export_to_json**, **export_to_excel**: Exportiert Daten in gängige Formate.
- **export_to_html**, **export_to_markdown**, **export_to_latex**: Konvertiert Daten in Markup-Sprachen.
- **export_to_parquet**: Exportiert Daten im Parquet-Format mit Apache Arrow.
- **export_to_pdf**: Generiert einen PDF-Bericht aus den Daten.
- **export_to_sql**: Fügt Daten in eine SQL-Datenbank ein.
- **export_to_xml**: (Geplant/Wird hinzugefügt) Konvertiert und exportiert Daten in das XML-Format.

---

## Test Suite

Die API wird mit einer umfassenden Test-Suite geliefert, die die Funktionalität aller Klassen validiert. Die Testdateien sind nach den Modulen organisiert, die sie testen, und stellen sicher, dass alle Methoden unter verschiedenen Bedingungen korrekt funktionieren.

Um die Tests auszuführen, navigieren Sie zum Testverzeichnis und führen Sie folgenden Befehl aus:

```bash
python -m unittest discover
```

### Testdateien:

- **Test Summarizer**: Testet alle statistischen Funktionen in `summarizer.py`.
- **Test Analyzer**: Testet Analysefunktionen, Datenbereinigung und Methoden zur Parallelverarbeitung.
- **Test Filter**: Validiert die Filter- und Abfragefunktionen von `filter.py`.
- **Test Sorter**: Stellt sicher, dass die Sortierfunktionen, einschließlich Multi-Column- und Parallelsortierung, korrekt funktionieren.
- **Test Exporter**: Testet den Datenexport in verschiedene Formate, einschließlich CSV, JSON, Excel, PDF und mehr.

---

## Anwendungsbeispiel

Hier ist ein einfaches Beispiel, um Ihnen den Einstieg zu erleichtern:

```python
from csv_analyzer_extended import CSVAnalyzer, CSVFilter, CSVSorter, CSVSummarizer, CSVExporter

# Daten laden und analysieren
analyzer = CSVAnalyzer('data.csv')
summarizer = CSVSummarizer(analyzer.data, analyzer.header)

# Berechnung grundlegender Statistiken
mean_value = summarizer.calculate_mean('Spaltenname')
print("Durchschnittswert:", mean_value)

# Daten filtern
filter = CSVFilter(analyzer.data, analyzer.header)
gefilterte_daten = filter.filter_by_numeric_range('Spaltenname', min_value=10)

# Daten sortieren
sorter = CSVSorter(gefilterte_daten, analyzer.header)
sortierte_daten = sorter.sort_by_column('Spaltenname')

# Ergebnisse exportieren
exporter = CSVExporter(sortierte_daten, analyzer.header)
exporter.export_to_csv('sortierte_daten.csv')
```

---

## Mitwirken

Beiträge sind willkommen! Bitte forken Sie das Repository und senden Sie einen Pull-Request mit Ihren Änderungen.

---

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.

