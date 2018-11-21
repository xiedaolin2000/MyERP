from django.db import models


class ERPconfig(models.Model):
    '''
    所有系统配置项统一配置在配置这里，配置中心。
    '''
    # 配置项编码，唯一不重复
    cfgCode = models.CharField("配置项编码", max_length=10, blank=False, null=False)
    # 表明这个配置项是针对哪个APP的配置，如果是全局则为ALL
    cfgAppName = models.CharField("应用名称", max_length=10, blank=False, null=False,default="ALL")
    # 配置项的名称，说明配置项值
    cfgName = models.CharField("配置项名称",max_length=50, blank=False, null=False)
    # 配置的类型，是字符串、还是数值、还是日期，用于校验
    cfgType = models.CharField("配置项值类型", max_length=50, blank=False, null=False)
    #配置项的值
    cfgValue = models.CharField("配置值",max_length=30, blank=False, null=False)

    def __str__(self):
        return "config items"

