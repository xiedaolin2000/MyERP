from django.db import models


class ERPconfig(models.Model):
    '''
    所有系统配置项统一配置在配置这里，配置中心。
    '''
    # 配置项编码，唯一不重复
    cfgCode = models.CharField("配置项编码", max_length=10, blank=False, null=False)
    # 表明这个配置项是针对哪个APP的配置，如果是全局则为ALL
    cfgAppName = models.CharField("应用名称", max_length=10, blank=False, null=False, default="ALL")
    # 配置项的名称，说明配置项值
    cfgName = models.CharField("配置项名称",max_length=50, blank=False, null=False)
    # 配置的类型，是字符串、还是数值、还是日期，用于校验
    cfgType = models.CharField("配置项值类型", max_length=50, blank=False, null=False)
    #配置项的值
    cfgValue = models.CharField("配置值",    max_length=30, blank=False, null=False)

    def __str__(self):
        return "config items"

class Organization(models.Model):
    """
    系统的组织结构图存储模型
    """
    # 0 表示根节点
    nodeID     = models.IntegerField("部门编号", primary_key=True,auto_created=True)
    nodeName   = models.CharField("部门名称",max_length=50, blank=False, null=False)
    #自己引用自己的数据，使用self关键字
    nodeParent = models.ForeignKey('self',  on_delete=models.CASCADE, verbose_name="上级部门")
    #距离根节点深度
    level      = models.IntegerField("几级部门", default = 1)

    def __str__(self):
        return self.nodeName

class company(object):
    ENShortName=""
    CNShortName=""
    ENFullName=""
    CNFullName=""

from django.contrib.auth.models import User

class MessageIn(models.Model):
    '''
    消息模型，用于消息消息发送，转发。
    类似内部用户的收件、发件箱
    本模型用于收件箱
    '''
    msgTitle   = models.CharField(verbose_name = "主题", max_length=50, blank=False, null=False, default = "无主题")
    msgContent = models.CharField(verbose_name = "内容", max_length=300,  default = "")
    #消息存储的是发出的消息还是接收消息 I---收到， O---发出
    msgType = models.CharField(verbose_name = "类型",max_length=1, choices=(("I","收件箱"), ("O","发件箱")), default = "I" )
    
    #信息是所有者，也就是谁发出的信息
    sender = models.ForeignKey(User,   on_delete=models.DO_NOTHING,  related_name="inSender" )
    #信息接收者
    receiver = models.ForeignKey(User,  on_delete=models.DO_NOTHING,  related_name="inReceiver" )
    #消息是否已读
    read = models.BooleanField(verbose_name="是否已读", default=False)
    #消息接收时间
    inDatetime = models.DateTimeField(verbose_name="接收时间",auto_now=True)
    def __str__(self):
        return ("主题：%s 内容：%s"%(self.msgTitle, self.msgContent))

class MessageOut(models.Model):
    '''
    消息模型，用于消息消息发送，转发。
    类似内部用户的收件、发件箱
    本模型用于发件箱
    '''
    msgTitle   = models.CharField(verbose_name = "主题", max_length=50, blank=False, null=False, default = "无主题")
    msgContent = models.CharField(verbose_name = "内容", max_length=300,  default = "")
    #消息存储的是发出的消息还是接收消息 I---收到， O---发出
    msgType = models.CharField(verbose_name = "类型",max_length=1, choices=(("I","收件箱"), ("O","发件箱")), default = "I" )
    
    #信息是所有者，也就是谁发出的信息
    sender = models.ForeignKey('HR.Employee',   on_delete=models.DO_NOTHING, related_name="outSender" )
    #信息接收者
    receiver = models.ForeignKey('HR.Employee',  on_delete=models.DO_NOTHING, related_name="outReceiver" )

    #消息接收时间
    outDatetime = models.DateTimeField(verbose_name="发送时间", auto_now=True)

    def __str__(self):
        return self.msgTitle
