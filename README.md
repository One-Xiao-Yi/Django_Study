# Django_part1  
Django-配置、连接数  
使用Pycharm开发  
### 1.新建Django项目  
### 2.打开设置，在peoject->Interpreter添加包PyMySQL（python3）、mysqlclient  
### 3.在init.py编写代码 

    import pymysql  
	pymysql.install_as_MySQLdb()   

### 4.settings.py修改数据库连接相关配置

	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.sqlite3',
        	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    	}
	}
	
### 5.创建模块，点击菜单栏的TOOLS->run manage.py Task,在下方命令行中输入 startapp part1(你想取的项目名称)
### 6.在settings.py中加入你的模块

	INSTALLED_APPS = [
    	'django.contrib.admin',
    	'django.contrib.auth',
    	'django.contrib.contenttypes',
    	'django.contrib.sessions',
    	'django.contrib.messages',
    	'django.contrib.staticfiles',
	]
	
### 7.打开part1下的views.py，编写hello代码
	from django.http import HttpResponse


	def hello(request):
    	return HttpResponse("Hello Django")

### 8.将该方法加入到url中，打开urls.py，在urlpatterns中加入你写的方法
首先导入该方法

	from part1.views import hello
在列表中加入该方法映射地址

	path('index/',hello),（方法后不要带括号）
	
### 9.点击运行，可能会遇到两个问题  
1）mysqlclient版本问题，在提示的base.py文件中，注释掉这两句

	#if version < (1, 3, 13):
	#    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
2）'str' object has no attribute 'decode' ，在提示的operations,py文件中，修改该行代码
	
	query = query.decode(errors='replace')#修改前
	query = query.encode(errors='replace')#修改后
### 10.遇到问题并修改过后，点击下方输出的网址，打开浏览器后，在端口后方加入在url中填写的映射地址，即

	http://127.0.0.1:8000/index/
	
### 11.环境搭建完成之后，开始连接数据库操作。继续在run manage.py Task中输入inspectdb，将根据数据库中的表生成model，将生成的文件复制到models.py中

### 12.在views.py文件中，完成对数据库数据的提取。先导入models文件中的类，通过以下代码提取数据库中的数据

	# 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1) 
    
    # 获取单个对象
    response3 = Test.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
    # 数据库操作
	
	def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>修改成功</p>")
	
	def testdb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")
	
### 完成搭建和对数据库的访问
