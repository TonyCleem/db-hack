# db-hack #

db-hack - скрипт разработанный в рамках учебного проекта Devman. Позволяет редактировать дневник ученика используя фреймворк Django.

---

## Функционал
Скрипт хранит в себе несколько функций для редактирования:

`get_schoolkid()` - задает ученика

`get_subject(schoolkid)` - задает предмет

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
from datacenter.fixes_diary import *

```
2. Выбрать необходимую функцию:

`get_schoolkid()` - Обозначаем ученика:
```
schoolkid = get_schoolkid()
```
Вводим ФИО:
```
Введите ФИО ученика: 
```
`get_subject(schoolkid)` - Обозначаем предмет:

```
schoolkid = get_schoolkid()
```
Вводим название предмета:
```
Введите название предмета:
```
> **_NOTE:_** Следующие функции рабтают только если ранее обозначены schoolkid и subject


`fix_marks(schoolkid)` - Запустить указав schoolkid по-умолчанию:
```
fix_marks(schoolkid)
```
Пример вывода:
```
У ученика Кошелева Эмилия Михайловна нет плохих отметок

```

`remove_chastisements(schoolkid)` - Запустить указав schoolkid по-умолчанию:
```
remove_chastisements(schoolkid)
```
Пример вывода:
```
У ученика Кошелева Эмилия Михайловна нет замечаний
```


`create_commendations(schoolkid, subject)` - Запустить указав schoolkid и subject по-умолчанию:
```
create_commendations(schoolkid, subject)
```
Пример вывода:
```
Ученику Кошелева Эмилия Михайловна, добавлен комплимент "Гораздо лучше, чем я ожидал!"

```

---
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).