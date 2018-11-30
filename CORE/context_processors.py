# 全局渲染变量
# 在Django中可以通过设置context_processors，使到每一个模板视图被渲染时，都传相对应的Context值。
from .models import company
from django.contrib.auth.models  import User

# 设置各个View需要的共同变量，节省每次都需要获取，在setting文件中配置context_processors，
# 把如下函数配置进去列表中就可以了，系统自带传入这个字典的上下文，不需要单独制定传入
def get_settings(request):
    c = company()
    c.ENShortName ="BJC"
    c.CNShortName = "佰钧成"
    c.CNFullName = "武汉佰钧成技术有限责任公司"

    #测试一个用户，查询出该登录用户有几条未读的消息
    #admin=Employee.objects.get(pk=7)
    admin=User.objects.get(pk=2)
    MiniMails = admin.inReceiver.all()
    return({"corp":c,  "MiniMails":MiniMails})