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

**重要**：必须指定智谱的模型名称（不是Claude的）：

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path 你的文档.pdf \
  --model glm-4.6
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
  --model glm-4-air \
  --if-add-node-summary no
```

### 完整模式（包含摘要和描述）

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --model glm-4.6 \
  --if-add-node-summary yes \
  --if-add-doc-description yes
```

### 使用超快模型（大批量处理）

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --model glm-4-flash
```

---

## ❓ 遇到问题？

### 1. 403 Forbidden 错误

如果看到 `403 Access denied`：

```bash
# 检查 API Key 格式
cat .env

# 确保：
# 1. API Key 是从智谱AI控制台获取的
# 2. 没有多余的空格或引号
# 3. 账户有足够余额
```

**解决方法**：
1. 访问 https://open.bigmodel.cn/
2. 登录控制台
3. 检查账户余额
4. 重新生成 API Key

### 2. 模型名称错误

使用智谱AI时必须使用 GLM 模型：

```bash
# ✅ 正确
--model glm-4.6

# ❌ 错误（这是 Claude 的模型名）
--model claude-3-5-sonnet-20241022
```

### 3. API Key 环境变量未设置

```bash
# 检查 .env 文件内容
cat .env

# 手动导出环境变量测试
export ANTHROPIC_API_KEY='你的key'
export ANTHROPIC_API_BASE='https://open.bigmodel.cn/api/anthropic'
python3 test_anthropic_api.py
```

### 4. 网络连接失败
```bash
# 测试能否访问智谱 AI
curl -I https://open.bigmodel.cn
```

### 需要更多帮助
- 详细文档：[ZHIPU_USAGE.md](ZHIPU_USAGE.md)
- Anthropic 说明：[ANTHROPIC_USAGE.md](ANTHROPIC_USAGE.md)
- 智谱AI文档：https://open.bigmodel.cn/dev/api

---

## 📊 支持的提供商

| 提供商 | 配置 | 运行命令 |
|-------|------|---------|
| **智谱 AI** | `ANTHROPIC_API_BASE=https://open.bigmodel.cn/api/anthropic` | `run_pageindex_anthropic.py` |
| **Anthropic** | 默认 | `run_pageindex_anthropic.py` |
| **OpenAI** | `CHATGPT_API_KEY` | `run_pageindex.py` |
| **Gemini** | `GEMINI_API_KEY` | `run_pageindex_gemini.py` |

完整示例请查看 [.env.example](.env.example)
