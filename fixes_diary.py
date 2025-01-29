import random
from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import Schoolkid, Subject, Lesson, Commendation, Chastisement, Mark


COMMENDATION = ['Молодец!',
                 'Отлично!',
                 'Хорошо!',
                 'Гораздо лучше, чем я ожидал!',
                 ]


def get_schoolkid():
    schoolkid_full_name = input('Введите ФИО ученика: ')
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_full_name)
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_full_name}'. Введите полное ФИО")
        return
    except Schoolkid.DoesNotExist:
        print(f"Ученик в базе не найден. Убедитесь, что имя '{schoolkid_full_name}' - введно верно")
        return


def get_subject(schoolkid):
    subject_title = input('Введите название предмета: ')
    try:
        subject = Subject.objects.get(
            title=subject_title,
            year_of_study=schoolkid.year_of_study,
        )
        return subject
    except Subject.MultipleObjectsReturned:
        print(f"Найдено несколько предметов с названием '{subject_title}'. Введите полное ФИО")
        return
    except Subject.DoesNotExist:
        print(f"Прдмет в базе не найден. Убедитесь, что название '{subject_title}' - введно верно")
        return


def fix_marks(schoolkid):
    fixed_marks = Mark.objects.filter(
        points__lte=3,
        schoolkid__full_name__contains=schoolkid.full_name,
    )
    if not fixed_marks:
        print(f"У ученика {schoolkid.full_name} нет плохих отметок")
        return
    fixed_marks.update(points=5)
    print('Плохие отметки исправлены на пятерки')
    return


def remove_chastisements(schoolkid):
    chastisements_schoolkid = Chastisement.objects.filter(schoolkid=schoolkid)
    if not chastisements_schoolkid.count():
        print(f"У ученика {schoolkid.full_name} нет замечаний")
        return
    chastisements_schoolkid.delete()
    print('Все замечания удалены')
    return


def create_commendations(schoolkid, subject):
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject,
    ).order_by('date').first()
    if not lesson:
        print('Уроки не найдены. Проверьте вводимые данные')
        return
    commendations = Commendation.objects.create(
        created=lesson.date,
        teacher=lesson.teacher,
        schoolkid=schoolkid,
        subject=subject,
        text=random.choice(COMMENDATION),
    )
    print(f'Ученику {schoolkid.full_name}, добавлен комплимент "{commendations.text}"')
    return lesson, commendations


def main():
    get_schoolkid()
    get_subject(schoolkid)
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendations(schoolkid, subject)


if __name__ == '__main__':
    main()