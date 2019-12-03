# PacMan2019
Napisati igricu nalik Pac-Man igrici. Napraviti šemu lavirinta, sličnu kao u originalnoj igrici,
kroz koje avatari mogu da se kreću.<br />
Uloge:<br />
<ul>
  <li>Dva ili više igrača, pokreću svog avatara pomoću strelica, odnosno ASDW tastera:
    <ul>
      <li>Kreću se gore-dole-levo-desno, kroz lavirint.</li>
      <li>Svaki igrač skuplja poene prelazeći preko kružića, koji potom nestaje.</li>
<li>Na početku nivoa igrači se nalaze u ćoškovima lavirinta. Kružić nosi 10
  poena.</li>
<li>Svaki igrač ima 3 života po nivou. Kada izgubi život igrač se pojavi na
  istom mestu odakle je započeo nivo.</li></li></ul>

<li>Neprijatelji:
  <ul>
    <li>Kreći se nasumično gore-dole-levo-desno, kroz tunele.</li>
 <il>Na početku nivoa, nalaze se u središnjem delu u svojoj jazbini.</li></li></ul>
<li>Bonus:
  <ul>
<li>Na nasumično izabranom mestu iskače bonus. Kada se pokupi bonus,
neprijatelji se usporavaju, menjaju boju i postoji mogućnost da ih igrač
  pojede i dobije 200 poena.</li>
<li>Nakon nasumičnog vremena, neprijatelji se vraćaju u prvobitno stanje i
  opet mogu da ubiju igrača.</li></li></ul></ul>
<br />Pravila:
<ul>
<li>Igra se beskonačno nivoa (prihvatljivo je napraviti jedan nivo koji se igra
  beskonačno mnogo puta).</li>
  <li>Ukoliko neprijatelj dodirne igrača, on gubi život.</li>
  <li>Nakon svakog nivoa neprijatelji se brže kreću.</li>
<li>Za prelaz na sledeći nivo potrebno je uništiti sve neprijatelje i proći kroz neki od
  izlaza iz lavirinta.</li>
  <li>Pobednik je igrač koji nakon gubitka svih života igrača ima najveći broj poena.</li>
  <li>Prikazivati u gornjem delu ekrana broj bodova svih igrača kao i broj života.</li>
  <li>Igrica se završava kada svi igrači izgube sve živote.</li>
  </ul>
Za realizaciju koristiti Python3, PyQt5, multiprocessing. Raditi u timovima od 4
člana.Napisati dokumentaciju u kojoj opisuje opšti rad aplikacije i rezimirati prednosti i
mane korišćenja Python jezika, PyQt5 okvira i paralelizacije rada.<br /> <br />
Demo originalne igrice: https://www.youtube.com/watch?v=HQv0zAXDCo8
