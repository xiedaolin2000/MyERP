from django.db import models
from datetime import date

# Create your models here.
#增加紧急联系人
class Person(models.Model):
    """
    人员信息，包含基本信息属性
    """
    # verbose_name = "员工详细信息"
    #第一个参数表示字段的自述名称，或者使用verbose_name="XXXX"，但是OneToOneField第一个参数被占用了
    # staff = models.OneToOneField(auth.user, primary_key=True, verbose_name="员工姓名")
    #staff = models.OneToOneField(User, primary_key=True, verbose_name="员工姓名")
    #员工姓名
    userName = models.CharField("姓名", max_length=15, default="张三")
    #公司工号
    workNo = models.CharField("公司工号", max_length=15,default="B-12345")
    #华为工号
    workNoExt = models.CharField("华为工号", max_length=15, null=True)
    #手机号码
    mobilePhone = models.CharField("手机号码", max_length=11, default="18600000000")
    #身份证号码
    IDNo = models.CharField("身份证", max_length=18)
    #电子邮箱
    email = models.EmailField("电子邮箱", max_length=50, null=True)
    #电子邮箱2
    email2 = models.EmailField("华为邮箱", max_length=50, null=True)

    #性别字段只能是0或1的值，元组第一位表示保存的值，第二位表示显示的值
    sex = models.CharField("性别", max_length=1, choices=(("0", "女"), ("1", "男")), default="1")
    # 岗位级别
    levelList = (
        ("00",   "00"),
        ("1B",   "1B"), ("1A",   "1A"), ("2B",   "2B"), ("2A",   "2A"),
        ("3B",   "3B"), ("3A",   "3A"), ("4B",   "4B"), ("4A",   "4A"),
        ("5B",   "5B"), ("5A",   "5A"), ("6B",   "6B"), ("6A",   "6A"),
        ("7B",   "7B"), ("7A",   "7A"), ("8B",   "8B"), ("8A",   "8A"),
        ("9B",   "9B"), ("9A",   "9A"), ("10B", "10B"), ("10A", "10A"),
        ("11B", "11B"), ("11A", "11A"), ("12B", "12B"), ("12A", "12A")
    )
    level = models.CharField("岗位级别", max_length=4, choices=levelList, default="4A")
    # 到岗日期/入职日期
    entryDate = models.DateField("入职日期", default=date.today)
    # 部门
    depart = models.CharField("部门", max_length=10, default="0", null=True)
    # 业务线
    productUnit = models.CharField("产品线", max_length=10, default="0",null=True)
    # 项目组
    projectName = models.CharField("项目组名", max_length=20, default="0",null=True)
    # 籍贯省
    provinceBirth = models.CharField("籍贯省份", max_length=20,null=True, default="江苏省")
    # 籍贯市
    cityBirth = models.CharField("籍贯市", max_length=20,null=True, default="南京市")
    # 出生日期
    birthDay = models.DateField("出生日期", null=True,default=date.today)
    # 婚姻状况
    maritalStatus = models.CharField("婚姻状况", max_length=1, 
        choices=(('0','未婚'), ('1','已婚'), ('2','离异')), default="0")
  
    #员工住址 ，第一个参数表示字段的自述名称，或者使用verbose_name="XXXX"
    address = models.CharField("住址", max_length=200, null=True)
    # 毕业院校
    graduatedSchool = models.CharField("毕业学校", max_length=20, null=True,default="大学")
    # 学历
    education = models.CharField("学历", max_length=1,
    choices=(('0', '小学'), ('1', '初中'), ('2', '高中'), ('3', '大专'), ('4', '本科'), ('5', '研究生')),null=True, default="4")
    # 大学专业名称
    profession = models.CharField("专业", max_length=20, null=True, default="")
    # 毕业时间
    graduatedDay = models.DateField("毕业日期", null=True,default=date.today)
    
   #人员在职状态 用两位数字字符表现 XY: 
	#（X=0 Y=0-9 归类为正常，基本计算正常成本，00 在职,01 出差，02 外出公干，03 调休；）
	#（X=1 Y=0-9 归类为福利请假：01 婚假，02 陪产假，03 病假，04 丧假，05 产假，06产检假，07 哺乳假）
	#（X=9 Y=0-9 归类为不在职：90 离职，91 辞退）
    workStatus = models.CharField(verbose_name = "工作状态", max_length=5, 
        choices=(('00','在职'), ('11','请假'), ('99','离职')), default="00", blank=False, null=False)

  
    def get_absolute_url(self):
        from django.urls import reverse
        # return reverse('PersonListView', kwargs={'pk': self.pk})
        return reverse('PersonListView')

    class Meta:
        ordering = ["-entryDate"]
    def __str__(self):
        return self.userName

#薪资调整记录
class Salary(models.Model):
    """
    员工薪资调整的详细数据
    """
    #员工
    person = models.ForeignKey(Person,on_delete=models.CASCADE , verbose_name="员工")
    #调薪生效日期，也就是说薪资是在几月份进行生效的
    applyDate = models.DateField("生效月份", default=date.today)
    #调薪幅度
    adjustRange = models.IntegerField("调薪幅度", default=0)
    #调整后薪资
    salaryFinal = models.IntegerField("调整后薪资", default=0)
    #调薪日期
    adjustDate = models.DateField("调薪日期", default=date.today)
    #备注
    notes = models.CharField("备注", max_length=200, blank=True, null=True)
    #此处表示表名字
    verbose_name = "薪资调整数据"
    def __str__(self):
        return self.person

#员工绩效考评记录
class Performace(models.Model):
    """
    员工绩效考核表
    Employee performance evaluation review
    """
    #关联员工表数据，多对一 ；外键要定义在‘多’的一方
    person     = models.ForeignKey(Person,on_delete=models.CASCADE, verbose_name="员工")

    #绩效考察周期
    dateRange  = models.CharField(verbose_name ="考核周期", max_length=10, default="2018Q1", blank=True, null=True)  

    #绩效得分    
    total      = models.IntegerField(verbose_name ="绩效得分",default=0,blank=True, null=True)

    #绩效结果
    result     = models.CharField(verbose_name ="绩效结果", max_length=10, blank=True, null=True)

    #绩效考评人
    appraisers = models.CharField(verbose_name ="考评人", max_length=10, blank=True, null=True)

    #备注
    notes      = models.CharField(verbose_name = "备注", max_length=200, blank=True, null=True)

    def __str__(self):
        return ""

class PerformaceDetail(models.Model):
    """
    员工绩效考评明细项记录表
    """

    #关联员工表数据，多对一 ；外键要定义在‘多’的一方
    person     = models.ForeignKey(Person,on_delete=models.CASCADE, verbose_name="员工")
    
    #绩效考察周期
    dateRange  = models.CharField(verbose_name ="考核周期", max_length=10, default="2018Q1", blank=True, null=True)
    
    #KPI的指标项
    KPIItem = models.CharField   (verbose_name ="考核项",   max_length=50, default="考核指标项内容")
    KPIScore= models.DecimalField(verbose_name="考核项得分", max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return ""

#骨干员工
class BackBone(models.Model):
    '骨干员工档案'

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE,verbose_name="姓名")
    #划分骨干的时间周期 例如：2018H1，2018H2，2019H1
    dateRange = models.CharField(verbose_name="骨干周期", max_length=10, default="2019H1")
    #骨干详细信息
    # 是否有房产
    ownHouse = models.BooleanField(verbose_name="是否有房产", default=False)
    # 房贷金额,大约列举
    houseDebt = models.CharField(verbose_name="房贷债务", max_length=20, default="房贷债务")
    # 是否分居两地
    diffArea = models.BooleanField(verbose_name="是否异地", default=False)
    # 是否有小孩
    hasChild = models.BooleanField(verbose_name="是否有小孩", default=False)
    # 小孩性别
    sexChild = models.CharField(verbose_name="小孩性别", max_length=10,  default="男孩")
    # 小孩年龄
    birthChild = models.CharField(verbose_name="小孩年龄", max_length=10,  default="出生日期")
    # 个人兴趣爱好
    hobby = models.CharField(verbose_name="个人兴趣爱好", max_length=30,  default="游戏、音乐，运动，看书，看电影")
    def __str__(self):
        return '骨干员工档案信息'
    
#骨干员工维护记录
class BackBoneOptRec(models.Model):
    '''
    骨干员工看护人责任维护记录，通过各种维护形式进行骨干维稳
    '''

    def __str__(self):
        return "骨干维护记录"





#员工考勤明细记录
class AttendanceDetail(models.Model):
    '''
    员工考勤明细表
    '''
    employee    = models.ForeignKey('Employee', on_delete=models.CASCADE)
    checkinTime = models.DateTimeField("打卡时间",auto_now=True)
    checkinArea = models.CharField(max_length=15, blank=False, null=False,default="") 

    def __str__(self):
        return "打卡明细记录"