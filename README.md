# 🚀 极简无后端静态博客系统 (Minimalist Serverless Blog)

这是一个基于 **GitHub Pages**、**GitHub API** 与 **Marked.js** 构建的**完全去中心化、无后端、极简且高安全级别**的个人博客系统。

系统不需要任何传统服务器、数据库或动态运行环境。所有的文章和数据都安全地托管在您的 GitHub 仓库中，通过前端直接与 GitHub API 进行安全握手，实现文章的动态检索、解析与零中介在线发布。

---

## ✨ 核心特性

1. **🛠️ 零传统后端，全静态托管**
   - 完美的 Serverless 架构，完全运行在浏览器端。
   - 完美适配 **GitHub Pages**、Vercel、Netlify 等静态文件托管平台，永久免费。

2. **🔒 高安全级别独立沙盒**
   - **独立纯原生安全设计**：发布管理端（`add.html`）**不依赖任何第三方 CDN 资产、外部脚本或统计追踪组件**，杜绝任何中间人攻击和跨站脚本漏洞。
   - **Token 内存安全驻留**：您的 GitHub Personal Access Token（个人访问令牌）仅留存在当前浏览器的运行内存中，**绝不上传至任何第三方服务器**。
   - **细粒度权限控制**：推荐配合 GitHub Fine-grained Tokens（细粒度令牌），仅对指定博客仓库授予 `Contents: Read and write` 最小权限。

3. **📝 浏览器端轻量级发布与全功能编辑器**
   - 内置高阶 Markdown 在线编辑器，提供流畅的创作环境。
   - 自定义文件名与 Commit Message，一键“安全传输”至云端仓库。
   - 自动处理**纯原生中文字符安全编码（UTF-8 & Base64 混合层）**，规避传统传输中可能出现的中文乱码问题。
   - 自动本地记住配置参数（用户名、仓库名、分支等，不包含 Token），下次创作开箱即用。

4. **⚡ 智能双轨路由与极致性能**
   - **动态实时同步（优先）**：首页与详情页优先调用 GitHub API，跨域动态抓取最新的文章列表与精准至秒级的 Git 提交推送时间（`git log` 级别）。
   - **静态本地兜底（降级方案）**：在 GitHub API 触发限流或网络抖动时，系统自动无缝降级读取由 Python 脚本生成的本地 `config.js` 路由文件，保障博客的高可用性。

5. **📊 现代前端数据流操控**
   - 支持多维数据过滤与交互，包括：**多规则排序切换**（按发布时间最新/最早、按文件名正序/倒序）和**自定义每页显示条数**。
   - 内置平滑翻页组件，长列表自动重置与视口定位优化。
   - 优雅的 `404 - 文章未找到` 路由防御机制。

6. **🎨 响应式美学视觉**
   - 首页基于 Tailwind CSS、详情页采用全定制精细化 `.prose` 样式渲染，提供极佳的排版与阅读体验。
   - 支持完美的移动端/响应式跨端适配，多平台文字渲染及代码高亮逻辑高度对齐。

---

## 📂 项目结构

```text
├── index.html          # 博客主入口（列表页与详情页双轨动态路由）
├── add.html            # 独立高安全级在线文章发布管理页面
├── config.js           # 自动生成的本地路由配置文件（API 失败时做数据兜底）
├── generate_list.py    # 本地自动化构建脚本（用于离线扫描生成 config.js）
└── posts/              # 存放 Markdown 文章源文件的目录 (*.md)
```

---

## ⚙️ 本地构建与自动化脚本 (`generate_list.py`)

为了配合系统的“智能双轨路由”，项目中自带了一个强大的 Python 3 构建工具。它会扫描 `posts/` 目录并抽离关键元数据，生成静态路由兜底。

### 脚本工作原理
1. **智能内容嗅探**：提取每个 Markdown 文件的首个一级标题（`# `）作为文章标题，并自动剥离 Markdown 格式化标记（粗体、链接、图片等），自动截取前 100 字作为智能摘要。
2. **高精准时间流获取**：由于硬盘文件系统（mtime）在 `git clone` 后的时间不准确，该脚本**优先通过调用 `git log` 解析文件的云端真实最后提交时间**。如遇非 Git 环境，则智能降级回退至本地硬盘修改时间。
3. **中文友好序列化**：输出的 `config.js` 采用原生非 ASCII 转义（`ensure_ascii=False`）编码，保留中文的高可读性。

### 脚本运行方法
```bash
# 使用默认配置直接运行
python3 generate_list.py

# 自定义博客全局参数并生成
python3 generate_list.py --title "我的技术博客" --owner "your-github-username" --repo "your-blog-repo" --branch "main"
```

---

## 🚀 快速上手与部署流程

### 第一步：创建或克隆仓库
在您的 GitHub 账户下建立一个新的公开（Public）或私有（Private）仓库，命名为例如 `my-blog`。

### 第二步：配置 GitHub Pages
进入仓库设置 `Settings` -> `Pages` -> `Build and deployment`，将 Source 选择为 `Deploy from a branch`，指定分支（如 `main`）和根目录 `/` 并保存。

### 第三步：获取最小权限 Token
1. 访问 GitHub `Settings` -> `Developer settings` -> `Personal access tokens` -> `Fine-grained tokens`。
2. 点击 **Generate new token**。
3. 在 **Repository access** 中选择 **"Only select repositories"** 并指定您的博客仓库。
4. 在 **Permissions** 列表中找到 **Contents**，将其设为 **Read and write**，生成并复制令牌。

### 第四步：开始创作与发布
1. 访问您托管好的或本地的 `add.html` 页面。
2. 填入您的 GitHub 账户名、仓库名、分支及刚才生成的 Token。
3. 在右侧使用 Markdown 尽情书写，赋予一个文件名（如 `hello-world.md`），点击**安全发布至仓库**。
4. 稍等片刻，访问 `index.html`，您的新文章已同步展现！

---

## 🛠️ 技术栈清单

- **HTML5 / CSS3** (CSS 变量控制、全原生网格与弹性盒布局)
- **Tailwind CSS** (用于主站界面的现代流式美化)
- **Marked.js** (客户端超轻量、高性能 Markdown 渲染器)
- **Python 3** (自动化元数据抽取与工程化构建脚本)
- **GitHub REST API v3** (完全去中心化数据交互桥梁)

---

## 🔒 隐私与安全声明

本系统设计之初就将安全放在首位。**发布端不存储、不中转、不共享您的任何个人令牌。** 所有数据和配置都严格限制在您信任的浏览器与 GitHub 官方服务器之间的私密链路内，是一套真正的私有化、去中心化的个人数据主权博客解决方案。
