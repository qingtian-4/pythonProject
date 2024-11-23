### git常用命令行

```
mkdir # 用来创建新目录；
pwd   # 用来显示当前的目录
```

```
git init # 把当前目录变成Git可以管理的仓库：
```

```
git add filename # 把文件添加到版本库；
```

```
git commit -m "explanations" # 把文件提交到仓库；
```

**命令执行成功后会提示：**

1. __file changed__：1个文件被改动（新添加的文件）；

2. __insertions__：插入了两行内容（文件有多少行内容）

>为什么Git添加文件需要`add`，`commit`一共两步呢？因为`commit`可以一次提交很多文件，所以可以多次`add`不同的文件

```
git status # 查看仓库当前的状态，可以看出文件是否被修改
```

__如果出现`Changes not staged for commit`：表示文件被修改过了，但还没有准备提交（还没git add和git commit）__

__如果出现`Changes to be committed`：表示要提交的修改包括列出来的（还没git commit）__

__如果出现`nothing to commit`：表示没有需要提交的修改__

```
git diff   # 查看具体修改的内容
```

```
git log                  # 查看历史记录，显示从最近到最远的提交日志
git log --pretty=oneline # 简洁的显示历史记录
```

```
git reset --hard HEAD^ # 回退到上一个版本
```

`--hard`会回退到上个版本的已提交状态，而`--soft`会回退到上个版本的未提交状态，`--mixed`会回退到上个版本已添加但未提交的状态；`HEAD`表示当前版本，`HEAD^`表示上一个版本，`HEAD^^`表示上上一个版本，如果回退比较多的话，可以用`HEAD~100`表示往上100个版本

#### 关联远程库

1、要关联一个远程库，使用命令`git remote add origin git@server-name:path/repo-name.git`_

2、关联一个远程库时必须给远程库指定一个名字，`origin`是默认习惯命名；

3、关联后，使用命令`git push -u origin master`第一次推送`master`分支的所有内容；

4、此后，每次本地提交后，只要有必要，就可以使用命令`git push origin master`推送最新修改；

5、先用`git remote -v`查看远程库信息，再用`git remote rm <name>`命令可以删除远程库

#### 总结流程如下：

1、`git init`
__把这个文件夹变成Git可管理的仓库。__

2、`git add`
__把该目录下的所有文件添加到仓库__

3、`git commit -m "first commit"`
__把项目提交到仓库。__

4、`git remote add origin ...`
__(将本地仓库与GitHub上创建好的目标远程仓库进行关联。 …后面加的是GitHub目标仓库地址)。__

5、`git push -u origin master`
__把本地库的所有内容推送到GitHub远程仓库上。__



#### 分支管理

```
git checkout -b dev # 创建dev分支，然后切换到dev分支
```

相当于以下两条命令

```plain
git branch dev     # 创建dev分支
git checkout dev   # 切换到dev分支
```

__单独的用`git branch`命令会列出所有分支，当前分支前面会标一个`*`号__

```
git merge          # 用于合并指定分支到当前分支
```

