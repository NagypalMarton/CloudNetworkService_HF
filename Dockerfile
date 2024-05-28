# Használjuk a Python 3.8-as alap képet
FROM python:3.8-slim-buster

# Munkakönyvtár beállítása
WORKDIR /app

# Függőségek másolása
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libgl1-mesa-dev libglib2.0-0

# Függőségek telepítése
RUN pip3 install -r requirements.txt

# YOLO fájlok másolása
COPY darknet/yolov3.weights yolov3.weights
COPY darknet/yolov3.cfg yolov3.cfg

# Alkalmazás másolása
COPY . .

# Alkalmazás futtatása
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]