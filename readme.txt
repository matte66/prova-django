per creare l'ambiente virtuale-> python -m venv "nomeAmbiente"
aggiorniamo pip (devi essere dentro l'ambiente virtuale)-> python -m pip install --upgrade pip
per intallare Django nell'ambiente virualte fare-> pip install Django=="versione di Django"
per creare il progetto fare-> django-admin.exe startproject mysite . il punto compreso per indicare di crearlo nella directory corrente
per avviare l'ambiente virtuale-> myvenv\Scripts\activate
per creare un applicazzione-> python manage.py startapp "nomeApplicazione" successivamente nel file setting dobbiamo dire a Django che c'è una nuova applicazione
per creare un super utente-> python manage.py crearesuperutente