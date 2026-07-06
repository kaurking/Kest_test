# Kest_test

Mini veebirakendus liikluskindlustuse (MTPL) pakkumiste leidmiseks numbrimärgi järgi.

## Käivitamine

```bash
scripts/server install
scripts/server db-import
scripts/server dev
```

`dev` käivitab serveri esiplaanil. Sulgemiseks vajuta terminalis `Ctrl+C`.
`db-import` loob SQLite database'i faili `data/app.db` ja impordib sinna
praeguse `offers.json` sisu.

SQLite'i ei pea eraldi alla laadima: Python kasutab sisseehitatud `sqlite3`
moodulit. VS Code'is näed database'i failina `data/app.db`; selle sisu
vaatamiseks võib hiljem lisada SQLite viewer extensioni, aga rakenduse
käivitamiseks pole seda vaja.

Kui tahad serveri taustal käima panna:

```bash
scripts/server start
```

Taustaserveri staatus, logid ja sulgemine:

```bash
scripts/server status
scripts/server logs
scripts/server stop
```

Rakenduse logid näitavad näiteks, millal MTPL pakkumisi küsiti, mitu rida
database'ist leiti, mitu pakkumist võrdlusesse jäi ja milline oli odavaim.
`dev` režiimis näed neid terminalis; taustaserveri puhul käsuga
`scripts/server logs`.

Kui muudad `offers.json` faili ja tahad andmed uuesti database'i panna:

```bash
scripts/server db-import
```

Kui port `8000` on kinni, saab käivitada teisel pordil:

```bash
PORT=8001 scripts/server dev
```

API:

```http
GET /api/mtpl/offers?registration_number=123ABC
```

Veebileht:

```text
http://127.0.0.1:8000/
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Testid

```bash
.venv/bin/python -m unittest
```

## Loogika

Backend loeb hetkel pakkumised SQLite database'ist `data/app.db`. Algandmed saab
sinna importida `offers.json` failist käsuga `scripts/server db-import`.
Veebilehel saab valida MTPL kindlustuse, sisestada numbrimärgi ja näha kõiki
sobivaid pakkumisi odavaimast kallimani.

Database'i lugemine käib `DatabaseOfferProvider` kaudu. See teeb SQL päringu,
tagastab sama kujuga pakkumised nagu vana JSON-provider ja edasi kasutab süsteem
sama MTPL filtreerimise ning hinnavõrdluse loogikat.

Hiljem saab `MockOfferProvider` asemel lisada päris kindlustuspakkujate
provider'id, ilma et UI või pakkumiste võrdlemise äriloogika peaks muutuma.


1. Client api (fastAPI)
GET /api/mtpl/offers?registration_number=123ABC

2. endpoint calls get_mtpl_offers()
registration_number is required and must be at least 1 character
If validation fails, FastAPI returns 400


3. QuoteService.get_cheapest_mtpl_offer()
Normalizes the registration number via normalize_registration_number()
removes spaces and dashes
converts to uppercase
Logs the request
Asks the configured provider for offers for that registration

4. Offer lookup
In the current app setup, DatabaseOfferProvider is used
It opens SQLite via database.py
It ensures schema exists with create_schema(connection)
Runs a SQL query:
select offers where upper(reg) = upper(?)
orders by id
Returns matching rows as dictionaries

5. No offers found
If the provider returns an empty list:
QuoteService raises NoOffersFound
main.py converts that to HTTP 404

6. Offer comparison
compare_mtpl_offers(raw_offers) in offer_comparison.py
For each raw offer:
rejects if product != "mtpl"
rejects if status != "ok"
rejects if premium is missing or not numeric
rejects unsupported period or non-EUR currency
Converts valid offers into comparable form:
computes annual premium
formats values
Sorts valid offers by (annualPremium, insurer)
Builds response sections:
cheapestOffer
cheapestOffers (all tied for lowest premium)
topOffers (top 3)
offers (all valid offers)
comparedOffers count
ignoredOffers with reasons

7. Final result
If no valid MTPL offers remain after filtering:
NoValidMtplOffersFound is raised and turned into HTTP 404
Otherwise the service returns:
"registrationNumber": normalized value
the comparison payload
That JSON is returned to the client
