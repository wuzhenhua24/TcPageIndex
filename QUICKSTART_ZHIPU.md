# 🚀 快速开始：使用智谱 AI 运行 PageIndex

> 3 分钟快速上手指南

## 第一步：安装依赖

```bash
pip3 install --upgrade -r requirements.txt
```

## 第二步：配置 API Key

创建 `.env` 文件：

```bash
cat > .env << 'EOF'
ANTHROPIC_API_KEY=你的智谱AI_API_KEY
ANTHROPIC_API_BASE=https://open.bigmodel.cn/api/anthropic
EOF
```

**如何获取智谱 API Key？**
1. 访问 https://open.bigmodel.cn/
2. 注册并登录
3. 在控制台创建 API key

## 第三步：测试连接

```bash
python3 test_anthropic_api.py
```

**看到 ✅ 成功！** 就可以继续了。

## 第四步：运行 PageIndex

```bash
python3 run_pageindex_anthropic.py --pdf_path 你的文档.pdf
```

**等待处理完成** (大约 20-40 分钟)

## 查看结果

```bash
cat results/你的文档_tree_claude.json
```

---

## 💡 常用命令

### 快速模式（不生成摘要，更快更便宜）

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --if-add-node-summary no
```

### 完整模式（包含摘要和描述）

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --if-add-node-summary yes \
  --if-add-doc-description yes
```

### 使用更快的模型

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --model claude-3-5-haiku-20241022
```

---

## ❓ 遇到问题？

### API Key 无效
```bash
# 检查 .env 文件内容
cat .env

# 确保没有多余的空格或引号
```

### 网络连接失败
```bash
# 测试能否访问智谱 AI
curl -I https://open.bigmodel.cn
```

### 需要更多帮助
- 详细文档：[ZHIPU_USAGE.md](ZHIPU_USAGE.md)
- Anthropic 说明：[ANTHROPIC_USAGE.md](ANTHROPIC_USAGE.md)

---

## 📊 支持的提供商

| 提供商 | 配置 | 运行命令 |
|-------|------|---------|
| **智谱 AI** | `ANTHROPIC_API_BASE=https://open.bigmodel.cn/api/anthropic` | `run_pageindex_anthropic.py` |
| **Anthropic** | 默认 | `run_pageindex_anthropic.py` |
| **OpenAI** | `CHATGPT_API_KEY` | `run_pageindex.py` |
| **Gemini** | `GEMINI_API_KEY` | `run_pageindex_gemini.py` |

完整示例请查看 [.env.example](.env.example)
