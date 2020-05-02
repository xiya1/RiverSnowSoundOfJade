from django.db import models

# # Create your models here.
# class BookInfo(models.Model):
#     btitle = models.CharField(max_length=20)
#     bpub_date = models.DateField()
#
#     def __str__(self):
#         return self.btitle
# #英雄人物类 名称 hname
#             # 性别 hgender
#             # 年龄 hage
#             # 备注 hcomment
# #定义关系属性，建立图书类和英雄人物类之间的一对多关系
# #关系属性 hbook
#
# class HeroInfo(models.Model):
#     hname = models.CharField(max_length=20)
#     #性别默认代表男 说明默认是bool类型
#     hgender = models.BooleanField(default=False)
#    # hage = models.IntegerField()
#     hcomment = models.CharField(max_length=128)
#
#     hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
#     def __str__(self):
#         return self.hname
class BookInfo(models.Model):
    #图书名称
    btitle = models.CharField(max_length=20,unique=False,db_index=False)
    # 出版日期
    bpub_date = models.DateField(auto_now=False,auto_now_add=False)
    #最大位数，价格
    # bprice = models.DecimalField(max_digits=10,decimal_places=2)
    #阅读量
    bread = models.IntegerField(default=0)
    #评论量
    bcomment = models.IntegerField(default=0)
    #删除标记
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    #英雄名称
    hname = models.CharField(max_length=20)
    #英雄性别
    hgender = models.BooleanField(default=False)
    #备注
    hcomment = models.CharField(max_length=128)
    #定义关联属性
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    #删除标记
    isDelete = models.BooleanField(default=False)

class NewsType(models.Model):
    type_name = models.CharField(max_length=20)
    type_mews = models.ManyToManyField('NewsInfo')

class NewsInfo(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    # class Meta():
    #     db_table = 'booktest2'


class LoginCheck(models.Model):
    Lusername = models.CharField(max_length=20,unique=True)
    Lpassword = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=True)
    class Meta:
        db_table = 'logincheck'

class AreaInfo(models.Model):
    atitle = models.CharField(verbose_name = '标题',max_length=20)
    aParent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.atitle
    def title(self):
        return self.atitle
    def parent(self):
        return self.aParent
    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'
    parent.admin_order_field = 'aParent'
    parent.short_description = '上级地区名称'

    def parents(self):
        if self.aParent is None:
            return ''
        else:
            return self.aParent.atitle

    parents.admin_order_field = 'atitle'
    parents.short_description = '父级地区名称'

#后台管理上传图片
class PicTest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to = 'booktest')