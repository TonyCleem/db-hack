import random
from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import Schoolkid, Subject, Lesson, Commendation, Chastisement, Mark


def fix_marks(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)[0]
    child = schoolkid.full_name
    fixed_marks = Mark.objects.filter(
        points__lte=3,
        schoolkid__full_name__contains=child,
    ).update(points=5)


def remove_chastisements(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)[0]
    child = schoolkid.full_name
    chastisements_schoolkid = Chastisement.objects.filter(schoolkid__full_name__contains=child).delete()


def create_commendations(schoolkid, subject_title):
    commendations = ['Молодец!',
                     'Отлично!',
                     'Хорошо!',
                     'Гораздо лучше, чем я ожидал!',
                     ]
    try:
        schoolkid = Schoolkid.objects.get(full_name=schoolkid_full_name)
    except ObjectDoesNotExist:
        print(f'Имя "{schoolkid_full_name}" - не найдено. Введите полное имя. Например: "Иванов Иван Иванович"')
        return

    try:
        subject = Subject.objects.get(
            title=subject_title,
            year_of_study=schoolkid.year_of_study,
        )
    except ObjectDoesNotExist:
        print(f'Предмет "{subject_title}" - не найден. Укажите верное название предмета без ошибок. Например: "Физика"')
        return

    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject,
    ).order_by('date').first()
    commendations = Commendation.objects.create(
        created=lesson.date,
        teacher=lesson.teacher,
        schoolkid=schoolkid,
        subject=subject,
        text=random.choice(commendations),
    )


def main():
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendations('Фролов Иван', 'Музыка')


if __name__ == '__main__':
    main()


