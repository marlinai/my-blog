# 极简个人博客 — GitHub Pages 版

一个完全托管在 GitHub Pages 上的极简个人博客系统。

**零后端、零构建工具、零成本。** 只用 HTML + CSS (Tailwind) + 原生 JavaScript，配合一个 Python 脚本完成自动化。

## 特性

- 📝 **Markdown 写作** — 在 `posts/` 下创建 `.md` 文件即可写文章
- ⚡ **浏览器端解析** — 使用 Marked.js 动态渲染，无需预构建
- 🤖 **自动路由表** — `python3 generate_list.py` 一键扫描文章并更新配置
- 🎨 **极简排版** — 手写 `prose` 样式，代码块深色主题，响应式布局
- 🚀 **零成本部署** — 推送到 GitHub 即可上线

## 项目结构

```
my-blog/
├── index.html          # 主页面（路由 + 渲染 + 样式）
├── config.js           # 文章路由表（由脚本自动生成）
├── generate_list.py    # Python 脚本：扫描 posts/ 自动更新 config.js
├── README.md           # 本文件
└── posts/              # 存放 Markdown 文章的文件夹
    ├── hello-world.md  # 示例文章
    └── css-tips.md     # CSS 技巧文章
```

## 🖥 本地运行

### 为什么不能直接双击 HTML？

因为 `index.html` 通过 `fetch('./posts/xxx.md')` 加载 Markdown 文件，而浏览器出于安全策略，不允许 `file://` 协议发起跨域请求（CORS）。所以需要一个本地 HTTP 服务器。

### 启动本地服务

```bash
# 进入项目目录
cd my-blog

# Python 启动简易 HTTP 服务
python3 -m http.server 8080
```

然后浏览器访问 **http://localhost:8080** 即可。

> 用 `Ctrl+C` 停止服务。

## ✍️ 写新文章

1. 在 `posts/` 下创建 `.md` 文件，例如 `my-post.md`
2. 第一行用 `# 标题` 作为文章标题（脚本会自动提取）
3. 写内容
4. 终端运行：

```bash
python3 generate_list.py
```

5. 刷新浏览器，新文章就出现在首页了

### 自定义博客标题

```bash
python3 generate_list.py --title "我的技术博客"
```

## 🚀 GitHub Pages 部署

1. 在 GitHub 新建一个仓库（例如 `my-blog`）
2. 推送项目到仓库：

```bash
git init
git add .
git commit -m "初始化博客"
git branch -M main
git remote add origin https://github.com/你的用户名/my-blog.git
git push -u origin main
```

3. 进入仓库 → **Settings** → **Pages**
4. **Source** 选择 `Deploy from a branch`，Branch 选 `main`，文件夹选 `/ (root)`
5. 点击 **Save**，等待 1-2 分钟
6. 访问 `https://你的用户名.github.io/my-blog/` 即可看到博客

## 🛠 技术栈

| 组件 | 技术 |
|------|------|
| 托管 | GitHub Pages |
| 样式 | Tailwind CSS v4 (CDN) |
| Markdown 解析 | Marked.js (CDN) |
| 前端路由 | URLSearchParams |
| 文章索引 | Python 自动扫描 |

## 许可

MIT
