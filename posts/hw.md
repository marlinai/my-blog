# 你好，世界 文件名缩写！

这是我的第一篇个人博客文章。它完全运行在 **GitHub Pages** 上，没有借用任何传统的后端服务器。

## 为什么选择这个方案？

- **零成本**：白嫖 GitHub 的静态托管服务
- **极简**：没有复杂的静态网站生成器，写完 Markdown 挂上就能读
- **自动化**：一条 `python3 generate_list.py` 命令即可更新文章列表

## 技术栈

| 层级 | 技术 |
|------|------|
| 托管 | GitHub Pages |
| 样式 | Tailwind CSS v4 |
| 解析 | Marked.js |
| 路由 | 原生 JavaScript + URLSearchParams |
| 排版 | 手写 prose 样式 |

## 写文章的流程

1. 在 `posts/` 下创建一个 `.md` 文件，比如 `my-post.md`
2. 用 Markdown 语法写内容
3. 终端运行：

```bash
python3 generate_list.py
```

4. 刷新浏览器，新文章就出现在首页了

> **提示**：Python 脚本会自动提取文章标题（首个 `#` 行）、摘要和最后修改时间，并更新 `config.js`。

## Markdown 语法测试场

下面展示这套博客系统支持的各种排版效果。

### 文本样式

**加粗文字**、*斜体文字*、~~删除线~~、`行内代码`

### 列表

有序列表：

1. 第一项
2. 第二项
3. 第三项

无序列表：

- 苹果
- 香蕉
  - 嵌套项
  - 另一个嵌套项
- 橙子

### 引用

> 好的代码本身就是最好的文档。
> —— 某位不知名的程序员

### 代码块

```javascript
// 这是 JavaScript 代码块
function greet(name) {
    return `你好，${name}！`;
}

console.log(greet('世界'));
```

```css
/* CSS 代码块 */
.container {
    max-width: 48rem;
    margin: 0 auto;
}
```

### 链接与图片

- [GitHub Pages 文档](https://docs.github.com/pages)
- [Marked.js 文档](https://marked.js.org/)

### 分割线

---

感谢阅读！后续会分享更多内容。
