#coding:utf-8
from django.views.generic import ListView
from pdf_gen import GenPDF
#采用post方法请求pdf文件，使用ListView试图，覆盖post方法
class ObjectListView(ListView):
    context_object_name = 'object_list'
    paginate_by = PAGE_NUM

    def post(self,request,**kwargs):
        name = self.kwargs.get('name','')
        admin_str = name + "_admin"
        page = request.POST.get('page',None)
        page = int(page)
        begin = (page-1)*PAGE_NUM
        end = page*PAGE_NUM - 1
        admin_setting = getattr(admin_settings,admin_str,None)
        list_display = admin_setting['list_display']                #表头
        result = ObjectListView.model.objects.values(*list_display)[begin:end]      #返回的是字典的列表 eg:[{},{},{}]
        
        return GenPDF(tablename=name,head=list_display,result=result)

