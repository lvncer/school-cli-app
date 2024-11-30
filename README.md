# School CUI CRUD App

## Dumping Database

### Loginning MySQL terminal

```cmd
mysql -u root -p
```

### Dumping DB file

```sql
DROP DATABASE IF EXISTS school;
CREATE DATABASE school;
USE school;
SOURCE /path/to/your/project/db/school.dmp
```

## Installing Python Modules

```bash
pip install -r requirements.txt
```

## Starting API Server

```bash
uvicorn dbaccess:app --reload
```

## Showing Docs

[localhost:8000/docs](localhost:8000/docs)

## Execute CRUDs

```bash
python.exe /path/to/your/project/crud/selectall.py
```
