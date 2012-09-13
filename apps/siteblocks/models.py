# -*- coding: utf-8 -*-
from django.db import models
import datetime
import os
from pytils.translit import translify
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from apps.utils.managers import PublishedManager
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from apps.utils.managers import VisibleObjects

def image_path(self, instance, filename):
    filename = translify(filename).replace(' ', '_')
    return os.path.join('uploads', 'images/menu', filename)

class SiteMenu(MPTTModel):
    title = models.CharField(
        max_length = 150, 
        verbose_name = u'название'
    )
    image = models.ImageField(
        verbose_name=u'иконка', 
        upload_to = image_path, 
        blank = True,
        null = True,
    )
    parent = TreeForeignKey(
        'self',
        verbose_name = u'родительский раздел',
        related_name = 'children',
        blank = True,
        null = True,
    )
    url = models.CharField(
        verbose_name = u'url', 
        max_length = 150, 
    )
    order = models.IntegerField(
        verbose_name = u'порядок сортировки',
        default = 0, 
        help_text = u'чем больше число, тем ниже располагается элемент'
    )
    is_published = models.BooleanField(
        verbose_name=u'опубликовано',
        default=True, 
    )

    objects = TreeManager()

    class Meta:
        verbose_name= _(u'menu_element')
        verbose_name_plural = _(u'menu_elements')
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['order']

    def __unicode__(self):
        return self.title

    def save(self, **kwargs):
        # remove the first and the last space
        self.title = self.title.strip()
        self.url = self.url.strip()
        # get level
        super(SiteMenu, self).save(**kwargs)

class Settings(models.Model):
    title = models.CharField(
        verbose_name = u'название', 
        max_length = 150,
    )
    name = models.CharField( 
        verbose_name = u'служебное имя',
        max_length = 250,
    )
    value = models.TextField(
        verbose_name = u'значение'
    )

    class Meta:
        verbose_name = _(u'setting')
        verbose_name_plural = _(u'setting_plural')

    def __unicode__(self):
        return u'%s' % self.name

def file_path_Banner(instance, filename):
    return os.path.join('images','banners', translify(filename).replace(' ', '_') )

slot_choices = (
    (u'header',u'слот 1'),
    (u'footer',u'слот 2'),
    )

class Banner(models.Model):
    title = models.CharField(
        u'название',
        max_length = 150,
    )
    banner_file = models.FileField(
        upload_to=file_path_Banner,
        help_text=u'Размер баннера 180х180 пикс.',        
        blank=True,
        verbose_name = u'Файл',
    )
    url = models.URLField(
        u'url',
        blank=True         
    )
    is_blank = models.BooleanField(
        u'открывать на новой странице',    
    )  
    slot = models.CharField(
        u'слот',
        choices=slot_choices,
        max_length=20
    )
    flash = models.BooleanField(
        verbose_name = u'Flash',
        default = False
    )
    # свой manager для отображения show = True
    show = models.BooleanField(
        verbose_name=u'Отображать',
        default=True
    )
    objects = models.Manager() # The default manager.
    items = VisibleObjects() # The visible objects manager.
    # 

    class Meta:
        verbose_name = _(u'banner_item')
        verbose_name_plural = _(u'banner_items')

    def __unicode__(self):
        return self.title

    def get_src_file(self):
        return self.banner_file.url    
