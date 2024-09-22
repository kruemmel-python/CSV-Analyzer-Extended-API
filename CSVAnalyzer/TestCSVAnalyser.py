from csv_analyzer_extended import CSVAnalyzer

# Initialisiere den Analyzer mit der CSV-Datei
analyzer = CSVAnalyzer("test_data.csv")

# Beispiel: Analysiere eine Spalte und exportiere sie
analyzer.analyze_and_export("Einkommen", "analyze_einkommen_output.csv")

# Berechne den Median für eine Spalte
median = analyzer.incremental_median("Alter")
print(f"Median für 'Alter': {median}")

# Berechne die Standardabweichung für eine Spalte
std_dev = analyzer.calculate_std_dev("Bewertung")
print(f"Standardabweichung für 'Bewertung': {std_dev}")

# Berechne die Varianz für eine Spalte
variance = analyzer.calculate_variance("Einkommen")
print(f"Varianz für 'Einkommen': {variance}")

# Detektiere einfache Anomalien in der Spalte "Einkommen"
anomalies = analyzer.detect_anomalies_simple("Einkommen")
print("Anomalien in 'Einkommen':")
for anomaly in anomalies:
    print(anomaly)

# Berechne die Pearson-Korrelation zwischen "Alter" und "Einkommen"
correlation = analyzer.calculate_correlation("Alter", "Einkommen", method='pearson')
print(f"Pearson-Korrelation zwischen 'Alter' und 'Einkommen': {correlation}")

# Lineare Regression auf "Bewertung" basierend auf "Alter" und "Einkommen"
coefficients, intercept = analyzer.linear_regression("Bewertung", "Alter", "Einkommen")
print(f"Lineare Regressionskoeffizienten: {coefficients}, Intercept: {intercept}")

# Entferne doppelte Zeilen
analyzer.remove_duplicates()
print("Duplikate entfernt.")

# Fehlende Werte auffüllen (zum Beispiel in "Bewertung")
analyzer.fill_missing_values("Bewertung", strategy="mean")
print("Fehlende Werte in 'Bewertung' aufgefüllt.")

# Spalte "Einkommen" normalisieren
analyzer.normalize_column("Einkommen")
print("Spalte 'Einkommen' normalisiert.")

# Spalte "Alter" standardisieren
analyzer.standardize_column("Alter")
print("Spalte 'Alter' standardisiert.")

# Spalte parallel analysieren
parallel_results = analyzer.parallel_analyze_column("Einkommen")
print("Parallele Analyse der Spalte 'Einkommen':")
print(parallel_results)

# Memory-Mapped Analyse der Spalte "Einkommen"
memory_mapped_result = analyzer.memory_mapped_analyze("Einkommen")
print(f"Memory-mapped Analyse für 'Einkommen': {memory_mapped_result}")

# T-Test zwischen den Spalten "Einkommen" und "Bewertung"
t_stat, p_value = analyzer.t_test("Einkommen", "Bewertung")
print(f"T-Test Ergebnis zwischen 'Einkommen' und 'Bewertung': T-Statistik = {t_stat}, P-Wert = {p_value}")

# Indiziere die Spalte "Kategorie"
index_map = analyzer.index_column("Kategorie")
print(f"Index für 'Kategorie': {index_map}")
