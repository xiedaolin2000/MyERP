'''
文档定义全局公共引用对象
'''
from django.db import models

class company(object):
    ENShortName=""
    CNShortName=""
    ENFullName=""
    CNFullName=""

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
    sender = models.ForeignKey('HR.Employee',   on_delete=models.DO_NOTHING,  related_name="inSender" )

    #信息接收者
    receiver = models.ForeignKey('HR.Employee',  on_delete=models.DO_NOTHING,  related_name="inReceiver" )
    #消息是否已读
    read = models.BooleanField(verbose_name="是否已读", default=False)
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

    def __str__(self):
        return self.msgTitle
