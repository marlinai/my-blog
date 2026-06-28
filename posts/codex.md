# OpenAI Codex 模型本地接入与高效使用指南

本教程将为你详细讲解如何通过官方 API 接入 OpenAI Codex（或目前替代的最新低延迟代码模型如 `gpt-4o` / `o1` 系列、`code-davinci-002`），以及如何在主流代码编辑器中配置与下载相关的辅助插件，建立起完全属于自己的 AI 辅助编程环境。

---

## 💡 核心前言：关于 Codex 的重要现状

在正式开始前，需要明确一个技术事实：
*   **不可本地纯离线运行**：OpenAI Codex 是一个拥有数百亿参数的超大型神经网络，无法像开源模型（如 Qwen-2.5-Coder、DeepSeek-Coder）那样通过 Ollama 或 `llama.cpp` 直接下载到个人的 Mac 或 Windows 电脑上进行纯离线推理。
*   **通过 API 或插件消费**：目前使用 Codex 能力的标准方式是**调用 OpenAI API** 或者下载集成了该能力的官方/第三方插件（如 GitHub Copilot）。

如果你需要实现完全的本地离线代码大模型，推荐在配置有双显卡或 M系列芯片的机器上使用 **Ollama / `llama.cpp`** 部署 `Qwen2.5-Coder-32B`。本教程将重点介绍如何接入正统的 OpenAI 代码大模型流派。

---

## 一、 获取 OpenAI API 凭证 (密钥)

要下载和调用 Codex 及其衍生模型，首先需要获取 API 密钥：

1. 访问并登录 [OpenAI 开发者平台 (platform.openai.com)](https://platform.openai.com/)。
2. 导航至左侧菜单的 **API Keys**。
3. 点击 **Create new secret key**（创建新密钥）。
4. 给密钥起一个名字（例如 `Codex-Dev`），生成后**立即复制并保存**。密钥只会显示一次，遗失需重新创建。
5. *注意：请确保你的账户内有足够的额度（Credit）以供调用。*

---

## 二、 在本地环境中测试与下载调用库

我们通过 Python 脚本来测试本地环境对 Codex/OpenAI 接口的连通性。

### 1. 安装官方依赖库
打开终端 (Terminal) 或命令提示符，通过 `pip` 下载最新版的 OpenAI SDK：
```bash
pip install --upgrade openai
