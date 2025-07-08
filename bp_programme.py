# Aufgabe 1:
# Schreiben Sie ein Programm, das den Benutzer nach seinem Namen, Alter und seiner Lieblingsfarbe fragt
# und anschließend folgendes ausgibt:
# "Ich heiße [Name], bin [Alter] Jahre alt und meine Lieblingsfarbe ist [Farbe]."
a = input("Enter your name: ")
b = input("Enter your age: ")
c = input("Enter your favorite color: ")
print("My name is", a, ", I am", b, "old and my favourite color -", c)
# Aufgabe 2:
# Schreiben Sie ein Programm, das die folgende Zeile auf verschiedene Arten ausgibt:
# Sie sagte: "Hallo!"
# (Hinweis: mindestens dreimal ausgeben, auf unterschiedliche Weise)
print("She said: Hi!\n" * 3)
print("She said: Hi!")
print("She said: Hi!")
print("She said: Hi!")
print(" ")
a = "She said: Hi!\n"
print(a * 3)
# Aufgabe 3:
# Schreiben Sie ein Programm, das folgenden Text ausgibt:
# To-Do-Liste:
# Lernen
# Aufräumen
# Sport
print("To-Do list:\n\tStudying\n\tCleaning\n\tGym")
# Aufgabe 4:
# Schreiben Sie ein Programm, das den Benutzer nach einer Entfernung in Kilometern und der Durchschnittsgeschwindigkeit fragt
# und berechnet, wie viel Zeit (in Stunden, als Dezimalzahl) für die Fahrt benötigt wird.
a = int(input("Enter the distance in km: "))
b = int(input("Enter the speed in km\\h: "))
time = a / b
print("The time is", time)
# Aufgabe 4.1:
# Erweitern Sie das vorherige Programm so, dass die Fahrzeit in Stunden und Minuten (ohne Nachkommastellen) angezeigt wird.
a = float(input("Enter the distance in km: "))
b = float(input("Enter the speed in km\\h: "))
time_in_hours = a / b
hours = int(time_in_hours)
minutes = int((time_in_hours - hours) * 60)
print("Time on the road", hours, "h and", minutes, "min")
# Aufgabe 5:
# Schreiben Sie ein Programm, das die Anzahl der verbleibenden Tage bis zu einem Ereignis abfragt
# und berechnet, wie viele Wochen und Tage das sind.
a = int(input("Enter the number of days until the event: "))
weeks = a // 7
days = a % 7
print("Time remaining until the event:", weeks, "weeks and", days, "days")
# Aufgabe 6:
# Schreiben Sie ein Programm, das folgende Eingaben vom Benutzer erwartet:
# - Entfernung in Kilometern
# - Benzinverbrauch auf 100 km
# - Preis pro Liter Benzin
# Das Programm soll die Gesamtkosten für die Fahrt berechnen.
km = int(input("Enter the distance: "))
fuel = int(input("Enter fuel consumption per 100 km: "))
price = int(input("Enter the price per liter of gasoline:"))
result = km / 100 * fuel * price
print("Cost of gasoline for the trip:", result, "liter")
# Aufgabe 7:
# Schreiben Sie ein Programm, das die Anzahl der Aufgaben und die durchschnittliche Bearbeitungszeit pro Aufgabe (in Minuten) abfragt
# und die Gesamtzeit in Stunden und Minuten ausgibt.
tasks = int(input("Enter the number of tasks: "))
min = int(input("Enter the average time required to complete one task (min): "))
hours = tasks * min // 60
minutes = tasks * min % 60
print("Total time:", hours, "h and", minutes, "min")
# Aufgabe 8:
# Schreiben Sie ein Programm, das eine Zahl „n“ einliest und den Ausdruck „n + nn + nnn“ berechnet.
# Beispiel: Wenn n = 5, dann wird 5 + 55 + 555 = 615
n = int(input("Enter the number: "))
result = n + n * 11 + n * 111
print("Meaning of the expression:", result)
# Aufgabe 9:
# Schreiben Sie ein Programm, das eine vierstellige Zahl einliest und die erste und letzte Ziffer vertauscht.
num = input("Enter the number:")
new_num = num[3] + num[1] + num[2] + num[0]
print("Number after change: ", new_num)
