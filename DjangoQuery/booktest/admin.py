from django.contrib import admin
from booktest.models import BookInfo,HeroInfo,LoginCheck,AreaInfo,PicTest
# Register your models here.
#注册模型类
#自定义模型管理类
admin.site.site_header = "技术平台"
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id','btitle','bpub_date']
class HeroInfoAdmin(admin.ModelAdmin):
    '''英雄人物模型管理类'''
    list_display = ['id','hname','hcomment','hbook_id']

class AreaStackedInline(admin.StackedInline):
	#写多类的名字
	model = AreaInfo
	extra = 2

class AreaTabularInline(admin.TabularInline):
	model = AreaInfo
	extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    '''地区模型管理类'''
    list_display = ['id', 'title', 'parent', 'atitle', 'aParent']
    list_filter = ['atitle']
    search_fields = ['aParent']
    list_per_page = 10  # 控制列表页数据每一页显示多少条
    actions_on_bottom = True
    actions_on_top = True
    # fields = ['aParent','atitle']
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )
    # inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(AreaInfo,AreaInfoAdmin)
admin.site.register(LoginCheck)
admin.site.register(PicTest)
