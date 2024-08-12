### README.md für `csv_analyzer_extended` API

---

## Übersicht

Die `csv_analyzer_extended`-API ist eine umfassende Python-Bibliothek, die entwickelt wurde, um CSV-Daten effizient zu verarbeiten, zu analysieren und zu manipulieren. Diese Bibliothek unterstützt verschiedene Datenverarbeitungsoperationen, einschließlich Filterung, Sortierung, Zusammenfassung und Export in verschiedene Formate. Zusätzlich integriert sie fortschrittliche Funktionen wie Multiprocessing und Speicher-Mapping-Operationen, um große Datensätze effizient zu verarbeiten.

---

## Installation

Um die `csv_analyzer_extended`-API zu installieren, entpacken Sie einfach die bereitgestellte `csv_analyzer_extended-1.1.zip` Datei und führen Sie folgenden Befehl aus:

```bash
pip install csv_analyzer_extended-1.1.zip
```

Die aktuellste Version ist direkt über pip installierbar:

[PyPI: csv-analyzer-extended 1.2](https://pypi.org/project/csv-analyzer-extended/1.2/)

```bash
pip install csv-analyzer-extended==1.2
```

---

## Module Übersicht

### 1. `summarizer.py`

Die `CSVSummarizer`-Klasse bietet eine breite Palette an Funktionen zur Analyse und statistischen Auswertung von CSV-Daten, darunter:

- **most_frequent_values(column_name)**: Findet den häufigsten Wert in einer Spalte.
- **find_outliers(column_name, threshold=1.5)**: Ermittelt Ausreißer in einer Spalte basierend auf dem Interquartilsabstand (IQR).
- **create_histogram(column_name, bins=10)**: Erstellt ein Histogramm für eine numerische Spalte.
- **calculate_sum(column_name)**: Berechnet die Summe der Werte in einer Spalte.
- **calculate_max(column_name)**: Bestimmt den maximalen Wert in einer Spalte.
- **calculate_min(column_name)**: Bestimmt den minimalen Wert in einer Spalte.
- **calculate_mean(column_name)**: Berechnet den Durchschnittswert einer Spalte.
- **calculate_median(column_name)**: Bestimmt den Medianwert in einer Spalte.
- **calculate_mode(column_name)**: Bestimmt den Modus und die Häufigkeit des häufigsten Wertes in einer Spalte.
- **calculate_variance(column_name)**: Berechnet die Varianz einer Spalte.
- **calculate_std_dev(column_name)**: Berechnet die Standardabweichung einer Spalte.
- **calculate_range(column_name)**: Berechnet die Spannweite (Range) einer Spalte.
- **calculate_percentile(column_name, percentile)**: Bestimmt einen bestimmten Perzentilwert einer Spalte.
- **calculate_z_scores(column_name)**: Berechnet die Z-Scores (Standardisierte Werte) für eine Spalte.
- **parallel_calculate_sum(column_name)**: Nutzt Multiprocessing, um die Summe der Werte in einer Spalte parallel zu berechnen.
- **mmap_calculate_sum(column_name, file_path)**: Verwendet Speicher-Mapping, um die Summe der Werte in einer großen Datei effizient zu berechnen.
- **mmap_calculate_max(column_name, file_path)**: Verwendet Speicher-Mapping, um den maximalen Wert in einer großen Datei effizient zu berechnen.

### 2. `analyzer.py`

Die `CSVAnalyzer`-Klasse bietet verschiedene Funktionen zur Analyse, Bereinigung und statistischen Auswertung von CSV-Daten:

- **__init__(file_path)**: Initialisiert den Analyzer mit dem Pfad zur CSV-Datei.
- **analyze_and_export(column_name, output_file)**: Analysiert eine Spalte und exportiert die Ergebnisse als CSV.
- **incremental_median(column_name)**: Berechnet den Median einer Spalte inkrementell.
- **calculate_std_dev(column_name)**: Berechnet die Standardabweichung einer Spalte.
- **calculate_variance(column_name)**: Berechnet die Varianz einer Spalte.
- **detect_anomalies_simple(column_name, threshold=1.5)**: Ermittelt einfache Anomalien in einer Spalte.
- **calculate_correlation(col1, col2, method='pearson')**: Berechnet die Korrelation zwischen zwei Spalten.
- **linear_regression(target_col, *feature_cols)**: Führt eine lineare Regression durch.
- **remove_duplicates()**: Entfernt doppelte Einträge.
- **fill_missing_values(column_name, strategy="mean")**: Füllt fehlende Werte in einer Spalte auf.
- **normalize_column(column_name)**: Normalisiert die Werte einer Spalte.
- **standardize_column(column_name)**: Standardisiert die Werte einer Spalte.
- **parallel_analyze_column(column_name, num_threads=4)**: Führt eine parallele Analyse einer Spalte durch.
- **memory_mapped_analyze(column_name)**: Analysiert eine Spalte mithilfe von Speicher-Mapping.
- **index_column(column_name)**: Erstellt einen Index für eine Spalte, um Abfragen zu beschleunigen.

### 3. `sorter.py`

Die `CSVSorter`-Klasse behandelt Sortieroperationen:

- **sort_by_column(column_name, reverse=False)**: Sortiert Daten nach einer einzelnen Spalte.
- **multi_column_sort(column_names, reverse=False)**: Sortiert Daten nach mehreren Spalten.
- **parallel_sort(column_name, num_threads=4, reverse=False)**: Nutzt Multiprocessing für paralleles Sortieren.
- **memory_mapped_sort(column_name, file_path, reverse=False)**: Nutzt Speicher-Mapping, um große Dateien effizient zu sortieren.
- **multiprocessing_sort(column_name, reverse=False)**: Sortiert Daten mithilfe von Multiprocessing.
- **optimized_sort(column_name, file_path=None, reverse=False, use_parallel=True)**: Bietet eine optimierte Sortierung mit mehreren Optionen.

### 4. `filter.py`

Die `CSVFilter`-Klasse bietet umfangreiche Filter- und Abfragefunktionen:

- **filter_by_numeric_range(column_name, min_value=None, max_value=None)**: Filtert Zeilen basierend auf einem numerischen Bereich.
- **filter_by_text_pattern(column_name, pattern)**: Filtert Zeilen basierend auf einem Textmuster (Regex).
- **filter_by_date_range(column_name, start_date, end_date, date_format='%Y-%m-%d')**: Filtert Zeilen basierend auf einem Datumsbereich.
- **filter_by_custom_function(column_name, custom_func)**: Filtert Zeilen basierend auf einer benutzerdefinierten Funktion.
- **normalize_column(column_name)**: Normalisiert die Werte in einer Spalte.
- **rank_column(column_name)**: Ordnet die Werte in einer Spalte nach Rang.
- **filter_by_condition_chain(conditions)**: Filtert Daten basierend auf einer Kette von Bedingungen.
- **multidimensional_filter(filters)**: Führt eine flexible Filterung basierend auf mehreren Kriterien durch.
- **inner_join(other, column_name)**: Führt einen Inner Join mit einem anderen Datensatz durch.
- **left_join(other, column_name)**: Führt einen Left Join mit einem anderen Datensatz durch.
- **right_join(other, column_name)**: Führt einen Right Join mit einem anderen Datensatz durch.
- **full_outer_join(other, column_name)**: Führt einen Full Outer Join mit einem anderen Datensatz durch.
- **select_columns(column_names)**: Wählt bestimmte Spalten aus den Daten aus.
- **where(column_name, condition)**: Filtert die Daten basierend auf einer Bedingung.
- **group_by(column_name, agg_func)**: Gruppiert die Daten nach einer Spalte und wendet eine Aggregatfunktion an.
- **order_by(column_name, ascending=True)**: Sortiert die Daten nach einer bestimmten Spalte.
- **limit(n)**: Gibt die ersten n Zeilen der Daten zurück.
- **count(column_name)**: Zählt die Einträge in einer Spalte.
- **sum(column_name)**: Berechnet die Summe der Werte in einer Spalte.
- **average(column_name)**: Berechnet den Durchschnitt der Werte in einer Spalte.
- **min(column_name)**: Findet den minimalen Wert in einer Spalte.
- **max(column_name)**: Findet den maximalen Wert in einer Spalte.
- **cumulative_sum(column_name)**: Berechnet die kumulative Summe einer Spalte.
- **cumulative_avg(column_name)**: Berechnet den kumulativen Durchschnitt einer Spalte.
- **rank(column_name)**: Ordnet die Werte in einer Spalte nach Rang.
- **dense_rank(column_name)**: Ordnet die Werte in einer Spalte nach Rang (ohne Lücken).
- **union(other_data)**: Vereint zwei Datensätze.
- **intersection(other_data)**: Gibt die Schnittmenge zweier Datensätze zurück.
- **difference(other_data)**: Gibt die Differenz zweier Datensätze zurück.
- **subquery(subquery_function, *args)**: Führt eine verschachtelte Abfrage durch.
- **exists(subquery_function, *args)**: Überprüft das Vorhandensein einer verschachtelten Abfrage.
- **in_(subquery_function, *args)**: Überprüft, ob ein Wert in den Ergebnissen einer verschachtelten Abfrage vorhanden ist.
- **self_join(column_name)**: Führt einen Self Join mit sich selbst durch.
- **cross_join(other_data)**: Führt einen Kreuzprodukt-Join mit einem anderen Datensatz durch.
- **case_when(conditions)**: Führt bedingte Abfragen durch

.
- **pivot(index_column, columns_column, values_column)**: Erstellt eine Pivot-Tabelle.
- **unpivot(columns)**: Macht eine Pivot-Tabelle rückgängig.
- **rolling_window(column_name, window_size, agg_func)**: Führt eine rollende Berechnung durch.
- **time_series_forecast(column_name, method='mean')**: Führt eine Zeitreihenprognose durch.
- **z_score(column_name)**: Berechnet die Z-Scores einer Spalte.
- **percentile(column_name, percentile)**: Berechnet den Perzentilwert einer Spalte.
- **correlation_matrix(columns)**: Berechnet die Korrelationsmatrix für mehrere Spalten.
- **contains_text(column_name, text)**: Filtert Zeilen, die einen bestimmten Text enthalten.
- **starts_with(column_name, prefix)**: Filtert Zeilen, die mit einem bestimmten Text beginnen.
- **ends_with(column_name, suffix)**: Filtert Zeilen, die mit einem bestimmten Text enden.

### 5. `exporter.py`

Die `CSVExporter`-Klasse bietet umfangreiche Exportfunktionen:

- **export_to_csv(file_path)**: Exportiert die Daten in eine CSV-Datei.
- **export_to_json(file_path)**: Exportiert die Daten in eine JSON-Datei.
- **export_to_excel(file_path)**: Exportiert die Daten in eine Excel-Datei.
- **export_to_html(file_path)**: Exportiert die Daten in eine HTML-Tabelle.
- **export_to_parquet(file_path)**: Exportiert die Daten im Parquet-Format.
- **export_to_markdown(file_path)**: Exportiert die Daten in eine Markdown-Tabelle.
- **export_to_latex(file_path)**: Exportiert die Daten in eine LaTeX-Tabelle.
- **export_to_pdf(file_path)**: Exportiert die Daten in eine PDF-Datei.
- **export_to_sql(table_name, cursor)**: Exportiert die Daten in eine SQL-Datenbank.
- **export_to_xml(file_path)**: Exportiert die Daten in eine XML-Datei.

### 6. `helper.py`

Die `CSVAnalyzerHelp`-Klasse bietet eine einfache Möglichkeit, die verfügbaren Funktionen der API anzuzeigen und Unterstützung zu erhalten:

- **show_help()**: Zeigt eine Übersicht und Hilfe für die Verwendung der `csv_analyzer_extended` API an. Diese Methode gibt eine detaillierte Liste der verfügbaren Klassen und ihrer Methoden zurück, die in der API enthalten sind.

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

