# 使用智谱 AI (GLM) 运行 PageIndex

本文档介绍如何使用智谱 AI 的 Anthropic 兼容接口运行 PageIndex。

## 🌟 为什么选择智谱 AI？

- ✅ **国内可用**：无需科学上网，访问速度快
- ✅ **兼容接口**：完全兼容 Anthropic API 格式
- ✅ **价格实惠**：相比国外服务更有价格优势
- ✅ **中文优化**：对中文文档处理更优秀

## 📋 前提条件

### 1. 获取智谱 API Key

1. 访问 [智谱 AI 开放平台](https://open.bigmodel.cn/)
2. 注册账户并登录
3. 在控制台创建 API key
4. 确保账户有足够的余额

### 2. 安装依赖

```bash
pip3 install --upgrade -r requirements.txt
```

## 🔑 配置 API Key

### 方法 1: 使用 .env 文件（推荐）

在项目根目录创建 `.env` 文件：

```bash
cat > .env << 'EOF'
ANTHROPIC_API_KEY=your-zhipu-api-key-here
ANTHROPIC_API_BASE=https://open.bigmodel.cn/api/anthropic
EOF
```

**重要**：
- `ANTHROPIC_API_KEY` 设置为你的智谱 API key
- `ANTHROPIC_API_BASE` 必须设置为 `https://open.bigmodel.cn/api/anthropic`

### 方法 2: 设置环境变量

```bash
export ANTHROPIC_API_KEY='your-zhipu-api-key-here'
export ANTHROPIC_API_BASE='https://open.bigmodel.cn/api/anthropic'
```

## 🧪 测试 API 连接

在运行 PageIndex 之前，建议先测试 API 连接：

```bash
python3 test_anthropic_api.py
```

**成功示例**：

```
======================================================================
Anthropic API 诊断工具
======================================================================

✅ API Key: your-key-prefix...suffix
   长度: 48 字符
   API Base: https://open.bigmodel.cn/api/anthropic

======================================================================
测试模型: claude-3-5-sonnet-20241022
======================================================================
状态码: 200
✅ 成功!
响应: Hello!
使用模型: claude-3-5-sonnet-20241022
Stop reason: end_turn
输入tokens: 10
输出tokens: 3
```

## 🚀 运行 PageIndex

### 基本用法

```bash
python3 run_pageindex_anthropic.py --pdf_path /path/to/your/document.pdf
```

由于环境变量 `ANTHROPIC_API_BASE` 已设置，程序会自动使用智谱 AI 的接口。

### 处理中文 PDF

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path 中文文档.pdf \
  --model claude-3-5-sonnet-20241022
```

### 快速处理模式（节省成本）

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --model claude-3-5-haiku-20241022 \
  --if-add-node-summary no
```

### 完整功能（包含摘要和描述）

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --if-add-node-summary yes \
  --if-add-doc-description yes
```

## 🎯 智谱 AI 支持的模型

智谱 AI 的 Anthropic 兼容接口支持以下模型：

| 模型名称 | 说明 | 适用场景 |
|---------|------|---------|
| `claude-3-5-sonnet-20241022` | 高性能模型 | 复杂文档、需要准确理解 |
| `claude-3-5-haiku-20241022` | 快速模型 | 简单文档、快速处理 |
| `claude-3-opus-20240229` | 顶级模型 | 最复杂的文档分析 |

**注意**：实际映射到智谱 AI 的 GLM 系列模型，但接口保持兼容。

## 📁 输出文件

处理完成后，结果保存到：

```
results/document_tree_claude.json
```

日志文件保存到：

```
logs/document.pdf_20250117_143022.json
```

## 💰 成本估算

智谱 AI 的定价通常比国外服务更优惠。具体价格请参考：
- [智谱 AI 价格](https://open.bigmodel.cn/pricing)

## 🔧 高级配置

### 自定义所有参数

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --model claude-3-5-sonnet-20241022 \
  --toc-check-pages 30 \
  --max-pages-per-node 15 \
  --max-tokens-per-node 25000 \
  --if-add-node-id yes \
  --if-add-node-summary yes \
  --if-add-doc-description yes
```

### 处理 Markdown 文件

```bash
python3 run_pageindex_anthropic.py \
  --md_path document.md \
  --if-add-node-summary yes
```

## 🐛 故障排除

### API Key 无效

```
❌ 401 Unauthorized - API密钥无效
```

**解决方法**：
1. 检查 API key 是否正确
2. 确认在智谱 AI 控制台生成的 key
3. 检查 `.env` 文件中是否有多余的引号或空格

### API Base URL 未设置

如果忘记设置 `ANTHROPIC_API_BASE`，会连接到 Anthropic 官方服务器，导致失败。

**解决方法**：
```bash
export ANTHROPIC_API_BASE='https://open.bigmodel.cn/api/anthropic'
```

### 余额不足

```
❌ 403 Forbidden - 余额不足
```

**解决方法**：
1. 登录智谱 AI 控制台
2. 充值账户余额

### 速率限制

```
⚠️  429 Rate Limit - 超过速率限制
```

**解决方法**：
1. 等待一段时间后重试
2. 升级到更高级别的账户
3. 降低并发请求数量

### 网络连接问题

**解决方法**：
1. 检查网络连接
2. 确认可以访问 `https://open.bigmodel.cn`
3. 检查防火墙设置

## 📊 性能对比

| 指标 | Anthropic 官方 | 智谱 AI 兼容接口 |
|------|---------------|----------------|
| **访问速度** | 较慢（需科学上网） | 快（国内直连） |
| **中文支持** | 一般 | 优秀 |
| **价格** | 较高 | 较低 |
| **稳定性** | 高 | 高 |

## 🔄 在不同提供商间切换

如果需要切换回 Anthropic 官方或使用其他提供商：

### 使用 Anthropic 官方

```bash
# 删除或修改 .env 文件
export ANTHROPIC_API_KEY='sk-ant-api03-...'
unset ANTHROPIC_API_BASE  # 或删除这行
```

### 使用 OpenAI

```bash
python3 run_pageindex.py --pdf_path document.pdf
```

### 使用 Google Gemini

```bash
python3 run_pageindex_gemini.py --pdf_path document.pdf
```

## 📝 完整示例

### .env 文件示例

```bash
# 智谱 AI 配置
ANTHROPIC_API_KEY=1234567890abcdef1234567890abcdef12345678
ANTHROPIC_API_BASE=https://open.bigmodel.cn/api/anthropic

# 可选：其他提供商（如果需要）
# OPENAI_API_KEY=sk-...
# GEMINI_API_KEY=AIza...
```

### 完整运行命令

```bash
# 1. 测试连接
python3 test_anthropic_api.py

# 2. 处理文档
python3 run_pageindex_anthropic.py \
  --pdf_path 财务报告.pdf \
  --model claude-3-5-sonnet-20241022 \
  --if-add-node-summary yes

# 3. 查看结果
cat results/财务报告_tree_claude.json
```

## 💡 最佳实践

1. **首次使用**：先用小文档测试，确认配置正确
2. **成本控制**：对于测试，使用 `--if-add-node-summary no`
3. **中文文档**：智谱 AI 对中文处理效果更好
4. **大文档**：考虑分批处理或增加 `--max-pages-per-node`
5. **保存日志**：查看 `logs/` 目录了解处理详情

## 🔗 相关链接

- [智谱 AI 开放平台](https://open.bigmodel.cn/)
- [智谱 AI 文档](https://open.bigmodel.cn/dev/api)
- [PageIndex 原理说明](README.md)
- [Anthropic API 使用说明](ANTHROPIC_USAGE.md)

## ❓ 常见问题

**Q: 智谱 AI 的兼容接口和 Anthropic 官方有什么区别？**

A: 智谱 AI 提供了与 Anthropic 完全兼容的 API 接口，底层使用的是智谱自己的 GLM 系列模型，但接口格式完全相同。

**Q: 可以混用不同的 API 提供商吗？**

A: 可以！通过设置不同的环境变量，可以随时切换。

**Q: 处理一个 100 页的 PDF 大概需要多少费用？**

A: 取决于文档复杂度和配置，通常在几元到几十元人民币之间。建议先用小文档测试。

**Q: 为什么要使用 Anthropic 格式而不是 OpenAI 格式？**

A: 智谱 AI 同时提供了多种兼容接口。本项目选择 Anthropic 格式是因为已经实现了完整的适配器，可以直接复用。
