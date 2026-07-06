# User Promptid Sona-Sonalt

## 1

```text
Mul vaja ehitada kindlustussüsteem, mis annab kasutajle numbrimärgi põhjal autole kindlustuspakkumise. Tegemist on lihtsa praegu lihtsa süsteemiga. Praegu oleks vaja süsteemi, mis vastab sellele kirjeldusele:
> "*Kasutajana tahan sisestada oma sõiduki registrinumbri ja näha liikluskindlustuse pakkumistest (vähemalt 3tk) kõige odavamat, et saaksin kiiresti teada, milline kindlustus mulle kõige vähem maksab.*"

**Ülesanne.** Ehita lihtne mini-funktsionaalsus: kasutaja sisestab registrinumbri ja näeb mock-pakkumiste seast kõige odavamat liikluskindlustuse (MTPL) pakkumist.

**Andmed.** Pakkumised tulevad kaasasolevast `offers.json` failist.

algne süsteem preagu võiks olla selline, et kasutab seda algset andmefaili. Milline oleks pädev backend sellisele ülesandele?
```

## 2

```text
kirjelda praegu üldist plaani palun
```

## 3

```text
Milline oleks päris loogika, mida saaks hiljem lihtsalt edasi arendada päris süsteemiks
```

## 4

```text
kui viable on sama asja pythonis teha?
```

## 5

```text
Võib selliselt alustada süsteemi ehitamist, aga arvesta, et hiljem lisan ka Testimise mõttes UI süsteemile.
```

## 6

```text
kuidas preagu kontroll käib, kuidas saan testida numbrimärk?
```

## 7

```text
Preagu on hard-coded sisse need autoinfod koos kindlustusega. Teeme hetkel nii, et saab auto nime järgi leida ja siis ta otsib JSON failist seda pakkumist. Ja lisaks tuleb kliendile anda alati vähemalt 3 odavaimat pakkujat, võiks teha nii, et saab järjestada lihtsalt nii, et odavaimad on eespool, aga näidatakse kõiki.
```

## 8

```text
mis on failis test_quote_service.py service muutujasse saalvestatud plokid, kas need on seal vajalikud? Kui meie JSON fail oleks 10 000 rida, siis see tekitaks probleemi?
```

## 9

```text
Selgita täpsemalt, kuidas see APi praegu töötab
```

## 10

```text
Ärme tee auto nime põhiselt, kirjutasin valesti enne. Kas Swagger UI on midagi ,mida kasutatakse? Tegelikult Võiks veebilehe normaalsele kujule teha. Teeks lihtsa dropdowni, kus on MTPL kindlustus ja seellel on funktsioon kus saab otsida numbrimärki ja siis näha pakkumisi alustades odavaimast. Kui numbrit ei oel siis pane otsingukoha juurde tekst, et sellist autot ei leitud. Veebileht võib olla preagu ilma igasuguste logode ja piltidetta, lihtsalt color code neutraalne, hele. Lihtslat basic template, kus üleval dropdown ja all kontakt jne. Võid võtta inspiratsiooni mõne eesti kindlustusfirma lehest, nt kindlustusest. 
```

## 11

```text
Huvi pärast küsin, kui mul praegu service jookseb arvutis ja ma paneb veebilehe ülesse, kas siis teoorias ta võtab mu "JSON datbasist" kogu info ja siis väljastab selle kasutajale? Kas see flow on praegu töötav?
```

## 12

```text
Teeks süsteemi käivitmise korralikumaks. Hetkel on backendi sulgemine ka segane, kuidas saaks paremaks seda teha?
```

## 13

```text
Küsin veidi tasutaküsimusi, kuna olen võhik süsteemi algstaadiumi osadega. 
Kuidas üldiselt selline süsteem jooksma peaks, mis masina peal?
Kuidas saaks eelneva küsimuse põhjal lisada database'i süsteemile?
Kas süsteem on preagu äärmiselt ebaturvaline küberturvalisuse ja andmekaitse poolte pealt?
```

## 14

```text
kui preagune logging on piisav, siis databse lisamisel tuleb ka seda uuendada? Selgita kuidas töötaks database lisamine hetkel minu setupiga ja kuidas saaks seda hiljem skaleerida, kus jookseb tulevikus suurem database?
```

## 15

```text
Jah integreeri sql lite database. Üldiselt uued autod lähevad otse database'i, aga võid teha ka json import skripti. DatabaseOfferProvider on see, mis saadetekase tagasi, mida näidatakse kasutajale eks? Ma pole Visual studi COde'i lisanud databse'i varem. Samuti pole ma laadinud alla sql lite'i. Ära loggingut kohe tee, aga võid arvetada, et see on järgmine samm.
```

## 16

```text
There seems to be a problem with the ports. 8000 in in use but i cant close it, im assuming its my server but status says server is not open. But when i open the url and search for 123abc then it works, whats up with that?
```

## 17

```text
mis on serveri taustal käivitamse mõte, ehk teha dev asemel start?
```

## 18

```text
okei saan aru. Teeme logid ka paremaks, mis oleksid vajalikud selles süsteemis logidesse? lihtsalt read (select) käsud?
```

## 19

```text
ma tegelt midagi sellest mõtlesingi, tee see ka ära
```

## 20

```text
right now there are 2 API endpoints. I dont think we need both, lets keep the offers one?
```

## 21

```text
in quote_service raw_offers = self.offer_provider.get_offers_for_registration(normalized_registration):
the function there is not defined. did the database overwrite this basically?
```

## 22

```text
Palun võta kokku kõik minu promptid, mis ma küsisin ja pane .md faili ja lisa siia kausta.
```

## 23

```text
Tee seda nüüd uuesti ja pane sõna sõnalt täpselt samamoodi kirja kuidas ma kirjutasin
```
