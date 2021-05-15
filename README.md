#  Chameleon: Course Project of MIIZ11 Software Engineering 

### Owner: Lulin Deng, Kan Ni, Zhiyao Xie 
![example workflow](https://github.com/MUSTMIIZ11/chameleon/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/MUSTMIIZ11/chameleon/branch/main/graph/badge.svg?token=9X73F77MZF)](https://codecov.io/gh/MUSTMIIZ11/chameleon)
***
It is a website of create your own character graph in books. Currently under active development...

### !!!  Notice to the developers !!! : 
Please commit changes to your own branch, and pull request.

Do not directly commit to the main branch.

TODO LIST:

### Welcome page 

Button

- [x] Logo: 主页上的logo跳转主页(index.html)

- [x] community: 主页community主页跳转到community.html

- [x] tools: tools按钮跳转login.html

- [ ] bookshelf: 跳转顺序：bookshelf.html->login.html->bookshelf.html

- [x] get start: 跳转顺序：login.html —> community.html 


### Login page

Button

- [x] Sign in：数据库记录三条登陆信息

- [x] Sign up:注册


### Community page

Button

- [x] Logo: 跳转到index.html

- [x] community: 跳转到community.html

- [x] tools: 跳转顺序：login.html —> tools.thml

- [ ] bookshelf: 跳转顺序login.html —> bookshelf.html 


### Tools page

- [ ] upload botton: 点击upload，作品发布到社区

- [x] save: 点击save，存到本地

- [ ] share：点击share，生成二维码，扫码可以下载到手机(方便pre的时候show一下

### Bookshelf page

- [ ] 时间不够这个page就删了吧要不... wait for version 2.0

### How to develop 进行本地开发
```shell
# 1.安装项目依赖
# cd到chameleon项目下
python -m pip install -r requirements
# 运行服务
# export DJANGO_ENV=devlopment 设置了环境变量,通过该环境变量，我们的配置使用了远程mysql数据库
export DJANGO_ENV=devlopment && python manage.py runserver 8080

# export DJANGO_ENV="" 将DJANGO_ENV置空，通过该环境变量，配置使用本地sqlite
export DJANGO_ENV="" && python manage.py runserver 8080

# 如果有新的app创建，并且要更新数据库，这时候需要执行下面的命令
python manage.py migrate

# 进行单元测试 Unit test command
export DJANGO_ENV="test" && python ./manage.py test
export DJANGO_ENV="test" && python ./manage.py test tools

# Converage test command
export DJANGO_ENV="test" && coverage run --source='.' manage.py test&& coverage xml
# 本地查看coverage报告的命令
coverage report -m
```

### Useful commands 
```shell
python manage.py startapp xxx  # 创建一个app 名字叫"xxx"


# 创建tools app,会在项目根目录下面创建tools目录
python manage.py startapp tools

# 如果有新的app创建，并且要更新数据库，这时候需要执行下面的命令
python manage.py migrate

管理员界面：http://127.0.0.1:8080/admin/   账号admin 密码admin

Project Online Address: http://159.75.82.228:9090/
JENKINS: http://159.75.82.228:8080/job/chameleon/

# docker commands
# docker run --name mysql -v mysql-volume:/var/lib/mysql -e MYSQL_DATABASE=chameleon_db_dev -e MYSQL_ROOT_PASSWORD=chameleon -p 3306:3306 -d mysql
# sudo docker run --name  "$RUN_NAME" -v /home/ubuntu/img/img:/code/chameleon/static/map_img  -p 9090:9090 -d"$CONTAINER"

```


### Database Design

#### User

| 列名       | 类型         | KEY  | 可否为空 | 注释     |
| ---------- | ------------ | ---- | -------- | -------- |
| id      | int   | PRIMARY KEY  | 否       | 自增主键ID   |
| username       | char(128)    |      | 否       | 用户名     |
| password      | varchar(255) |      | 否      | 密码     |
| createtime | datetime     |      | 是       | 创建时间 |


#### Map

| 列名       | 类型         | KEY  | 可否为空 | 注释     |
| ---------- | ------------ | ---- | -------- | -------- |
| id      |int   | PRI  | 否       | 自增主键ID   |
| map_name       | char(128)    |      | 否       | 图谱名称     |
| map_url       | text    |      | 否       | 图谱链接     |
| user_id      | int |      | 是       | 图谱所属的用户ID     
| like | int |    | 否 | 图谱获得的点赞数
| createtime | datetime     |      | 是       | 创建时间 |

### TroubleShooting
```shell
遇到数据库表冲突的问题解决方案：
mysql -uroot -p -h 159.75.82.228
#password: chameleon
DELETE FROM django_migrations WHERE app = 'community'
DROP table communicy;
python manage.py makemigrations
python manage.py migrate;
```


### Project Workflow


New Branch(Feature/BugFix/Main) -> Code Review(Pull Requests) -> Continuous Integration(Github Actions) -> Continuous Deployment(Github webook + Jenkins)

### Load Test
https://github.com/nikan1996/Webenchmark is similar to Apache Benchmark , use it to make a test
