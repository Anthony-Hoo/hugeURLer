# hugeURLer
[Read This in English](#hugeurler-en)

hugeURLer 是一个基于 Python 和 Vercel 的短链接服务  


### 如何使用

#### 如果您没有本仓库的 push 权限

请将本仓库 clone 到本地，然后在终端执行 `python3 .\src\addNewRedirection.py  <url>` ，就能创建一个指向你设置的 url 的跳转页面。

随后，您只需要 pr 到本仓库，在我们 merge 后，您就能通过这个短链接来访问您设置的 url 。

#### 如果您有本仓库的 push 权限

直接在线修改 `redirectionConfig.csv` 来设置跳转记录并提交即可。

### 如何实现的

通过 `redirectionConfig.csv` 来记录需要跳转的 url 与短链接的对应关系，再由 Vercel 通过执行 `src/main.py` 来填充页面模板，以生成跳转页面到 `pages/` 。

当访问设置的跳转路径时，页面将在 3 秒内通过 JavaScript 重定向到设置的 URL, 请允许本网站执行 JS 以完成重定向。

### 惊喜

如果您的设备对 HDR 支持良好，且正确启用了相关特性，在访问我们的主页( [s.csu.st](https://s.csu.st) ) 或任意跳转链接时，您可以在视频中看到一些有趣的效果。

### 未来计划

- [x] 美化跳转页面
- [x] 美化主页
- [ ] 更便捷地增加新跳转纪录

### 最后

欢迎大家来用，欢迎 pr 功能。

---

# hugeURLer-en

hugeURLer is a short URL service based on Python and Vercel  

### How to Use

#### If you do not have push access to this repository

Clone this repository to your local machine, then execute `python3 .\src\addNewRedirection.py <url>` in the terminal to create a redirection page pointing to the URL you set.

Afterward, you only need to submit a pull request (PR) to this repository. Once we merge it, you can access your desired URL using the short link.

#### If you have push access to this repository

Simply edit the `redirectionConfig.csv` file online to set up redirection records and commit your changes.

### How It Works

The `redirectionConfig.csv` file records the mapping between short links and the URLs they redirect to. Vercel executes `src/main.py` to populate the page template and generates redirection pages in the `pages/` directory.

When visiting a configured redirection path, the page will redirect to the set URL within 3 seconds using JavaScript. Please allow this site to execute JavaScript to complete the redirection.

### Surprise
If your device supports HDR well and the related features are correctly enabled, you may notice some interesting effects in the video when visiting our homepage ( [s.csu.st](https://s.csu.st) ) or any of the short links.

### Future Plans

- [x] Beautify the redirection page
- [x] Beautify the homepage
- [ ] Provide an easier way to add new redirection records

### Final Notes

Everyone is welcome to use this project and contribute features via pull requests.
