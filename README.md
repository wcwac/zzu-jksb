# 2021/01/13

# 学校加入了ip记录，暂无有效解决措施

# 本库停更




## 教程地址：https://wcac.art/posts/jksb/ ##

请仔细阅读教程及以下提示后再进行操作

建议Watch本项目以获取更新提示



### 关于Github Actions自动停用
 根据 https://docs.github.com/cn/free-pro-team@latest/actions/managing-workflow-runs/disabling-and-enabling-a-workflow 所述：

>警告： 为防止不必要的工作流程运行，可能会自动禁用计划的工作流程。 在复刻公共仓库时，默认情况下将禁用计划的工作流程。 在公共仓库中，当 60 天内未发生仓库活动时，将自动禁用计划的工作流程。

所以尽量每隔两个月上线对仓库进行修改避免自动停用GitHub Actions。

如果已经被停用可在**自己的仓库**选择Actions->jksb->enable重新启用。



### 自动同步主分支最新的代码
将仓库与主分支保持一致（也可选择删除仓库重新fork（推荐这样做）），务必确保存在/.github/pull.yml文件，内容同主分支相同。

安装[pull插件][1]，选择**Only select repositories**并将此项目加入。

  [1]: https://github.com/apps/pull
