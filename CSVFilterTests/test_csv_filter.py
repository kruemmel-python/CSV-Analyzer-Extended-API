from csv_analyzer_extended import CSVFilter
from pprint import pprint

# Initialisiere den CSVFilter mit der erstellten CSV-Datei
csv_filter = CSVFilter(file_path="test_data.csv")

# 1. Filter nach einem numerischen Bereich (z.B. Alter zwischen 30 und 60)
print("Filter nach Alter zwischen 30 und 60:")
filtered_data = csv_filter.filter_by_numeric_range("Alter", min_value=30, max_value=60)
pprint(filtered_data)

# 2. Filter nach Textmuster (Nachname beginnt mit 'B')
print("\nFilter nach Nachnamen, die mit 'B' beginnen:")
filtered_data = csv_filter.filter_by_text_pattern("Nachname", "^B")
pprint(filtered_data)

# 3. Filter nach Datumsbereich (Datum zwischen 2020-08-01 und 2020-12-31)
print("\nFilter nach Datum zwischen 2020-08-01 und 2020-12-31:")
filtered_data = csv_filter.filter_by_date_range("Datum", "2020-08-01", "2020-12-31")
pprint(filtered_data)

# 4. Custom Filter (Bewertung größer als 4)
print("\nCustom Filter: Bewertung größer als 4:")
filtered_data = csv_filter.filter_by_custom_function("Bewertung", lambda x: float(x) > 4)
pprint(filtered_data)

# 5. Normalisierung einer Spalte (Einkommen)
print("\nNormalisiere Einkommen:")
normalized_data = csv_filter.normalize_column("Einkommen")
pprint(normalized_data)

# 6. Ranken der Spalte (Alter)
print("\nRänge für Alter:")
ranked_data = csv_filter.rank_column("Alter")
pprint(ranked_data)

# 7. Bedingte Filterkette (z.B. Alter > 30 und Bewertung >= 3)
print("\nBedingte Filterkette (Alter > 30 und Bewertung >= 3):")
conditions = [("Alter", ">", 30), ("Bewertung", ">=", 3)]
filtered_data = csv_filter.filter_by_condition_chain(conditions)
pprint(filtered_data)

# 8. Joins (Inner Join)
# Erstellen eines zweiten Datensatzes zum Testen
other_data = [
    ['1', 'Charlie', 'Koch', 'C', 'IT'],
    ['2', 'Julia', 'Becker', 'C', 'Marketing'],
    ['3', 'Ivan', 'Wagner', 'A', 'HR'],
    ['4', 'Emma', 'Schäfer', 'B', 'Finance'],
    ['5', 'George', 'Schmidt', 'B', 'Sales']
]
other_header = ['ID', 'Vorname', 'Nachname', 'Kategorie', 'Abteilung']

other_filter = CSVFilter(data=other_data, header=other_header)

print("\nInner Join mit zweitem Datensatz auf 'ID':")
joined_data = csv_filter.inner_join(other_filter, "ID")
pprint(joined_data)

# 9. Left Join
print("\nLeft Join mit zweitem Datensatz auf 'ID':")
left_joined_data = csv_filter.left_join(other_filter, "ID")
pprint(left_joined_data)

# 10. Group by Kategorie und Berechne Durchschnittsalter
print("\nGroup by Kategorie (Durchschnittsalter):")
grouped_data = csv_filter.group_by("Kategorie", lambda rows: sum(float(row[4]) for row in rows) / len(rows))
pprint(grouped_data)

# 11. Sortieren nach Einkommen
print("\nSortieren nach Einkommen:")
sorted_data = csv_filter.order_by("Einkommen", ascending=False)
pprint(sorted_data)

# 12. Limit auf die ersten 3 Datensätze
print("\nErste 3 Datensätze:")
limited_data = csv_filter.limit(3)
pprint(limited_data)

# 13. Aggregationen (Summe, Durchschnitt, Min, Max auf Einkommen)
print("\nSumme des Einkommens:")
print(csv_filter.sum("Einkommen"))

print("\nDurchschnitt des Einkommens:")
print(csv_filter.average("Einkommen"))

print("\nMinimalwert des Einkommens:")
print(csv_filter.min("Einkommen"))

print("\nMaximalwert des Einkommens:")
print(csv_filter.max("Einkommen"))

# 14. Set-Operationen (Union)
other_set_data = [
    ['1', 'Charlie', 'Koch', 'C', '26', '3477.21', '4.4', '2020-05-31'],
    ['11', 'Paul', 'Müller', 'D', '35', '3200.00', '3.5', '2020-09-15']
]

print("\nUnion mit anderem Datensatz:")
union_data = csv_filter.union(other_set_data)
pprint(union_data)

# 15. Window-Funktion (Kumulatives Einkommen)
print("\nKumulatives Einkommen:")
cumsum_data = csv_filter.cumulative_sum("Einkommen")
pprint(cumsum_data)

# 16. Anomalie-Erkennung (Isolation Forest auf Einkommen)
print("\nAnomalie-Erkennung mit Isolation Forest auf Einkommen:")
anomalies = csv_filter.detect_anomalies_isolation_forest("Einkommen")
pprint(anomalies)
