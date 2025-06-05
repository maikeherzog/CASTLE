# Anpassungen zu CASTLE mithilfe des Originalen Codes zum Paper
In der ursprünglichen Python Implementierung auf dem main Branch konnten die im CASTLE Paper von Jianneng Cao et al., 2011 veröffentlichten Ergebnisse nicht komplett reproduziert werden. Aus diesem Grund wurde probiert mithilfe des originalen Codes, welcher uns von ... bereitgestellt wurde, unseren Code anzupassen und zu optimieren. Die dabei vorgenommenen Änderungen und Ergebnisse werden hier zusammengefasst.

## Inhalt

- [Unterschiede in der Benennung](#unterschiede-in-der-benennung)
- [Unterschiede bei den Funktionen](#unterschiede-bei-den-funktionen)
  - [best\_selection()](#best_selection)
  - [merge\_left\_clusters()](#merge_left_clusters)
- [Sonstige Beobachtungen](#sonstige-beobachtungen)
- [Weitere Fragen](#weitere-fragen)


## Unterschiede in der Benennung 
| Unser Code | Original Code | Benennung im Paper, Bedeutung |
|------------|---------------|----------|
|not_anonymized_clusters | _nonwork_clusters | $\Gamma$, set of non $k_s$-anonymized clusters|
|anonymized_clusters |_work_clusters|  $\Omega$, set of $k_s$-anonymized clusters|
|best_selection() | win() | best_selection(t), wählt für ein neues Tupel $t$ denjenigen nicht-$k_s$-anonymisierten Cluster aus, dessen Aufnahme den geringsten Vergrößerungsaufwand bei gleichzeitig akzeptabler Informationsverlustschwelle verursacht|
| beta | _upper_bound_clusters | $\beta$, Obergrenze für betrachtete Cluster|
| mu (default mäßig auf 100 gesetzt) | _recent | $\mu$, Anzahl der zuletzt betrachteten Tuple|

## Unterschiede bei den Funktionen
### best_selection()
- Im Python Code wird für ein Tuple t das Cluster gewählt mit dem geringsten Informationsverlusst. Gab es z.B. vor dem Tupel $t$ ein weiteres Tupel $t'$ mit den gleichen Quasiidentifikatoren, dann wurde bereits ein Cluster $C'$ über $t'$ gebildet. Da es zu keinem Informationsverlusst führen würde, wenn man $t$ nun ebenfalls in dieses Cluster einfügen würde, gibt die best_selection Funktion $C'$ zurück.
- In der originalen Implementierung funktioniert dies ein bisschen anders. Hier werden solange neue Cluster gebildet, bis die obere Grenze (upper_bound) an nicht $k_s$- anonymisierten Clustern erreicht ist. Dies bedeutet also für das Beispiel, dass für win(t) nicht $C'$ zurück gegeben werden würde, sondern ein neues Cluster $C$ gebildet werden würde, wenn die upper_bound noch nicht erreicht ist.
- Diese Änderung erzeugte im ersten Versuch einen um 0.3 verringerten Informationsverlusst. Leider konnten wir durch erneute Ausführungen die Ergebnisse nicht konstant bestätigen. Viellmehr schwankte der Informationsverlusst (s. Tabellen)

k= 100
|Nr. Versuch |ursprünglicher Code |angepasster Code |
|------------|---------------------|------------------|
|1. | 0.7559801693963233 | 0.19443310821245433|
|2. | 0.7346345492648588 | 0.6988945695238096|
|3. | 0.7805553846060732 | 0.779665486095238|
|4. | 0.7542863414633837 | 0.4887570263516478|
|5. | 0.754766446176423 | 0.7815961714285716

k= 200
|Nr. Versuch |ursprünglicher Code |angepasster Code |
|------------|---------------------|------------------|
|1. | 0.7583598714287436 | 0.35017010476190474|
|2. | 0.7844604490855808 | 0.8014276380952382|
|3. | 0.7866543361672433 | 0.7912696180000012|
|4. | 0.7585456782018238 | 0.19632439956043934|
|5. | 0.7669203470783847 | 0.8170390190476191|

- Wo wir bei $k=100$ den Informationsverlusst in jedem Versuch um wenigsten einen geringe Menge senken konnten, zeigen die Versuche bei $k=200$ auch Steigerungen
- Nach Überlegungen wodurch diese Schwankungen auftreten könnten, kam uns die Idee die Stellen im Code genauer zu untersuchen, die mit Zufall arbeiten. Dies betrifft die Funktionen delay_constraint() und split(). Leider konnten wir hier keine Unterschiede zwischen den Implementierungen finden und somit auch nicht den Grund für die Unterschiede.

### merge_left_clusters()
Diese Funktion aus dem Originalen Code behandelt die restlichen Cluster, welche noch nicht $k_s$-anonym sind, wenn der Stream fertig abgelaufen ist. Im Python Code ist das noch nicht mit beachtet. Dort endet der Code einfach, wenn der Stram durchgelaufen ist und die noch nicht $k_s$-anonymen Cluster verbleiben im Speicher.

## Sonstige Beobachtungen
In unserer Arbeit trafen wir die Aussage, dass es aus dem CASTLE Paper nicht eindeutig hervorgeht, wie der dargestellt Informationsverlusst genau berechnet wird. Durch den Original Code wurde ersichtlich, dass es sich um den durchschnittlichen Informationsverlusst handelt, der über den letzten $\mu$ Clustern berechnet wird. 

Der Informationsverlusst im Originalen Paper wird nicht normiert. Im Python Code hingegen wird es wie im Paper beschrieben immer direkt gemacht. Um also auf die gleichen Zahlen zu kommen, muss die berechnete Zahl aus dem Original Paper durch die Anzahl der Attribute rechnen, die für den Informationsverlusst verwendet wurden (warscheinlich die QI-Attribute).

Wir haben auch untersucht, wie mit Tupel umgegangen wird, welche ein Tupel in kein CLuster eingefügt werden kann, da z.B. der dadurch resultierende Informationsverlusst zu hoch wäre oder es nicht mehr genug Tupel gibt um ein weiteres Cluster zu bilden, dass $k_s$ anonym ist. Es gibt also weniger als $k$ Tupel von unterschiedlichen Personen. In solch einem Fall wird dieses Tupel unterdrückt. Im Originalen Code bedeutet unterdrücken einfach, dass das Tupel als unterdrückt makiert wird. Wird ein Tupel als Ausreißer erkannt, dann wird es gelöscht. 
Der Unterschied hierbei zu dem Python Code besteht darin, dass im Python Code unterdrückte Tuple einfach nicht mehr beachtet werden.

## Weitere Fragen
- Achten sie im Originalen Code bei Split darauf, dass es verschiedene Personen sind? Oder wird hier einfach davon ausgegangen, dass eine Person sowieso nur ein Tupel im gesammten Stream erzeugen kann?
