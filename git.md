# git
## 参考资料
* http://www.jianshu.com/p/86dfc616de68
* http://www.jianshu.com/p/482b32716bbe
* https://git-scm.com/book/zh/v2
* http://res.crossincode.com/wechat/git.html

## 安装
* [Git的官方安装包](http://git-scm.com/download)

* 检查Git版本
```
git --version
```
* 创建用户标识
```
git config --global user.name “xxx”    //用户名
git config --global user.email “xx@xxx”    //邮箱   
git config --global color.ui “auto”    //界面偏好
```

* Git仓库
```
    git init    //创建一个包含所有元数据和仓库变更历史的.git隐藏目录
    git status    //检查当前目录下文件的状态
```

* 查看log时中文乱码

在Bash提示符下输入：

	git config --global i18n.commitencoding utf-8
	git config --global i18n.logoutputencoding gbk


## 操作
* 文件跟踪
```
git add .    //跟踪并记录当前目录下所有文件变化
git add index.html    //添加指定文件到暂存区
git add javascript/    //添加指定文件夹到暂存区
git add *.js    //通过通配符，添加一组文件到暂存区
git add -i    //以交互方式添加文件
git add -p    //只提交部分修改的内容
git commit –m “xxx”    //提交当前目录下的所有内容，并备注提交说明
git commit –-amend    //修改上一次提交的说明
```
* 本地文件操作
```
git mv originalfile.txt newsubdir/newfilename.txt    //移动文件
git rm filetoremove.txt    //将文件标识为删除状态，下一次提交时确认删除

git diff    //查看当前工作树与暂存区的差别，如果暂存区是空的，那么它将显示工作树与最新提交状态之间的差别
git diff --staged    //
git diff HEAD    //

git reset    //回滚到最后一次提交后的状态
git reset --hard    //循环地将所有未提交或未被放入暂存区的文件进行回滚
git checkout modifiedfile.txt    //只回滚某一个文件
```

* 远程交互
```
git remote -v 	//查看关联的远程主机及权限
git push <远程主机名称> <本地主机名称> 	//将本地文件提交至远程
```

## github操作
* 将制定地址的文件克隆到本地
```
git clone git@github.com:xxxx.git
```
