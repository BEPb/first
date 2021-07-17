# python 3.9 (name dev: 3BEPb)
# models.py - файл в котором храняться наши модели приложения
from django.db import models

# Create your models here.
class Phonenumber(models.Model):
    # id - создается по умолчанию

    subdivision = models.CharField(max_length=150, verbose_name='подотдел', blank=True)  # поле "подотдел", максимальная длинна 150 символов
    position = models.CharField(max_length=150, verbose_name='должность')  # поле "должность", максимальная длинна 150 символов
    surname = models.CharField(max_length=50, verbose_name="фамилия")  # поле "фамилия", максимальная длинна 50 символов
    name = models.CharField(max_length=20, verbose_name="имя")  # поле "имя", максимальная длинна 20 символов
    second_name = models.CharField(max_length=20, verbose_name="отчество")  # поле "отчество", максимальная длинна 20 символов
    oficial_telephone = models.CharField(max_length=20, verbose_name="служебный телефон")  # поле "служебный телефон"
    landline_telephone = models.CharField(max_length=20, verbose_name="городской телефон", blank=True)  # поле "городской телефон"
    service_fax = models.CharField(max_length=20, verbose_name="служебный факс", blank=True)  # поле "служебный факс"
    mobile_telephone = models.CharField(max_length=20, verbose_name="мобильный телефон", blank=True)  # поле "мобильный телефон"
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')  # дата и время создания
    update_at = models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')  # дата и время обновления
    # auto_now_add=True - время создания данной записи
    # auto_now=True - время создания или редактирования данной записи
    # verbose_name= - отображаемое имя в таблице админки
    # blank = True  - означает не обязательное к заполнению
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото', blank=True)  # upload_to='photos/' - место хранения фото
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")  # публикация, по умолчанию - истина
    note = models.TextField(blank=True, verbose_name="примечание")  # поле "примечание"
    service_email = models.CharField(max_length=150, verbose_name='почта', blank=True)  # поле с указание служебной почты

    division = models.ForeignKey('Division', on_delete=models.PROTECT, null=True, verbose_name='Подразделение')
    # ForeignKey - специфическое поле отношений (многие-к-одному)
    # on_delete = models.PROTECT -  в случае удаления одного из подразделений потребует переопределения данных в нем
    # on_delete = models.CASCADE -  в случае удаления одного из подразделений удалит все данные в нем
    # null = True - поскольку мы добовляем это поле гораздо позже, оно будет не заполнено, необходимо разрешить пустые поля

    military_unit = models.ForeignKey('MilitaryUnit', on_delete=models.PROTECT, null=True, verbose_name='Войсковая часть')
    # ForeignKey - специфическое поле отношений (многие-к-одному)
    # on_delete = models.PROTECT -  в случае удаления одного из подразделений потребует переопределения данных в нем
    # on_delete = models.CASCADE -  в случае удаления одного из подразделений удалит все данные в нем
    # null = True - поскольку мы добовляем это поле гораздо позже, оно будет не заполнено, необходимо разрешить пустые поля

    def __str__(self):  #  создадим функцию для вывода объектов (строк базы данных) не по номеру объекта (ID),
        # а по должности (position)
        # __str__ - Это строковое представление объекта
        return self.position

    class Meta:  # задаем параметры админки
        verbose_name = 'Запись'  # отображаемое значение в шапке админки
        verbose_name_plural = 'Записи'  # значение в множественном числе
        ordering = ['-create_at']  # сортировка выводимых значений в обратной последовательности даты создания

class Division(models.Model):  # создаем специфичиский класс к полю отношений "подразделение"
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование подразделения')

    def __str__(self):#  создадим функцию для вывода объектов (строк базы данных) не по номеру объекта (ID),
        # а по его строковому представлению подразделения (division)
        # __str__ - Это строковое представление объекта
        return self.title

    class Meta:  # задаем параметры админки
        verbose_name = 'Подразделение'  # отображаемое значение в шапке админки
        verbose_name_plural = 'Подразделения'  # значение в множественном числе
        ordering = ['id']   # указываем по какому полю идет сортировка


class MilitaryUnit(models.Model):  # создаем специфичиский класс к полю отношений "подразделение"
    title = models.CharField(max_length=7, db_index=True, verbose_name='№ в\ч')
    name_unity = models.CharField(max_length=150, db_index=True, null=True, verbose_name='Наименование в\ч')

    def __str__(self):#  создадим функцию для вывода объектов (строк базы данных) не по номеру объекта (ID),
        # а по его строковому представлению подразделения (division)
        # __str__ - Это строковое представление объекта
        return self.title

    class Meta:  # задаем параметры админки
        verbose_name = 'Войсковая часть'  # отображаемое значение в шапке админки
        verbose_name_plural = 'Воинские части'  # значение в множественном числе
        ordering = ['id']   # указываем по какому полю идет сортировка