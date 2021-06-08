# studienarbeit
Code der Studienarbeit

Syntax des JSON-Generators:<br>
printjson druckt eine JSON-Datei<br>
exit beendet das Programm

Befehl zum Erstellen eines Knotens:<br>
node NAME = TYP (PARAMETER1, PARAMETER2, ...)

NAME gibt den Namen zur Referenzierung des Knotens an<br>
TYP ist ein Knotentyp(Knotentyp+Einstellung wie ADD, Liste an Typen ist unten sichtbar<br>
    nodeTypes = "Uniform","Normal","Exponential","Percentage","AND","OR","XOR","NAND","NOR","XNOR","Equals","Greater","Smaller","GreaterThan","SmallerThan","Add","Subtract","Multiply","Divide","Sine","Cosine","Tangent","Arcsine","Arccosine","Arctangent","Power","Logarithm","Minimum","Maximum","Round","Modulo","Absolute","Output" <br>
PARAMETER steht für die einzelnen Parameter Werte. Zahlen, Booleans und Strings können direkt eingegeben werden. Wenn der Outputwert eines anderen Knotens verwendet werden soll, muss ein * vor den Namen des Knotens eingefügt werden. Beispiel \*NAME <br>
Die Reihenfolge der Parameter entspricht der Reihenfolge der Interfaces in de GUI von oben nach unten.<br>

Beispielbefehle für die Multiplikation zweier Zufallszahlen:
node random = Normal("hallo",0,10,True)<br>
node zufall = Normal("hallo",0,10,True)<br>
node mul = Multiply(\*random,\*zufall)<br>
node out = Output(\*mul, Ergebnis)<br>
printjson<br>
exit<br>
