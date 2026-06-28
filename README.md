# 极简个人博客

一个完全托管在 **GitHub Pages** 上的极简博客系统。

**零后端、零构建工具、零成本。** 纯 HTML + Tailwind CSS + 原生 JavaScript，GitHub Actions 全自动维护文章索引。

## 它怎么工作

1. 你往 `posts/` 里扔一个 `.md` 文件，`git push`
2. GitHub Actions 自动扫描所有文章，提取标题/日期/摘要，更新 `config.js`
3. 前端首页通过 GitHub API 实时拉取文章列表（API 失败则回退到 `config.js` 兜底）
4. 浏览器端用 **Marked.js** 把 Markdown 渲染成 HTML

## 特性

- 📝 **纯 Markdown 写作** — 文章就是 `.md` 文件，用任何编辑器写都行
- ⚡ **零步发布** — `git push` 完成，无需手动运行脚本
- 🤖 **GitHub Actions 自动化** — 推送时自动扫描文章、更新索引
- 🔄 **GitHub API 实时列表** — 首页从 API 动态拉取，文章即推即现
- 🛡️ **config.js 兜底** — API 限流时自动降级，首页不会白屏
- 🎨 **极简排版** — 手写 prose 样式，深色代码块，响应式布局
- 🌐 **SPA 路由** — `?post=filename.md` 即可直达文章
- 📱 **响应式** — 手机/平板/桌面都好读

## 项目结构

```
my-blog/
├── index.html                          # 主页（路由 + 渲染 + 全套样式）
├── config.js                           # 配置文件（由 GitHub Actions 自动更新）
├── generate_list.py                    # Python 脚本（本地 & Actions 共用）
├── README.md
├── .github/workflows/update-config.yml # GitHub Actions 工作流
└── posts/                              # 文章目录
    ├── hello-world.md
    ├── css-tips.md
    └── ...
```

## 本地运行

浏览器不能直接用 `file://` 打开——`fetch()` 会被 CORS 拦截。

```bash
cd my-blog
python3 -m http.server 8080
```

然后访问 **http://localhost:8080**。

## 发布文章

```bash
# 1. 在 posts/ 下写一篇文章，首行 # 标题
echo "# 我的新文章" > posts/my-post.md

# 2. 推送
git add posts/my-post.md
git commit -m "新文章"
git push
```

GitHub Actions 会在几秒内自动运行 `generate_list.py` 并更新 `config.js`，无需手动操作。

> 如果需要在本地预览首页效果，可以手动运行 `python3 generate_list.py` 更新 `config.js`。

## 配置说明

编辑 `config.js` 顶部的几个字段即可适配你自己的仓库：

```js
title: "我的极简个人博客",  // 博客名称
owner: "你的GitHub用户名",    // GitHub 用户名
repo:   "my-blog",          // 仓库名
branch: "main",             // 分支名
```

> 使用 `generate_list.py --owner xxx --repo xxx` 可以在生成时覆写这些值。

## 部署到 GitHub Pages

1. GitHub 仓库 → **Settings** → **Pages**
2. **Source**: `Deploy from a branch` → 选 `main` 分支，根目录 `/ (root)`
3. 保存，两分钟后访问 `https://你的用户名.github.io/仓库名/`

## 技术栈

| 组件 | 技术 |
|------|------|
| 托管 | GitHub Pages |
| 样式 | Tailwind CSS v4 (CDN) |
| Markdown 解析 | Marked.js (CDN) |
| 前端路由 | URLSearchParams |
| 文章索引 | GitHub API + GitHub Actions 自动扫描 |
| 兜底 | config.js 静态路由表 |
