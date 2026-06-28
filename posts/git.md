# Git 基础与进阶实用教程

本教程全面介绍了 Git 的核心概念、日常高频操作以及进阶实战技巧，帮助你从零开始掌握版本控制，建立起清晰的代码管理工作流。

---

## 一、 Git 核心概念回顾

在深入命令之前，理解 Git 的“三个工作区域”至关重要：

1. **工作区 (Working Directory)**：你在电脑里实际看得到、正在修改的文件目录。
2. **暂存区 (Staging Area / Index)**：一个临时的保存区域，用来存放你准备提交的修改。
3. **本地仓库 (Repository)**：保存了所有版本历史记录的地方，通过 `commit` 将暂存区的内容永久存入此处。
4. **远程仓库 (Remote)**：托管在云端（如 GitHub、GitLab、Gitee）的仓库，用于团队协作。

---

## 二、 基础配置与初始化

### 1. 首次使用必配：设置用户信息
正如在本地提交时常遇到的提示一样，Git 需要明确每一次提交的作者身份：
```bash
# 全局配置用户名
git config --global user.name "你的名字或昵称"

# 全局配置邮箱
git config --global user.email "your_email@example.com"
