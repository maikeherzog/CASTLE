# CASTLE

## Überblick
Dieses Projekt implementiert den CASTLE (Continuously Anonymizing Streaming data via adaptive cLustEring) Algorithmus zur Anonymisierung von Streaming-Daten in IoT-Netzwerken. Der Algorithmus wurde basierend auf den in Jianneng Cao et al., 2011 veröffentlichten Verfahren entwickelt. Ziel dieses Projekts ist es, die Funktionsweise des CASTLE-Algorithmus zu reproduzieren und eine Grundlage zur Weiterentwicklung bereitzustellen. 

## Inhalt

- [Funktionen](#funktionen)
- [Installationsanweisungen](#installationsanweisungen)
- [Nutzung](#nutzung)
- [Beispiele](#beispiele)
- [Konfiguration](#konfiguration)
- [Projektstruktur](#projektstruktur)
- [Bekannte Probleme](#bekannte-probleme)
- [Zukünftige Arbeiten](#zukünftige-arbeiten)
- [Kontakt](#kontakt)

## Funktionen
- ***Anonymisierung von Streaming-Daten:*** Der CASTLE-Algorithmus anonymisiert kontinuierlich eintreffende Datenpunkte in Echtzeit.
- ***Anpassbare Hierarchie:*** Unterstützt benutzerdefinierte Generalisierungshierarchien für kategorische und kontinuierliche Attribute.
- ***Flexible Konfiguration:*** Ermöglicht die Konfiguration von Parametern wie der Anzahl der nicht-anonymisierten Cluster, der Anonymitätsstufe und die Verzögerungsbeschränkung.
- ***Modularer Aufbau:*** Ermöglicht die einfache Erweiterung des Algorithmus für zusätzliche Funktionalitäten.

## Installationsanweisungen
### Voraussetzungen
- Python 3.8+
### Installation
1. Klonen Sie das Repository:
   ```   git clone```

## Nutzung
1. Führen Sie die Datei `main.py` aus:
   ```python main.py```

## Beispiele
Beispiele zur Nutzung des CASTLE-Algorithmus finden Sie in der Datei `main.py`. Die genutzten Beispieldaten befinden sich im Ordner `data`. Die Beispiele zeigen verschiedene Varianten, wie der CASTLE Algorithmus genutzt werden kann.

## Konfiguration
### Parameter
- ***k:*** Der Parameter k bestimmt die Anonymitätsstufe.
- ***beta***: Der Parameter beta bestimmt die Anzahl der nicht-anonymisierten Cluster.
- ***delta***: Der Parameter delta bestimmt die Verzögerungsbeschränkung.
- ***stream***: Der Parameter stream enthält die zu anonymisierenden Datenpunkte.
- ***name_dataset:*** Der Parameter name_dataset enthält den Namen des verwendeten Datensatzes, so wie er im Dictionary `attribute_properties` definiert ist. Das Dictionary wird zur Zuordnung der Domänen zu den Attributen verwendet.

### Anpassung der Generalisierungshierarchie
Die Hierarchien für kategorische Attribute können in der Datei hierarchy_tree.py definiert und angepasst werden. Eine Zuordnung der Bäume zu den Attribute erfolgt im Dictionary `attribute_properties` in der Datei edit_data.py. Für die kontinuierlichen Attribute wird das Domainintervall ebenfalls im Dictionary `attribute_properties` definiert.

## Projektstruktur
Die Projektstruktur ist wie folgt aufgebaut:
```
castle/
│
├── data/                     # Beispieldaten
│
├── src/                      # Quellcode
│   ├── Castle.py/            # CASTLE Klasse
│   ├── edit_data.py/         # Funktionen zur Datenbearbeitung
│   ├── hierarchy_tree.py/    # Hierarchiebäume für kategorische Attribute
│   ├── Cluater.py/           # Cluster Klasse
│   ├── Data.py/              # Klasse für die Datentransformation
│   ├── HeapElement.py/       # Klasse für die HeapElemente
│   ├── tree_functions.py/    # Funktionen zur Bearbeitung der Hierarchiebäume
│   ├── Tuple.py/             # Klasse für die Repräsentation und Umwandlung der Datenpunkte
│
├── graph                     # Ordner für die Erstellung der Auswertungsdiagramme
│   ├── hist_plot.py/         # Funktionen zur erstellung der Histogramme
│   ├── plot_graph.py/        # Funktionen zur Erstellung der Graphen
│   ├── diverse Auswertungsdiagramme
│
├── test/                     # Testdateien
│   ├── test_Castle.py/       # Testfälle für die CASTLE Klasse
│   ├── test_Cluster.py/      # Testfälle für die Cluster Klasse
│   ├── test_Data.py/         # Testfälle für die Data Klasse
│   ├── test_HeapElement.py/  # Testfälle für die HeapElement Klasse
│   ├── test_Tuple.py/        # Testfälle für die Tuple Klasse
│
├── README.md                 # Dokumentation
├── main.py                   # Hauptdatei

```

## Bekannte Probleme
- ***Reihenfolge der Attribute:*** Die aktuelle Implementierung erfordert, dass die Reihenfolge der Attribute in den Datensätzen exakt definiert ist. Dies kann bei komplexen Datensätzen zu Problemen führen.
- ***Generalisierungshierarchie:*** Die Generalisierungshierarchie für kategorische Attribute muss händisch definiert werden. 

## Zukünftige Arbeiten
- ***Automatische Generalisierungshierarchie:*** Implementierung eines Algorithmus zur automatischen Generierung von Generalisierungshierarchien für kategorische Attribute.
- ***Erweiterung der Funktionalität:*** Erweiterung des Algorithmus um zusätzliche Funktionalitäten wie die Anonymisierung von Zeitreihendaten.
- ***Integration anderer Datenschutzmodelle:*** Integration anderer Datenschutzmodelle wie l-Diversität, t-Closeness oder Differential Privacy.

## Kontakt
Bei Fragen oder Anregungen wenden Sie sich bitte an die folgende E-Mail-Adresse: [maike.herzog@mailbox.tu-dresden.de](mailto:maike.herzog@mailbox.tu-dresden.de)


```