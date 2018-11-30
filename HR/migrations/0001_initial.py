# Generated by Django 2.0.5 on 2018-11-29 14:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('CORE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateLeave', models.DateField(default=datetime.date.today, verbose_name='离职时间')),
                ('classLeave', models.CharField(choices=[('0', '主动离职'), ('1', '淘汰'), ('2', '辞退')], default='0', max_length=1, verbose_name='离职类型')),
                ('reasonLeave', models.CharField(max_length=50, verbose_name='离职原因')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='姓名')),
                ('workNo', models.CharField(default='B-12345', max_length=15, verbose_name='公司工号')),
                ('workNoExt', models.CharField(max_length=15, null=True, verbose_name='华为工号')),
                ('mobilePhone', models.CharField(default='18600000000', max_length=11, verbose_name='手机号码')),
                ('IDNo', models.CharField(max_length=18, verbose_name='身份证')),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='电子邮箱')),
                ('email2', models.EmailField(max_length=50, null=True, verbose_name='华为邮箱')),
                ('sex', models.CharField(choices=[('0', '女'), ('1', '男')], default='1', max_length=1, verbose_name='性别')),
                ('level', models.CharField(choices=[('00', '00'), ('1B', '1B'), ('1A', '1A'), ('2B', '2B'), ('2A', '2A'), ('3B', '3B'), ('3A', '3A'), ('4B', '4B'), ('4A', '4A'), ('5B', '5B'), ('5A', '5A'), ('6B', '6B'), ('6A', '6A'), ('7B', '7B'), ('7A', '7A'), ('8B', '8B'), ('8A', '8A'), ('9B', '9B'), ('9A', '9A'), ('10B', '10B'), ('10A', '10A'), ('11B', '11B'), ('11A', '11A'), ('12B', '12B'), ('12A', '12A')], default='4A', max_length=4, verbose_name='岗位级别')),
                ('entryDate', models.DateField(default=datetime.date.today, verbose_name='入职日期')),
                ('productUnit', models.CharField(default='0', max_length=10, null=True, verbose_name='产品线')),
                ('provinceBirth', models.CharField(default='江苏省', max_length=20, null=True, verbose_name='籍贯省份')),
                ('cityBirth', models.CharField(default='南京市', max_length=20, null=True, verbose_name='籍贯市')),
                ('birthDay', models.DateField(default=datetime.date.today, null=True, verbose_name='出生日期')),
                ('maritalStatus', models.CharField(choices=[('0', '未婚'), ('1', '已婚'), ('2', '离异')], default='0', max_length=1, verbose_name='婚姻状况')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='住址')),
                ('graduatedSchool', models.CharField(default='大学', max_length=20, null=True, verbose_name='毕业学校')),
                ('education', models.CharField(choices=[('0', '小学'), ('1', '初中'), ('2', '高中'), ('3', '大专'), ('4', '本科'), ('5', '研究生')], default='4', max_length=1, null=True, verbose_name='学历')),
                ('profession', models.CharField(default='', max_length=20, null=True, verbose_name='专业')),
                ('graduatedDay', models.DateField(default=datetime.date.today, null=True, verbose_name='毕业日期')),
                ('workStatus', models.CharField(choices=[('00', '在职'), ('11', '请假'), ('99', '离职')], default='00', max_length=5, verbose_name='工作状态')),
                ('depart', models.ForeignKey(db_column='depart', limit_choices_to={'level': 3}, on_delete=django.db.models.deletion.CASCADE, to='CORE.Organization', verbose_name='部门')),
            ],
            options={
                'ordering': ['-entryDate'],
            },
        ),
        migrations.CreateModel(
            name='Performace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRange', models.CharField(default='2018Q1', max_length=10, verbose_name='考核周期')),
                ('total', models.IntegerField(default=0, verbose_name='绩效得分')),
                ('result', models.CharField(blank=True, max_length=10, null=True, verbose_name='绩效结果')),
                ('appraisers', models.CharField(blank=True, max_length=10, null=True, verbose_name='考评人')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.Employee', verbose_name='员工')),
            ],
        ),
        migrations.CreateModel(
            name='PerformaceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRange', models.CharField(blank=True, default='2018Q1', max_length=10, null=True, verbose_name='考核周期')),
                ('KPIItem', models.CharField(default='考核指标项内容', max_length=50, verbose_name='考核项')),
                ('KPIScore', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='考核项得分')),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.Employee', verbose_name='员工')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applyDate', models.DateField(default=datetime.date.today, verbose_name='生效月份')),
                ('adjustRange', models.IntegerField(default=0, verbose_name='调薪幅度')),
                ('salaryFinal', models.IntegerField(default=0, verbose_name='调整后薪资')),
                ('adjustDate', models.DateField(default=datetime.date.today, verbose_name='调薪日期')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.Employee', verbose_name='员工')),
            ],
        ),
        migrations.AddField(
            model_name='demission',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.Employee', verbose_name='离职员工姓名'),
        ),
    ]
