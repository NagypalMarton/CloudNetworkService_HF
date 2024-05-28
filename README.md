# CloudNetworkService_HF
Felhők hálózati szolgáltatások Házi Feladat repoja

[![Actions Status](https://github.com/NagypalMarton/CloudNetworkService_HF/workflows/Python%20CI-CD.yml/badge.svg)](https://github.com/NagypalMarton/CloudNetworkService_HF/actions)

Futtatható webalkalmazás [ITT](https://github.com/NagypalMarton/CloudNetworkService_HF/releases/tag/latest) érhető el!

## Webalkalmazásról

A tárgy keretén belül a feladat leírásban foglalt járműfelismerő és értesítő webalkalmazás készítése. Ezt egy Python nyelvben mgírt frameworkben, a Flaskban készül el Ubuntu alapú környezetben. Az alkalmazásban lehet képet és hozzá tartozó leírás feltöltését 
- CI/CD környezet: GitHub Actions + DockerHUB
- Autodetektáló modell: YOLO

## Feladat kiírás
A félév során mindenkinek létre kell hoznia egy fejlesztői CI/CD környezetet a saját gépén és ennek használatával egy olyan web szolgáltatást kell létrehozni ami az alábbi funkciókat látja el:
- Kép és hozzá tartozó leírás feltöltése (kép és leírás páros tárolás)
- A feltöltött képen automatikus autó detektálás és a megtalált autók bekeretezésével a kép megjelenítése a weboldalon
- A weboldal “üzemeltetői” képesek legyenek feliratkozni az oldalra, azaz kapjanak értesítést az összes eddigi és az új feltöltött képekről úgy, hogy kiküldésre kerül számukra a képhez tartozó leírás és a rendszer által detektált autók száma a feltöltött képen

**FONTOS!** A fejlesztésről készítsetek **fejlesztői dokumentációt**, melyben szerepeljen a futási környezet leírása, a CI/CD környezet leírása, a fejlesztett kód vázlatos leírása, a használt adatszerkezetek és a webszolgáltatás architektúrája.

### Egyéb tudnivalók
- A weboldal létrehozásánál nem a dizájn a lényeg (akár sima HTML is lehet), hanem az általatok összerakott és használt CI/CD illetve a webszolgáltatáshoz tartozó “felhős ökoszisztéma”, azaz a félév során bemutatott backend technológiák használata
- A fejlesztéshez nincsen technológiai megkötés, viszont a HF bemutatásakor legyenek érveitek, hogy miért a használt backend megoldást választottátok (pl. Funkció 1-et konténerben valósítottam meg a jól ledobozálhatóság miatt, míg a Funkció 2-re FaaS-t gondoltam alkalmasnak a gyors skálázódás és párhuzamos végrehajtás miatt). Kiváncsian várjuk, hogy ki milyen architektúrát tartott megfelelőnek a kiírt feladat megoldására.
- Természetesen az autó detektáló modellt nem a hallgatóknak kell lefejleszteniük. Bármilyen online elérhető ingyenes detektáló modellt szabad használni.
- Az üzemeltetői feliratkozásra érdemes lehet valamilyen message queue-t használni

### Osztályzás
A házi feladat három részből áll:
1. CI/CD környezet telepítése
2. weboldal + autó detektálás funkció imeplementálása
3. üzemeltetők feliratkozási funkciója
