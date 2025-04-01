## Tehtävä 2

```mermaid
 sequenceDiagram
    Main->>laitehallinto: lisaa_lataaja(rautatientori)
    Main->>laitehallinto: lisaa_lukija(ratikka6)
    Main->>laitehallinto: lisaa_lukija(bussi244)
    Main->>lippu_luukku: osta_matkakortti("Kalle")
    lippu_luukku-->>Main: kallen_kortti   
```

