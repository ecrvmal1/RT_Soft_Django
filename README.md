# RTSoft
## Technical task
Pls check file request.txt 

## Project stack:
Python 3.10  
Django==3.2.23  
Pillow==10.1.0  

## To Run Project 

### Import Categories from file
```bash
python manage.py import_categs <filename.csv>
example:
python manage.py import_categs D:\GB\pythonProject\RTSoft\gen_csv\input_data.csv
```
### Import Records data from file
```bash
python manage.py import_data <filename.csv>
example:
python manage.py import_data D:\GB\pythonProject\RTSoft\gen_csv\input_data.csv
```

### Run native project
```bash
python manage.py runserver
```
  
### Run project in Docker
```bash
docker-compose up --build
```

## Dumpdata:
To Make Dumpdata:
```bash
python manage.py dumpdata mainapp --indent 2 -o mainapp/fixtures/001_dumpdata.json  

```

To load Dumpdata:
```bash
python manage.py loaddata mainapp/fixtures/001_dumpdata.json  
```
