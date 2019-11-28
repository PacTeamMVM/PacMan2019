# PacMan2019
Napisati igricu nalik Pac-Man igrici. Napraviti šemu lavirinta, sličnu kao u originalnoj igrici,
kroz koje avatari mogu da se kreću.<br />
Uloge:<br />
  • Dva ili više igrača, pokreću svog avatara pomoću strelica, odnosno ASDW tastera:
o Kreću se gore-dole-levo-desno, kroz lavirint.
o Svaki igrač skuplja poene prelazeći preko kružića, koji potom nestaje.
o Na početku nivoa igrači se nalaze u ćoškovima lavirinta. Kružić nosi 10
poena.
o Svaki igrač ima 3 života po nivou. Kada izgubi život igrač se pojavi na
istom mestu odakle je započeo nivo.
• Neprijatelji:
o Kreći se nasumično gore-dole-levo-desno, kroz tunele.
o Na početku nivoa, nalaze se u središnjem delu u svojoj jazbini.
• Bonus:
o Na nasumično izabranom mestu iskače bonus. Kada se pokupi bonus,
neprijatelji se usporavaju, menjaju boju i postoji mogućnost da ih igrač
pojede i dobije 200 poena.
o Nakon nasumičnog vremena, neprijatelji se vraćaju u prvobitno stanje i
opet mogu da ubiju igrača.
Pravila:
• Igra se beskonačno nivoa (prihvatljivo je napraviti jedan nivo koji se igra
beskonačno mnogo puta).
• Ukoliko neprijatelj dodirne igrača, on gubi život.
• Nakon svakog nivoa neprijatelji se brže kreću.
• Za prelaz na sledeći nivo potrebno je uništiti sve neprijatelje i proći kroz neki od
izlaza iz lavirinta.
• Pobednik je igrač koji nakon gubitka svih života igrača ima najveći broj poena.
• Prikazivati u gornjem delu ekrana broj bodova svih igrača kao i broj života.
• Igrica se završava kada svi igrači izgube sve živote.
Za realizaciju koristiti Python3, PyQt5, multiprocessing. Raditi u timovima od 4
člana.Napisati dokumentaciju u kojoj opisuje opšti rad aplikacije i rezimirati prednosti i
mane korišćenja Python jezika, PyQt5 okvira i paralelizacije rada.<br />
Demo originalne igrice: https://www.youtube.com/watch?v=HQv0zAXDCo8
