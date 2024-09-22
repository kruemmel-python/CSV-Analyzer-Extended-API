from csv_analyzer_extended import CSVClustering
from pprint import pprint

# Beispiel-Daten für das Clustering
data = [
    ['1', 'Charlie', 'Koch', 'C', '26', '3477.21', '4.4', '2020-05-31'],
    ['2', 'Julia', 'Becker', 'C', '65', '4651.88', '3.0', '2020-08-22'],
    ['3', 'Ivan', 'Wagner', 'A', '49', '3678.19', '4.4', '2020-08-13'],
    ['4', 'Emma', 'Schäfer', 'B', '27', '3739.59', '2.4', '2020-12-19'],
    ['5', 'George', 'Schmidt', 'B', '36', '21794.09', '5.43', '2020-10-14'],
    ['6', 'David', 'Becker', 'C', '59', '22020.36', '8.17', '2020-11-26'],
    ['7', 'Kevin', 'Schmidt', 'A', '24', '16076.86', '9.70', '2020-03-17'],
    ['8', 'Nina', 'Schäfer', 'C', '73', '24670.61', '5.09', '2020-10-20'],
    ['9', 'Anna', 'Hoffmann', 'A', '43', '49715.26', '8.71', '2020-11-18'],
    ['10', 'Ben', 'Weber', 'C', '52', '24468.02', '9.30', '2020-12-27']
]
header = ['ID', 'Vorname', 'Nachname', 'Kategorie', 'Alter', 'Einkommen', 'Bewertung', 'Datum']

# Initialisiere den CSVClustering mit den Beispieldaten
clustering = CSVClustering(data, header)

# Liste der Algorithmen, die getestet werden sollen
algorithms = ['kmeans', 'agglomerative', 'dbscan', 'gmm', 'mean_shift', 'spectral', 'affinity_propagation', 
              'hierarchical', 'isolation_forest', 'lof', 'one_class_svm', 'elliptic_envelope', 'birch']

# Spalten, die für das Clustering verwendet werden (z.B. 'Alter' und 'Einkommen')
columns_to_cluster = ['Alter', 'Einkommen']

# Teste jeden Algorithmus
for algo in algorithms:
    print(f"\nClustering mit {algo}:")
    try:
        if algo in ['kmeans', 'agglomerative', 'gmm', 'spectral', 'birch']:
            labels = clustering.cluster_data(algo, 3, *columns_to_cluster)  # 3 Cluster für diese Algorithmen
        else:
            labels = clustering.cluster_data(algo, None, *columns_to_cluster)
        pprint(labels)
    except Exception as e:
        print(f"Fehler bei {algo}: {e}")
