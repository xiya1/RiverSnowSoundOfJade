from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo,HeroInfo,LoginCheck,AreaInfo,PicTest
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageDraw, ImageFont
# from django.utils.six import BytesIO
from io import BytesIO
from django.conf import settings
from django.db.models import Q,F,Count,Sum,Avg,Max,Min
from django.core.paginator import Paginator


#定义装饰器函数
def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request,*view_args,**view_kwargs):
        #判断用户是否登录
        print('开始进行判断是否登录')
        if request.session.has_key('islogin'):
            print('已经登录')
            #用户已登录,调用对应视图
            return view_func(request,*view_args,**view_kwargs)
        else:
            print('用户未登录')
            # 用户未登录，跳转至首页
            return redirect('/login')
    return wrapper
EXCLUIDE_IPS = ['192.168.8.101']
#定义页面访问是否在禁止访问ip范围内
def blockeds_ips(view_func):
    def wrapper(request,*view_args,**view_kwargs):
        #获取浏览器的ip地址
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUIDE_IPS:
            return HttpResponse('<h1>禁止</h1>')
        else:
            return view_func(request,*view_args,**view_kwargs)
    return wrapper

# Create your views here.
#1.httprequest类型的一个对象，定义视图类时需有该参数
#2.进行url配置，建立url地质和视图的对应关系
#http://127.0.0.1:8000/index
def my_render(request,templat_path,context_dict={}):
    temp = loader.get_template(templat_path)
    # 2.定义模板上下文，给模板文件传递数据
    context = RequestContext(request,context_dict)
    context.push(locals())
    # 3.模板渲染：产生标准的html内容
    res_html = temp.render(context=locals(), request=request)
    # 4.返回给浏览器
    return HttpResponse(res_html)



# def index(request):
#     # 进行处理 和M、T进行交互
#     # return HttpResponse('你好132呀')
#     #1.加载模板文件
#     # return my_render(request,'booktest/index.html')
#     return render(request,'booktest/index.html',{'content':'hello world',
#                                                  'list':list(range(1,10))},
#                  )

def index2(request):
    return HttpResponse('hello python')

def show_books(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

def detail(request,bid):
    '''查询图书关联的英雄信息'''
    #!.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    #2.查询和book关联的英雄信息
    heros = book.heroinfo_set.all()
    #3.使用模板进行传递
    return render(request,'booktest/detail.html',{
        'book':book,'heros':heros
    })

def create(request):
    '''新增一本图书'''
    #1.创建对象
    b= BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    #2.保存进数据库
    b.save()
    #3.返回应答
    # return HttpResponse('OK!')
    #url重定向
    return HttpResponseRedirect('/index')


#登录校验视图
def login_check(request):
   #request.POST保存的事post提交的参数
   #request.GET保存的是get提交的参数
   #1.获取提交的用户名和密码
    # print(type(request.POST))
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = HeroInfo.objects.filter(hname=username)
    pwd = HeroInfo.objects.filter(hcomment=password)
   #2.进行登录的校验:
    if user.count()!=0 and pwd.count()!=0:
    # if username == 'jiang' and password == 'jiang':
        return redirect('/index1')
    else:
        return redirect('/login')
   #3.进行应答

def ajax_test(request):
    '''ajax功能验证'''
    return render(request,'booktest/ajax_test.html')

def ajax_handle(request):
    return JsonResponse({'res':1})

#ajax登录页面
def login_ajax(request):
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    if 'password' in request.COOKIES:
        password = request.COOKIES['password']
    else:
        password=''
    return render(request,'booktest/login_ajax.html',{'username':username,'password':password})

#ajax登录处理函数
# def login_ajax_check(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     rememberuser = request.POST.get('rememberuser')
#     rememberpwd = request.POST.get('rememberpwd')
#     user = HeroInfo.objects.filter(hname=username)
#     pwd = HeroInfo.objects.filter(hcomment=password)
#     if user.count() != 0 and pwd.count() != 0:
#     # if username == 'jiang' and password == 'jiang':
#         response = JsonResponse({'res':1})
#         if rememberuser == 'true':
#             response.set_cookie('username',username,max_age=7*24*3600)
#         if rememberpwd == 'true':
#             response.set_cookie('password',password,max_age=7*24*3600)
#         return response
#     else:
#         return JsonResponse({'res':0})

def index(request):
    #1.加载模板文件，获取一个模板对象
    temp = loader.get_template('booktest/index.html')
    #2.定义模板上下文，给模板文件传输数据
    # context = RequestContext(request,{})
    context = {'ni':123}
    #3.模板渲染，产生一个替换后的内容
    res_html = temp.render(context)
    #4.返回应答
    return HttpResponse(res_html)



def login(request):
    return render(request,'booktest/login.html')

@csrf_exempt
#验证用户名密码的正确性
def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    #获取用户输入的验证码
    vcode1 = request.POST.get('vcode')
    print('获取用户输入验证码成功')
    #获取session中的验证码
    vcode2 = request.session.get('verifycode')
    if vcode1 != vcode2:
        #验证码错误
        print('验证码错误，返回登录页')
        return redirect('/login')
    loginnum = LoginCheck.objects.filter(Lusername=username,Lpassword=password,is_delete=True)
    if loginnum.count() == 1:
       response = JsonResponse({'res':1})
       # response.set_cookie('username',username)
       # response.set_cookie('password', password)
       request.session['username'] = username
       request.session['password'] = password
       request.session['islogin'] = True
       print('设置session成功')
       return response
    else:
        return JsonResponse({'res':0})

#用户注册页面
def regeister(request):
    return render(request,'booktest/regeister.html')

#用户注册数据写入数据库
def regeisterpost(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    verifypassword = request.POST.get('verifypassword')
    login_check = LoginCheck()
    login_check.Lusername = username
    login_check.Lpassword = password
    login_check.save()
    return JsonResponse({'res':1})

#设置session
def set_session(request):
    request.session['username'] = 'jiang'
    request.session['password'] = 123
    # 设置session过期时间
    request.session.set_expiry(0)
    return HttpResponse('设置session成功！')

#获取session
def get_session(request):
    username = request.session['username']
    password = request.session['password']
    return HttpResponse(username + ':'+str(password))

#删除session中的数据部分
def clear_session(request):
    request.session.clear()
    return HttpResponse('清除session数据成功!')


#删除session中的全部内容
def flush_session(request):
    request.session.flush()
    return HttpResponse('清除session全部内容成功！')

#设置cookie
def set_cookie(request):
    response = HttpResponse('设置cookie')
    response.set_cookie('shiniya',123)
    return response

#获取cookie
def get_cookie(request):
    user = request.COOKIES['shiniya']
    return HttpResponse(user)

#设置模板标签
def temp_var(request):
    lc = LoginCheck.objects.all()
    return render(request,'booktest/temp_var.html',{'lc':lc})

#模板继承
def child(request):
    return render(request,'booktest/child1.html')




#/change_pwd
@login_required
def change_pwd(request):
    return render(request,'booktest/change_pwd.html')


#/change_pwd_action
@login_required
def change_pwd_action(request):
    '''模拟修改密码处理'''
    #1.获取新密码
    pwd = request.POST.get('pwd')
    #2.修改对应数据库中内容
    username = request.session['username']
    password = request.session['password']
    user = LoginCheck.objects.get(Lusername=username, Lpassword=password)
    if user:
        user.Lpassword = pwd
        user.save()
        return HttpResponse('%s修改密码为：%s' %(username,pwd))
    #3.返回一个应答
    return HttpResponse('修改失败')


#产生图片验证码:pillow模块
def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('C:\Windows\Fonts\simsunb.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

from django.urls import reverse
#测试url反向解析功能，即namesoace
def url_reverse(request):
    return render(request,'booktest/url_reverse.html')


#关键字参数-url
def show_args(request,a,b):

    return HttpResponse(a+':'+b)

#位置参数
def show_kwargs(request,c,d):
    return HttpResponse(c+':'+d)

def test_redirect(request):
# 函数实现url反向解析
#位置参数
    url = reverse('booktest:show_args',args=(1,3))
#关键字参数
    url2 = reverse('booktest:show_kwargs',kwargs={'c':4,'d':7})
    return redirect(url2)

#测试url静态文件的配置功能
def static_test(request):
    print(settings.STATICFILES_FINDERS)
    #['django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
    return render(request,'booktest/static_test.html')

# @blockeds_ips
def indextwo(request):
    '''首页'''
    print('江')
    return render(request,'booktest/index2.html')

#模板继承
def river(request):
    return render(request,'booktest/river.html',{'content':'<h1>a11d</h1>'})


def show_upload(request):
    return render(request,'booktest/upload_to.html')

#上传图片处理
def upload_handle(request):
    #1.获取上传文件的处理对象
    pic = request.FILES.get('pic')
    # print(type(pic))
    # print(pic.name)
    # pic.chunks()
    '''<class 'django.core.files.uploadedfile.TemporaryUploadedFile'>'''
    '''"django.core.files.uploadhandler.MemoryFileUploadHandler"'''
    #上传文件不大于2.5M，文件放在内存中
    #上传文件大于2.5M，文件放在一个临时文件中
    #2.创建一个文件
    save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT,pic.name)
    with open(save_path,'wb') as f:
    #3.获取上传文件的内容，并写入创建的文件中
        for content in pic.chunks():
            f.write(content)
    #4.保存上传文件的记录，写入数据库
    PicTest.objects.create(goods_pic = 'booktest/%s'%pic.name)
    #5.返回
    return HttpResponse('OK')

def show_area(request,pindex):
    '''分页'''
    #1.查询所有省级地区对应的信息
    areas = AreaInfo.objects.filter(aParent__isnull = True)
    #分页,每页显示十条
    paginator = Paginator(areas,10)
    print(paginator.num_pages)
    print(paginator.page_range)
    #获取第一页的内容,page是Page的实例对象
    if pindex == '':
        pindex = 1;
    else:
        pidnex = int(pindex)
    # print('pidnex'+str(pidnex))
    page = paginator.page(pindex)
    print(page.number)
    if page.has_previous:
        print('yes')
    if page.has_next:
        print('下一页yes')
    print(page.previous_page_number)
    print(page.next_page_number)
    #2.使用模板
    return render(request,'booktest/show_area.html',{'page':page})

#省市县案例
def areas(request):
    return render(request,'booktest/areas.html')

def prov(request):
    #获取所有省级地区的信息
    print('开始获取所有省级地区信息')
    areas = AreaInfo.objects.filter(aParent__isnull = True)
    #变例areas拼接出json数据:标题:atitle id
    areas_list = []
    print('开始遍历省级地区信息')
    for area in areas:
        areas_list.append((area.id,area.atitle))
    #返回数据
    print('遍历完成，发送省级信息json给ajax')
    return JsonResponse({'data':areas_list})

def city(request,pid):
    '''获取pid的下级地区信息'''
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    print('开始获取所有市级地区信息')
    areas = AreaInfo.objects.filter(aParent__id=pid)
    areas_list = []
    print('开始遍历市级地区信息')
    for area in areas:
        areas_list.append((area.id,area.atitle))
    #返回数据
    print('遍历完成，发送市级信息json给ajax')
    return JsonResponse({'data':areas_list})

# def dis(request,pid):
#     '''获取pid的下级地区信息'''
#     # area = AreaInfo.objects.get(id=pid)
#     # areas = area.areainfo_set.all()
#     print('开始获取所有县1级地区信息')
#     areas = AreaInfo.objects.filter(aParent__id=pid)
#     areas_list = []
#     print('开始遍历县1级地区信息')
#     for area in areas:
#         areas_list.append((area.id,area.atitle))
#     #返回数据
#     print('遍历完成，发送县1级信息json给ajax')
#     return JsonResponse({'data':areas_list})



def set_session(request):
    '''设置session'''
    request.session['username'] = 'smart'
    request.session['age'] = 16
    return HttpResponse('设置session')

def get_session(request):
    '''获取session'''
    useranme = request.session['username']
    age = request.session['age']
    return HttpResponse(useranme+':'+str(age))