import random
from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import Schoolkid, Subject, Lesson, Commendation


def create_commendations(schoolkid_full_name, subject_title):
    commendations = ['Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    ]
    try:
        schoolkid = Schoolkid.objects.get(full_name=schoolkid_full_name)
    except ObjectDoesNotExist:
        print(f'Имя "{schoolkid_full_name}" - не найдено. Введите полное имя. Например: Иванов Иван Иванович')
        return

    subject = Subject.objects.get(
        title=subject_title,
        year_of_study=schoolkid.year_of_study,
        )
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
	create_commendations('Schoolkid', 'Subject')


if __name__ == '__main__':
	main()


