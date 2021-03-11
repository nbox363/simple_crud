# Animal crud

# Product service

It's an app that has been created as a test-task for "Виста" company


# Install

```bash
$ git clone https://github.com/nbox363/animal_crud
$ cd animal_crud
```

Create a virtualenv and activate it:
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Install pip packages:
```bash
$ pip install -r requirements.txt
```

# Run
you may need to stop local postgres before starting docker 
```
sudo service postgresql stop
```
to run postgres database
```bash
docker-compose up
```



to run server
```bash
python manahe.py runserver
```
