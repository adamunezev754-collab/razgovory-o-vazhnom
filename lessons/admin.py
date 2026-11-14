from django.contrib import admin
from .models import Lesson, SiteSettings, Document, ClassCover, LessonMaterial

class LessonMaterialInline(admin.TabularInline):
    model = LessonMaterial
    extra = 1
    verbose_name = "Материал"
    verbose_name_plural = "Материалы (файлы)"

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    verbose_name = "Настройки"
    verbose_name_plural = "Настройки сайта"

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    verbose_name = "Документ"
    verbose_name_plural = "Важные документы"

@admin.register(ClassCover)
class ClassCoverAdmin(admin.ModelAdmin):
    list_display = ('class_name',)
    verbose_name = "Обложка класса"
    verbose_name_plural = "Обложки классов"

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'get_audience', 'is_published')
    list_filter = ('target_audience', 'for_all_classes', 'is_published')
    inlines = [LessonMaterialInline]
    verbose_name = "Занятие"
    verbose_name_plural = "Занятия"

    # Добавили поле files_later в отображение формы
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'date', 'target_audience', 'for_all_classes', 'description', 'cover_image', 'files_later', 'is_published')
        }),
    )

    def get_audience(self, obj):
        if obj.for_all_classes:
            return "Все классы"
        return obj.get_target_audience_display()
    get_audience.short_description = "Класс"