## Monopoli, muokattu luokkakaavio

```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Aloitusruutu "1" -- Ruutu
    Vankila "10+30" -- Ruutu
    Sattuma -- Ruutu
    Yhteismaa -- Ruutu
    laitokset -- Ruutu
    Asemat -- Ruutu
    kadut -- Ruutu
    Omistukset -- Pelaaja
    laitokset -- Omistukset
    Asemat -- Omistukset
    kadut -- Omistukset
    Rahat -- Pelaaja
    Kortit -- Yhteismaa
    Kortit -- Sattuma   
```
