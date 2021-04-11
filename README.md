# Face Recognition 

Pentru a rula aplicația este nevoie de urmat următori pași:

1 Fă `git clone git@github.com:boriscazacu/faceRecog.git` sau descarcă arhiva.

2 Du-te în folderul faceRecog și deschide terminalul/consola.

3 Instalează librariile necesare `pip install cmake face_recognition numpy opencv-python`

4 Rulează aplicația pentru windows `python main.py` sau pentru linux `python3 main.py`


# Setări suplimentarea

În folderul `images` sunt niște exemple de imagini în formatul `.jpeg` dacă vrei să adaugi imagini de un alt format
deschie `main.py` într-un editor de cod și în linia `94    train = Train('jpeg')` adaugi formatul dorit.

> Aplicația rulează doar cu formatul indicat în această linie, dacă adugi imagini de un alt format ia le va ignora !!