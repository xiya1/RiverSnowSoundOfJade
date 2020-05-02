from django.http import HttpResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class BlockIPSMiddleware(MiddlewareMixin):
    '''中间件类'''
    EXCLUIDE_IPS = ['127.0.0.1']
    def process_view(self,request,view_func,*view_args,**view_kwargs):
        '''视图函数调用之前会进行调用该函数'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockIPSMiddleware.EXCLUIDE_IPS:
            return HttpResponse('<h1>禁止</h1>')

class TestMiddleware(MiddlewareMixin):
    def __init__(self,get_response):
        '''服务器重启之后接受第一个请求时调用'''
        self.get_response = get_response
        print('---init---')

    def process_request(self,request):
        '''产生request对象之后,url调用之前调用'''
        print('中间件1的请求')
        return HttpResponse('OK111')

    # def process_view(self,request,view_func,*view_args,**view_kwargs):
    #     '''url调用之后，view调用之前调用'''
    #     print('---process_view---')
    def __call__(self, request):
        # return HttpResponse('1231')
        print('中间件1的 view前调用')
        response = self.get_response(request)

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print('中间件1的 view之后调用')
        return response

    def process_response(self,request,response):
        '''view调用之后，返回结果给浏览器结果之前调用'''
        print('---process_response---')
        return response
    #process_esception调用时从settings.py中的MIDDELWARE从下往上进行搜索调用