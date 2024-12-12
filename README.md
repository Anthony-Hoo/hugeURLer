# hugeURLer

hugeURLer 是一个基于 Python 和 GitHub action 的短链接服务

### 如何使用

将本仓库 clone 到本地，然后在终端执行 `python3 .\src\addNewRedirection.py  <url>` ，就能创建一个指向你设置的 url 的跳转页面。

随后，您只需要 pr 到本仓库，在我们 merge 后，您就能通过这个短链接来访问您设置的 url 。

### 如何实现的

通过 `redirectionConfig.csv` 来记录需要跳转的 url 与短链接的对应关系，再通过 `src/pageGen.py` 来生成跳转页面到 `pages/` 。

# 现在已经换成了 Vercel
# 现在已经换成了 Vercel
# 现在已经换成了 Vercel

~~在仓库 push 到 GitHub 上时，在 `.github/workflows/` 设置好的 action 会执行，生成跳转页面并部署到 GitHub page 上。这时大家将能够访问跳转。~~


### 未来计划

- [x] 美化跳转页面
- [x] 美化主页
- [ ] **都tmd换成 Vercel 了还搁这 GitHub Pages 呢啊？？？**
- [ ] **把那逼 HDR 视频换一下啊**
- [ ] 更便捷地增加新跳转纪录

### 最后

欢迎大家来用，欢迎 pr 功能。
