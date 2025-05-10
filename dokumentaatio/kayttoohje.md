# Käyttöohje

Lataa ensin projektin uusin release.

## Ohjelman käynnistäminen

```bash
poetry install
```

```bash
poetry shell
```
```bash
poetry run invoke start
```


## Käyttäminen

Ohjelma käynnistyessä avaa käyttöliittymän mistä valitaan taso. Valitse taso klikkaamalla jotakin nappia.
Sen jälkeen peli alkaa ja sen voi sulkea sulkemalla ikkunan. Säännöt ovat samat kuin tavallisessa Minesweeperissä.


## Testaus
```bash
poetry run invoke test
```

tarkemmat tiedot:

```bash
poetry run invoke coverage-report
```
