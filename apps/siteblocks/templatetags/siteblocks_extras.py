# -*- coding: utf-8 -*-
from apps.siteblocks.models import SiteMenu, Settings, Banner
from apps.articles.models import Divide,Article,PhotoAlbum
from apps.pages.models import Page
import datetime

from django import template

register = template.Library()

def get_active_menu(url, site_menu):
    
    request_path = url
    
    for i, menu_item in enumerate(site_menu):
        setattr(site_menu[i], 'is_active', False)
        #if request_path.startswith(menu_item.path):
            #site_menu[i].is_active = True


    for i, menu_item in enumerate(site_menu):
        setattr(site_menu[i], 'is_active', False)
        if not menu_item.parent:
            for menu_subitem in site_menu:
                # highlight parent menu item
                if menu_subitem.parent == menu_item and menu_subitem.is_active:
                    site_menu[i].is_active = True
        elif menu_item.is_active:
            for menu_subitem in site_menu:
                # remove redundant sibling highlight
                if menu_subitem.parent \
                     and menu_subitem.parent.path == menu_item.parent.path \
                     and menu_subitem.path.startswith(menu_item.path) \
                     and len(menu_subitem.path) > len(menu_item.path) \
                     and menu_subitem.is_active:
                        site_menu[i].is_active = False
    return site_menu

@register.inclusion_tag("siteblocks/block_menu.html")
def block_menu(url):
    url = url.split('/')
    
    if url[1] and not url[2]:
        current = u'/%s/' % url[1]
    elif url[1] and url[2]:
        current = u'/%s/%s/' % (url[1],url[2])
    else:
        current = u'/'

    if url[1]:
        currentM = u'/%s/' % url[1]
    else:
        currentM = u'/'

    divides = Divide.items.all()
    menus = SiteMenu.objects.all()
    #menus = get_active_menu(url, menus)
    return {'divides': divides, 'menus':menus ,'current': current,'currentM': currentM}

@register.inclusion_tag("siteblocks/block_setting.html")
def block_static(name):
    try:
        setting = Settings.objects.get(name = name)
    except Settings.DoesNotExist:
        setting = False
    return {'block': block,}

@register.inclusion_tag("siteblocks/block_menu_footer.html")
def block_menu_footer():
    pages = Page.objects.all().order_by('-order')
    return {'pages': pages,}

@register.inclusion_tag("siteblocks/block_content_t.html")
def block_content_t():
    article_id_list = PhotoAlbum.items.filter(article__isnull=False).values_list('article', flat=True)
    articles = Article.items.filter(pk__in=article_id_list).exclude(image='').order_by('-date_create')[:9]
    return {'articlesByAlbums': articles,}

@register.inclusion_tag("siteblocks/block_banner.html")
def block_banner(place):
    banners = Banner.items.all()
    if banners:
        if place == 'double':
            banner = banners.filter(slot = 'header')       
            banner = banner.order_by('?')
            bannerSecond = banners.filter(slot = 'footer')      
            bannerSecond = bannerSecond.order_by('?') 
        else:
            banner = banners.filter(slot = place)
            banner = banners.order_by('?')
            bannerSecond = ['','']
        return {
            'banner': banner[0],
            'bannerSecond':bannerSecond[0],
        }
    else:        
        return {
            'banner': '',
            'bannerSecond':'',
        }

@register.simple_tag()
def years(start):
    if str(datetime.datetime.now().year)!=start:
        return u'%s-%s' % (start, datetime.datetime.now().year)
    else:
        return u'%s' % start
