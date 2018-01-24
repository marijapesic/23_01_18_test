Teorijski deo
---

Dati sto konciznije odgvore u formi prosto prosirenih recenica na svako od sledecih pitanja.

01. Sta je to JSON?
JSON (JavaScript Object Notation) je jedan od lakših tekstualnih otvorenih standarda dizajniran za citljivu razmenu podataka. Ekstenzija datoteke s podacima u JSON-ovom formatu je .json, dok je meta oznaka (MIME format) application/json.

02. Sta je to XML?
XML (Extensible Markup Language)predstavlja tekst (podaci) koji je formatiran u skladu sa
pravilima.standard za opis sadrzaja i strukture (tekstualnih i
multimedijalnih) dokumenata i razmenu
dokumenatta na Web-u

03. Sta je to URL?
URL (Uniform Resource Locator) je ujednačeni ili uskladjeni lokator sadrzaja (resursa), globalni adresar koji se koristi za lokalizaciju trazenih sadrzaja na webu, ukljucujuci protokol identifikatora i IP adresu. 

04. Sta je to HTTP?
HTTP (HyperText Transfer Protocol) je glavni i najcesci protokol za prenos informacija na webu. Osnovna namena ovog protokola je da omoguci objavljivanje i prezentaciju HTML dokumanata, tj web stranica.

05. Sta je to RESTful API?

06. Koje HTTP metode imamo?
HTTP metode definisu set naredbi(metoda) kako bi se zeljena akcija izvrsila za dati resurs: get, head, post, put, delete, connect, options, trace, path

07. Sta je to DNS?
DNS ( Domain name system) je u stvari jedna baza podataka u kojoj su upisana sva imena i odgovarajuće IP adrese pojedinih računara, kao i grupe funkcija koje omogućavaju prevođenje istih. Pretvara simbolična imena i adrese sa Interneta (npr. alfa.auxx.com) u odgovarajuće brojeve, nerazumljive korisniku (npr. 132.196.55.i obratno. 

08. Sta je to private IP?
IP je jedinstveni broj (adresa) koju koriste masine (racunari) u medjusobnom saobracaju putem interneta uz koriscenje internet protokola.
 
09. Sta je to AJAX?
AJAX (Asinhroni JavaScript + XML) je novija tehnika za kreiranje bolje, brze i interaktivnije web aplikacija uz pomoc XML, HTML, CSS i Java Scripta.

10. Sta je to TCP/IP?
TCP/IP (Transmission Control Protocol/Internet Protocol) je vodic (set pravila i procedura) komunikacionih protokola koji se koriste za konekciju uredjaja na internetu, ili na privatnoj mrezi.

11. Sta je to kes memorija?
Kes memeorija je memorija malog kapaciteta koja sluzi za zapis podataka koji se cesto koriste. T je mesto gde programeri skladiste podatke sa internet stranica i programa, da kada bi ponovo prisutpili odredjenoj stranici ili programu one i njihovi sadrzaji bi se brze ucitavale. Glavna karakteristika kesa je smanjenje brzine ucitavanja sadrzaja koristeci vec skinute podatke.

12. Koja je razlika izmedju klase i objekta?
klase i objekti su dva najvaznija kocepta Objekto orijentisanog programiranja. 
Objekat  je definisan kao entitet koji moze biti koriscen upotrebom komanda Objektivno-orijentisanog programiranja (Objekat - varijabla).
Klasa se koristi u Objektivno-orijentisanom programiranju za opisivanje jednog ili vise objekata (klasa - tip)


Backend
---

1. U `models.py` fajlu implementirati `Comment` model (klasu) u Python-u koja sadrzi atribute:
- `text`: sam komentar, i
- `date`: datum komentara u formatu `YYYY-MM-DD`
"Override"-ovati `__repr__` metod.

2. U `models.py` fajlu definisati `COMMENTS` varijablu koja sadrzi niz od 3 elementa koji su tipa `Comment`. 

3. U `app.py` fajlu napraviti Flask applikaciju koja ima `index` "view" funkciju koja handle-uje `/` route. Funkcija bi trebalo da vraca HTML string koji u `body`-ju sadrzi heading "Welcome!".

4. U `app.py` dodati `comments` "view" funkciju koja handle-uje `/comments` route. Funkcija bi trebalo da vraca HTML koji u `body`-ju sadrzi tabelu komentara. Koristiti Flask template.

5.  U `app.py` dodati `api_comments` "view" funkciju koja handle-uje `/api/v1.0/comments` route. Funkcija bi trebalo da vraca JSON reprezentaciju `COMMENTS` niza.

Frontend
---

U `home.html` fajlu imlementirati jednostavnu klijent aplikaciju kojom moze da testira prethodno implementirani API end point. Koristiti `form` i `iframe`.

Algoritmi
---

Napisati i JavaScript i Python funkciju koja predstavlja resenje sledeceg zadataka:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Fizz` instead of the number and for the multiples of five print `Buzz`. For numbers which are multiples of both three and five print `FizzBuzz`.

Uputstvo
---

Resenja i odgovore predati u okviru GitHub repozitorijuma.
