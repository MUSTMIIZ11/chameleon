#  Chameleon: Course Project of MIIZ11 Software Engineering 

### Owner: Lulin Deng, Kan Ni, Zhiyao Xie 

***
It is a website of create your own character graph in books. Currently under active development...

TODO LIST:

### Welcome page 

Button

- [ ] Logo: 主页上的logo跳转主页(index.html)

- [ ] community: 主页community主页跳转到community.html

- [ ] tools: tools按钮跳转login.html

- [ ] bookshelf: 跳转顺序：bookshelf.html->login.html->bookshelf.html

- [ ] get start: 跳转顺序：login.html —> community.html 


### Login page

Button

- [ ] Sign in：数据库记录三条登陆信息

- [ ] Forget password：不能忘记密码（不是


### Community page

Button

- [ ] Logo: 跳转到index.html

- [ ] community: 跳转到community.html

- [ ] tools: 跳转顺序：login.html —> tools.thml

- [ ] bookshelf: 跳转顺序login.html —> bookshelf.html 


### Tools page

- [ ] upload botton: 点击upload，作品发布到社区

- [ ] save: 点击save，存到本地

- [ ] share：点击share，生成二维码，扫码可以下载到手机(方便pre的时候show一下

### Bookshelf page

- [ ] 时间不够这个page就删了吧要不... wait for version 2.0

### How to develop 进行本地开发
```shell
# 1.安装项目依赖
# cd到chameleon项目下
python -m pip install -r requirements
# 启动服务，端口8080
python manage.py runserver 8080

# 如果有新的app创建，并且要更新数据库，这时候需要执行下面的命令
python manage.py migrate

```

### Useful commands 好用的命令
```shell
python manage.py startapp xxx  # 创建一个app 名字叫"xxx"
python manage.py runserver 8080  # 运行服务

python manage.py startapp tools  # 创建tools app,会在项目根目录下面创建tools目录

```