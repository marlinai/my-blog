#!/usr/bin/env python3
"""
generate_list.py — 自动扫描 posts/ 目录下的 .md 文件，
提取标题、日期和摘要，生成 config.js 路由配置文件。

用法：
    python3 generate_list.py              # 使用默认博客标题
    python3 generate_list.py --title "我的技术博客"  # 自定义标题
"""

import os
import re
import json
import argparse
from pathlib import Path
from datetime import datetime

# --- 配置 ---
POSTS_DIR = Path(__file__).resolve().parent / "posts"
OUTPUT_FILE = Path(__file__).resolve().parent / "config.js"
DEFAULT_TITLE = "我的极简个人博客"
DEFAULT_OWNER = "marlinai"
DEFAULT_REPO = "my-blog"
DEFAULT_BRANCH = "main"
SUMMARY_MAX_LEN = 100  # 摘要最大字符数


def extract_title_and_summary(md_path):
    """
    从 Markdown 文件中提取标题和摘要。
    - 标题：第一个 `# ` 开头的行（去掉 # 和首尾空白）
    - 摘要：第一个非空、非标题、非图片的非纯标记段落
    返回 (title_or_None, summary_or_None)
    """
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  ⚠ 无法读取 {md_path.name}: {e}")
        return None, None

    title = None
    summary_lines = []
    in_summary = False

    for line in lines:
        stripped = line.strip()

        # 提取标题：首个 # 开头的行
        if title is None and stripped.startswith("# ") and not stripped.startswith("## "):
            title = stripped[2:].strip()
            continue

        # 跳过其他标题行、空行、分隔线、图片、代码块标记
        if not in_summary:
            if (
                stripped == ""
                or stripped.startswith("#")
                or stripped.startswith("---")
                or stripped.startswith("![]")
                or stripped.startswith("```")
                or stripped.startswith(">")
                or stripped.startswith("|")
            ):
                continue
            # 对纯标记符号的行也跳过
            if re.match(r"^[\*\-\+\>\|\!\#\`\~\[\]]+$", stripped):
                continue
            in_summary = True

        if in_summary:
            # 遇到标题行或分隔线时停止收集摘要
            if stripped.startswith("#") or stripped.startswith("---") or stripped.startswith("```"):
                break
            if stripped == "" and summary_lines and summary_lines[-1] == "":
                continue  # 跳过连续空行
            summary_lines.append(stripped)

    # 拼接摘要
    if summary_lines:
        raw = " ".join(summary_lines)
        # 去掉 Markdown 标记
        cleaned = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", raw)  # 链接文本
        cleaned = re.sub(r"[*_~`]{1,3}", "", cleaned)  # 粗体/斜体/代码标记
        cleaned = re.sub(r"!\[.*?\]\(.*?\)", "", cleaned)  # 图片
        cleaned = cleaned.strip()
        summary = cleaned[:SUMMARY_MAX_LEN]
        if len(cleaned) > SUMMARY_MAX_LEN:
            summary += "…"
        return title, summary if summary else None

    return title, None


def title_to_filename(title):
    """将文章标题转为文件名友好的形式"""
    return title.replace(" ", "-").replace("/", "-") + ".md"


def js_str(s):
    """将 Python 字符串转为 JS 安全字符串，保留中文可读性"""
    if s is None:
        return "null"
    return json.dumps(s, ensure_ascii=False)


def generate_config(blog_title, owner, repo, branch):
    """主函数：扫描 posts/ 目录，生成 config.js"""
    if not POSTS_DIR.exists():
        print(f"❌ 错误：posts/ 目录不存在 ({POSTS_DIR})")
        return

    md_files = sorted(POSTS_DIR.glob("*.md"))
    if not md_files:
        print("⚠ 警告：posts/ 目录下没有 .md 文件，将生成空文章列表。")

    articles = []

    for md_path in md_files:
        filename = md_path.name
        print(f"  📄 处理: {filename}")

        title, summary = extract_title_and_summary(md_path)

        # 获取文件修改时间
        mtime = os.path.getmtime(md_path)
        date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

        article = {
            "file": filename,
            "title": title,
            "date": date_str,
            "summary": summary,
        }
        articles.append(article)

    # 按日期倒序排列（最新的在前）
    articles.sort(key=lambda a: a["date"], reverse=True)

    # 生成 config.js 内容
    articles_js = ",\n        ".join(
        [
            f'{{ file: {js_str(a["file"])}, title: {js_str(a["title"])}, date: {js_str(a["date"])}, summary: {js_str(a["summary"])} }}'
            for a in articles
        ]
    )

    config_content = f"""// 此文件由 generate_list.py 自动生成，请勿手动编辑
// 更新时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
const BLOG_CONFIG = {{
    title: {js_str(blog_title)},
    owner: {js_str(owner)},
    repo: {js_str(repo)},
    branch: {js_str(branch)},
    articles: [
        {articles_js}
    ]
}};
"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(config_content)

    print(f"\n✅ 已生成 {OUTPUT_FILE}")
    print(f"   博客标题: {blog_title}")
    print(f"   文章数量: {len(articles)}")
    for a in articles:
        print(f"     • {a['title'] or a['file']} ({a['date']})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="扫描 posts/ 目录，自动生成 config.js")
    parser.add_argument(
        "--title",
        type=str,
        default=DEFAULT_TITLE,
        help=f'博客标题 (默认: "{DEFAULT_TITLE}")',
    )
    parser.add_argument("--owner", type=str, default=DEFAULT_OWNER, help=f'GitHub 用户名 (默认: {DEFAULT_OWNER})')
    parser.add_argument("--repo", type=str, default=DEFAULT_REPO, help=f'仓库名 (默认: {DEFAULT_REPO})')
    parser.add_argument("--branch", type=str, default=DEFAULT_BRANCH, help=f'分支名 (默认: {DEFAULT_BRANCH})')
    args = parser.parse_args()

    print("🔍 扫描 posts/ 目录...")
    generate_config(args.title, args.owner, args.repo, args.branch)
