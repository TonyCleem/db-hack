# db-hack #

db-hack - скрипт разработанный в рамках учебного проекта Devman. Позволяет редактировать дневник ученика используя фреймворк Django.

---

## Функционал
Скрипт хранит в себе несколько функций для редактирования:

`fix_marks(schoolkid)` - исправляет все плохие оценки на пятерки

`remove_chastisements(schoolkid)` - удаляет все замечания ученика

`create_commendations(schoolkid, subject_title)` - добавляет одобрение ученику по указанному предмету

## Минимальные требования
* Python 3.7+
* Репозиторий с [электронным дневником](https://github.com/devmanorg/e-diary/tree/master)
* Зависимости с `requirements.txt`
---
## Установка и запуск

### Установка

- Скопировать репозиторий
```
git clone https://github.com/devmanorg/e-diary/
```
- Создать виртуальное окружение:
```
python -m venv  <имя env>
```
- Установить все зависимости из `requirements.txt`
```
pip install -r requirements.txt
```

- Импортировать скрипт в приложение `datacenter` (можно просто переместить мышью в папку)
- Импортировать необходимую базу данных, которая будет "взламываться". Используйте только в ознакомительных целях. Чтобы правильно импортировать базу данных читайте [документацию](https://docs.djangoproject.com). Можно воспользоваться примером из [урока](https://docs.djangoproject.com/en/5.1/intro/tutorial02/) Django.
- Запустить оболочку командой
```
pyhton3 manage.py shell
```

### Запуск
1. Импортировать скрипт в оболочке со всеми функциями
```
>>> from datacenter.fixes_diary import fix_marks, remove_chastisements, create_commendations

```
2. Выбрать необходимую функцию:

`fix_marks(schoolkid)` - запустить с указанием имени ученика:
```
>>> fix_marks('<указать полное имя>')
```

`remove_chastisements(schoolkid)` - запустить с указанием имени ученика:
```
>>> remove_chastisements('<указать полное имя>')
```

`create_commendations(schoolkid, subject_title)` - запустиь и в скобках указать полное имя ученика и название предмета.
```
>>> create_commendations(<Полное Имя Ученика>, <Название предмета>)
```

---
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).