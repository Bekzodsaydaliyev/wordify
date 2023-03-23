from django.contrib import admin
from .models import Article, Tag, Category, SubContent, SubContentImage, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date']
    list_filter = ['category', 'tags']
    search_fields = ['id', 'title']
    date_hierarchy = 'created_date'
    filter_horizontal = ['tags', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']


@admin.register(SubContent)
class SubContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article']


@admin.register(SubContentImage)
class SubContentImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sub_content']

