# User Promptide Kokkuvote

See fail koondab senised kasutaja kysimused ja soovid kronoloogilises jarjekorras.

## 1. Algne backend'i idee

Kasutaja soovis ehitada kindlustussusteemi, kus kasutaja sisestab soiduki
registrinumbri ja naeb mock-pakkumiste seast odavaimat liikluskindlustuse
(MTPL) pakkumist. Andmed pidid tulema kaasasolevast `offers.json` failist.

Kusimus: milline oleks padev backend sellisele ulesandele?

## 2. Uldise plaani soov

Kasutaja palus kirjeldada praegu uldist plaani.

## 3. Pariselt edasiarendatav loogika

Kasutaja kysisi, milline oleks paris loogika, mida saaks hiljem lihtsalt edasi
arendada paris susteemiks.

## 4. Python sobivus

Kasutaja kysisi, kui viable oleks sama asja Pythonis teha.

## 5. Susteemi alustamine Pythonis

Kasutaja lubas alustada susteemi ehitamist Python/FastAPI kujul ning palus
arvestada, et hiljem lisandub testimise jaoks UI.

## 6. Numbrimargi testimine

Kasutaja kysisi, kuidas praegu kontroll kaib ja kuidas saab numbrimarki testida.

## 7. Auto nime pohine otsing

Kasutaja pakkus vahepeal, et numbrimargi asemel voiks otsida auto nime järgi
ning kliendile tuleks anda alati vahemalt 3 odavaimat pakkujat, kuid kuvada
koik pakkumised odavaimast kallimani.

Hiljem kasutaja tapsustas, et see oli eksitus ja auto nime pohist otsingut ei
ole vaja.

## 8. Testandmete plokid testides

Kasutaja kysisi, mis on `test_quote_service.py` failis `service` muutujasse
salvestatud pakkumiste plokid, kas need on vajalikud ja kas 10 000 realine JSON
tekitaks probleemi.

## 9. API too selgitus

Kasutaja palus tapselt selgitada, kuidas API praegu tootab.

## 10. Veebilehe lisamine

Kasutaja tapsustas, et auto nime pohist otsingut ei ole vaja. Ta kysisi, kas
Swagger UI on midagi, mida kasutatakse, ja soovis tavalist lihtsat veebilehte:

- uleval MTPL kindlustuse dropdown
- numbrimargi otsing
- pakkumised odavaimast kallimani
- kui numbrit ei leita, kuvada otsingukoha juures tekst, et sellist autot ei
  leitud
- neutraalne hele basic template
- ilma logode ja piltideta
- all kontaktiosa

## 11. JSON database flow

Kasutaja kysisi, kas kui service jookseb arvutis ja veebileht on uleval, siis
susteem votab info `offers.json` "JSON database'ist" ja valjastab selle
kasutajale ning kas see flow on praegu tootav.

## 12. Korralikum kaivitamine ja sulgemine

Kasutaja soovis muuta susteemi kaivitamise korralikumaks, sest backendi
sulgemine oli segane.

## 13. Taustal kaivitamise mote

Kasutaja kysisi, mis on serveri taustal kaivitamise mote ehk miks kasutada
`start` kasu `dev` asemel.

## 14. Susteemi hostimine, database ja turvalisus

Kasutaja kysisi taustakysimusi:

- kuidas selline susteem uldiselt jooksma peaks ja mis masina peal
- kuidas lisada database
- kas praegune susteem on kübertuvalisuse ja andmekaitse poolelt aarimselt
  ebaturvaline

## 15. Database lisamise detailid ja skaleerimine

Kasutaja kysisi, kas praegune logging on piisav, kas database lisamisel tuleks
seda uuendada, kuidas database lisamine tootaks praeguse setupiga ja kuidas
seda hiljem skaleerida. Samuti huvitas, kus tulevikus suurem database jookseks.

## 16. SQLite database integreerimine

Kasutaja palus integreerida SQLite database'i.

Tapsustused:

- uued autod lahevad uldiselt otse database'i
- lisada voib ka JSON import skripti
- kasutaja kysisi, kas `DatabaseOfferProvider` on see kiht, mis saadab tagasi
  kasutajale naidatavad andmed
- kasutaja mainis, et ta pole varem VS Code'is database'i lisanud
- kasutaja pole SQLite'i alla laadinud
- loggingut ei ole vaja kohe teha, aga sellega voib jargmise sammuna arvestada

## 17. Portide probleem

Kasutaja margas, et port `8000` on kasutusel, aga serverit ei saa sulgeda.
`scripts/server status` ytles, et server ei jookse, kuid URL avanes ja
`123ABC` otsing tootis tulemust.

Kasutaja kysisi, mis toimub.

## 18. Loggingu sisu

Kasutaja kysisi, mida oleks selles susteemis vaja logida ning kas logida lihtsalt
SQL `SELECT` kaske.

## 19. Loggingu lisamine

Kasutaja kinnitas, et ta motleski sellist loggingut, ja palus selle ara teha.

## 20. API endpointide lihtsustamine

Kasutaja margas, et API endpoint'e on kaks, ja palus jatta alles ainult
`/api/mtpl/offers`.

## 21. Provider'i funktsiooni tapsustus

Kasutaja kysisi `quote_service.py` rea kohta:

```python
raw_offers = self.offer_provider.get_offers_for_registration(normalized_registration)
```

Kasutaja ei nainud, kus funktsioon on defineeritud, ja kysisi, kas database
overwrite'is selle sisuliselt ara.

## 22. Promptide kokkuvote faili

Kasutaja palus kokku votta koik senised promptid ja lisada need Markdown failina
kausta.
