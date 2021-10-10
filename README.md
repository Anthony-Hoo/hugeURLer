# hugeURLer

hugeURLer是一个基于python的serverless短链接服务

### 如何使用

您需要把库clone到本地，然后在终端执行`python3 .\src\addNewRedirection.py  <url>` ，就能创建一个指向你设置的url的跳转页面。

随后，您只需要pr到本仓库，在我们merge后，您就能通过这个短链接来访问您设置的url了。

### 如何实现的

我们通过`redirectionConfig.csv`来记录需要跳转的url与短链接的对应关系，再通过`src/pageGen.py`来生成跳转页面到`pages/`。

在仓库push到GitHub上时，在`.github/workflows/`设置好的action就会执行，生成跳转页面并部署到GitHub page上。这时大家就能够访问跳转了。

### 未来计划

- [ ] 美化跳转页面、
- [ ] 美化主页

### 最后

欢迎大家来用，欢迎pr功能。