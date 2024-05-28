# CloudNetworkService_HF
Felhők hálózati szolgáltatások Házi Feladat repoja

[![Actions Status](https://github.com/NagypalMarton/CloudNetworkService_HF/workflows/Python%20CI-CD.yml/badge.svg)](https://github.com/NagypalMarton/CloudNetworkService_HF/actions)

Futtatható webalkalmazás [ITT](https://github.com/NagypalMarton/CloudNetworkService_HF/releases/tag/latest) érhető el!

## Webalkalmazásról

A tárgy keretén belül a feladat leírásban foglalt járműfelismerő és értesítő webalkalmazás készítése. Ezt egy Python nyelvben mgírt frameworkben, a Flaskban készül el Ubuntu alapú környezetben. Az alkalmazásban lehet képet és hozzá tartozó leírás feltöltését 
- CI/CD környezet: GitHub Actions + DockerHUB
- Autodetektáló modell: YOLO

## Futtatási környezet
- Legújabb Ubuntu
- Flask (Python alapú webframework)
- Docker && Kubernetes

### Hiányzó funkciók
- A weboldal “üzemeltetői” képesek legyenek feliratkozni az oldalra, azaz kapjanak értesítést az összes eddigi és az új feltöltött képekről úgy, hogy kiküldésre kerül számukra a képhez tartozó leírás és a rendszer által detektált autók száma a feltöltött képen * (Az üzemeltetői feliratkozásra érdemes lehet valamilyen message queue-t használni) *
- Autó Detektálása és ennek kiírása képernyőre