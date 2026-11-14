from django.db import models

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип сайта (Админка и Сайт)", blank=True, null=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"

class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название документа")
    file = models.FileField(upload_to='documents/', verbose_name="Файл (PDF, Word)")

    class Meta:
        verbose_name = "Важный документ"
        verbose_name_plural = "Важные документы"

    def __str__(self):
        return self.title

class ClassCover(models.Model):
    class_name = models.CharField(max_length=10, unique=True, verbose_name="Класс")
    image = models.ImageField(upload_to='class_covers/', verbose_name="Обложка (картинка)")

    class Meta:
        verbose_name = "Обложка класса"
        verbose_name_plural = "Обложки классов"

    def __str__(self):
        return f"Обложка для {self.class_name}"

class Lesson(models.Model):
    CLASS_CHOICES = [
        ('1-2', '1-2 классы'),
        ('3-4', '3-4 классы'),
        ('5', '5 класс'),
        ('6-7', '6-7 классы'),
        ('8-9', '8-9 классы'),
        ('10-11', '10-11 классы'),
        ('СПО', 'СПО 1 курс'),
    ]

    title = models.CharField(max_length=200, verbose_name="Тема занятия")
    date = models.DateField(verbose_name="Дата проведения")
    target_audience = models.CharField(max_length=10, choices=CLASS_CHOICES, verbose_name="Класс (если не для всех)", blank=True)
    description = models.TextField(verbose_name="Краткое описание", blank=True)
    cover_image = models.ImageField(upload_to='covers/', verbose_name="Обложка занятия", blank=True, null=True)
    for_all_classes = models.BooleanField(default=False, verbose_name="Показывать для ВСЕХ классов")
    files_later = models.BooleanField(default=False, verbose_name="Загрузить файлы позже")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
        ordering = ['-date'] 

    def __str__(self):
        return f"{self.title} ({self.date})"

class LessonMaterial(models.Model):
    FILE_TYPES = [
        ('script', 'Сценарий'),
        ('presentation', 'Презентация'),
        ('video', 'Видео'),
        ('other', 'Другое'),
    ]
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials', verbose_name="Занятие")
    title = models.CharField(max_length=255, verbose_name="Название материала")
    file = models.FileField(upload_to='materials/', verbose_name="Файл")
    file_type = models.CharField(max_length=50, choices=FILE_TYPES, verbose_name="Тип файла", default='other')

    class Meta:
        verbose_name = "Материал занятия"
        verbose_name_plural = "Материалы занятия"

    def __str__(self):
        return self.title