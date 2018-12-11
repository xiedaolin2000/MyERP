from openpyxl import load_workbook


def import_Excel(srcFile):
    # wb = load_workbook(r"E:\OneDrive\Work\billjc\区域研发中心\人力资源\在职&离职名单\南京在职&amp;离职名单--2018.5.11.xlsx",data_only=True)
    wb = load_workbook(srcFile, data_only=True)
    sht = wb["人员信息"]
    # colIDX_SRC=["A","B"]
    # colIDX_DES=["A","B"]
    # 花名册Excel表格中，列名称对应的数据库字段属性，key是列名，value是字段属性
    colIDX_Fields_Mapping = {
        "A":"id",
        "B":"workNo",
        "C":"workNoExt",
        "D":"userName", #姓名
        "E":"IDNo", #身份证
        "F":"sex", #性别字段
        "G":"level", #性别字段
        "H":"productUnit", #产品线
        "J":"projectName", #项目组
        "L":"role", #员工角色
        "N":"mobilePhone", #手机号
        "O":"majorSkill", #手机号
        "P":"entryDate", # 到岗日期/入职日期
        "Q":"birthDay",# 出生日期
        "R":"graduatedDay", # 毕业时间
        "S":"graduatedSchool", #毕业院校
        "T":"schoolType", #毕业院校类型211/985
        "U":"education", #学历
        "V":"profession",  # 大学专业名称
        "W":"provinceBirth", #籍贯省
        "X":"cityBirth", #籍贯市
        "Y":"maritalStatus",
        "Z":"emailExt", #华为邮箱
        "AA":"email",  #佰钧成邮箱  
        "AB":"workStatus",  #佰钧成邮箱          
        "AC":"address", #居住地址
        }
    usedRowCount = sht.max_row
    # usedRowCount = 10
    #数据从第二行开始读取，第一行是标题
    # for row in range(2,usedRowCount):
    #     p = Employee()
    #     for colName,fieldName  in colIDX_Fields_Mapping.items():
    #         print(colName,fieldName)
    #         #动态设置对象的属性值
    #         p.__setattr__ (fieldName, sht["%s%i" % (colName,row)].value)
    #         # pars[fieldName]=sht["%s%i" % (colName,row)].value
    #     p.save()
    #生成SQL语句
    #数据从第二行开始读取，第一行是标题
    for row in range(2,usedRowCount):        
        fieldSQL = ""
        vlsSQL = ""
        for colName,fieldName  in colIDX_Fields_Mapping.items():
            fieldSQL = fieldSQL +" "+ fieldName
            print(sht["%s%i" % (colName,row)].value)
            vlsSQL   = vlsSQL +" "+ str( sht["%s%i" % (colName,row)].value)
        insSQL = "row=%i=>INSERT INTO HR_employee (%s) values(%s)"%(row,fieldSQL, vlsSQL)
        print(insSQL)


def initData(*args):
    """初始化数据"""

def main(*args,**kwargs):
    print("run here")
    import_Excel(r"E:\Workspace\MyERP\testdata.xlsx")


if __name__ == "__main__":
    main()
