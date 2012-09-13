# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.articles.models import Divide,Rubric,Tag,Spec_project,Article,PhotoAlbum,Photo,Author
from apps.utils.widgets import Redactor,RedactorMini
from sorl.thumbnail.admin import AdminImageMixin

class DivideAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug','order','show',)
	list_display_links = ('id','title',)
	list_editable = ('order','show','slug',)
	list_filter = ('show',)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('id','fullname',)
	list_display_links = ('id','fullname',)	
	search_fields = ('fullname',)

class RubricAdmin(admin.ModelAdmin):
	list_display = ('id','divide','title','slug','order','show',)
	list_display_links = ('id','title',)
	list_editable = ('order','show','slug',)
	list_filter = ('show','divide',)
	search_fields = ('title',)

class TagAdmin(admin.ModelAdmin):
	list_display = ('title',)

class Spec_projectAdmin(admin.ModelAdmin):
	list_display = ('title','order',)
	list_editable = ('order',)

class ArticleAdminForm(forms.ModelForm):
	short_text = forms.CharField(widget=RedactorMini(attrs={'cols': 100, 'rows': 7}))
	short_text.label=u'краткое описание'
	text = forms.CharField(widget=Redactor(attrs={'cols': 200, 'rows': 30}))
	text.label=u'текст статьи'

	class Meta:
		model = Article

class ArticleAdmin(AdminImageMixin,admin.ModelAdmin):
	list_display = ('id','title','slug','rubric','author','date_create','show')
	list_display_links = ('id','title',)
	list_editable = ('show','slug',)
	list_filter = ('show','is_on_main','date_create','rubric','author',)
	search_fields = ('title','short_text','text','rubric__title','author__username','author__first_name','author__last_name')
	raw_id_fields = ('rubric',)		
	filter_horizontal = ('tag',)
	form = ArticleAdminForm

class PhotoInline(AdminImageMixin,admin.TabularInline):
	model = Photo

class PhotoAlbumAdmin(admin.ModelAdmin):
	list_display = ('id','article','author','date_create','show')
	list_display_links = ('id','article',)
	list_editable = ('show','author',)
	list_filter = ('show','date_create','author',)
	raw_id_fields = ('article',)	
	search_fields = ('article__title','author',)
	inlines = [
        PhotoInline,
    ]

admin.site.register(Divide, DivideAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Rubric, RubricAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Spec_project, Spec_projectAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PhotoAlbum, PhotoAlbumAdmin)