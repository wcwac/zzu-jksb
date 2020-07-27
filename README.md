# zzu-jksb

使用 GitHub Actions 每日自动完成zzu疫情情况打卡

## 使用说明

Fork 本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加三个Secrets环境变量，前者在 Name 中填写，后者在 Value 中填写，冒号不需要填写

* username ：你的用户名

* password ：你的密码

* api ：你的server酱api密钥(登录http://sc.ftqq.com/ 并绑定微信可获取)

最后在你的仓库内随便改点什么（比如给 README 文件删掉或者增加几个字符，行尾加空格不算）提交一下就可以手动触发一次 Github Actions ，以后每天的00:15和05:15都会自动完成打卡(该时间可修改yml文件进行配置)

在 Actions 处可以看到打卡情况，假如发生错误会看到详情。
