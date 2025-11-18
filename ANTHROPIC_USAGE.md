# PageIndex with Anthropic Claude Support

本文档介绍如何使用 Anthropic Claude API 运行 PageIndex。

## 📋 前提条件

1. **获取 Anthropic API Key**
   - 访问 [Anthropic Console](https://console.anthropic.com/)
   - 注册账户并创建 API key
   - 确保账户有足够的余额

2. **安装依赖**
   ```bash
   pip3 install --upgrade -r requirements.txt
   ```

## 🔑 配置 API Key

有两种方式配置 API key：

### 方法 1: 使用 .env 文件（推荐）

在项目根目录创建 `.env` 文件：

```bash
echo 'ANTHROPIC_API_KEY=sk-ant-api03-...' > .env
```

### 方法 2: 设置环境变量

```bash
export ANTHROPIC_API_KEY='sk-ant-api03-...'
```

### 方法 3: 使用兼容的 API 提供商（如智谱 AI）

如果你使用的是 Anthropic 兼容接口的其他提供商，需要额外设置 `ANTHROPIC_API_BASE`：

**使用智谱 AI**：

```bash
# .env 文件
ANTHROPIC_API_KEY=your-zhipu-api-key
ANTHROPIC_API_BASE=https://open.bigmodel.cn/api/anthropic
```

或

```bash
export ANTHROPIC_API_KEY='your-zhipu-api-key'
export ANTHROPIC_API_BASE='https://open.bigmodel.cn/api/anthropic'
```

> 📝 **注意**：使用智谱 AI 等第三方兼容接口时，请参考 [智谱 AI 使用指南](ZHIPU_USAGE.md) 获取详细说明。

## 🧪 测试 API 连接

在运行 PageIndex 之前，建议先测试 API 连接：

```bash
python3 test_anthropic_api.py
```

如果成功，你会看到：

```
======================================================================
Anthropic API 诊断工具
======================================================================

✅ API Key: sk-ant-api03-xxxxx...xxxxx
   长度: 108 字符

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

======================================================================
✅ 找到可用模型: claude-3-5-sonnet-20241022
======================================================================
```

## 🚀 运行 PageIndex

### 处理 PDF 文件

基本用法：

```bash
python3 run_pageindex_anthropic.py --pdf_path /path/to/your/document.pdf
```

### 可用参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--pdf_path` | PDF 文件路径 | 必需 |
| `--model` | Claude 模型名称 | claude-3-5-sonnet-20241022 |
| `--toc-check-pages` | 检查目录的页数 | 20 |
| `--max-pages-per-node` | 每个节点最大页数 | 10 |
| `--max-tokens-per-node` | 每个节点最大 token 数 | 20000 |
| `--if-add-node-id` | 是否添加节点 ID | yes |
| `--if-add-node-summary` | 是否生成节点摘要 | yes |
| `--if-add-doc-description` | 是否生成文档描述 | no |
| `--if-add-node-text` | 是否添加节点文本 | no |

### 高级示例

使用 Claude Haiku（更快更便宜）：

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --model claude-3-5-haiku-20241022
```

禁用摘要生成以节省成本：

```bash
python3 run_pageindex_anthropic.py \
  --pdf_path document.pdf \
  --if-add-node-summary no
```

### 处理 Markdown 文件

```bash
python3 run_pageindex_anthropic.py --md_path /path/to/your/document.md
```

## 📊 可用模型

| 模型 | 说明 | 速度 | 成本 |
|------|------|------|------|
| `claude-3-5-sonnet-20241022` | 最新 Sonnet，最佳性能 | 中 | 中 |
| `claude-3-5-haiku-20241022` | 最新 Haiku，快速便宜 | 快 | 低 |
| `claude-3-opus-20240229` | Opus，最强推理能力 | 慢 | 高 |

## 📁 输出文件

处理完成后，结果会保存到：

```
results/document_tree_claude.json
```

日志文件会保存到：

```
logs/document.pdf_20250117_143022.json
```

## 🔄 与其他 LLM 切换

本项目支持三种 LLM：

1. **OpenAI** (原版):
   ```bash
   python3 run_pageindex.py --pdf_path document.pdf
   ```

2. **Google Gemini**:
   ```bash
   python3 run_pageindex_gemini.py --pdf_path document.pdf
   ```

3. **Anthropic Claude**:
   ```bash
   python3 run_pageindex_anthropic.py --pdf_path document.pdf
   ```

## 🔍 实现原理

Anthropic 适配器的工作原理：

1. **适配器模块** (`pageindex/utils_anthropic.py`):
   - 将 OpenAI 风格的函数调用转换为 Anthropic API 格式
   - 保持与原始代码相同的接口签名
   - 支持同步和异步调用

2. **模块注入** (`run_pageindex_anthropic.py`):
   ```python
   # 注入 Anthropic 适配器替换原始 utils
   sys.modules['pageindex.utils'] = utils_anthropic
   ```

3. **API 差异处理**:
   - OpenAI: `{"role": "system", "content": "..."}`
   - Anthropic: `{"role": "user", "content": "..."}`
   - 适配器自动处理格式转换

## ⚠️ 注意事项

1. **成本控制**:
   - Claude Sonnet 约为 $3/百万输入 tokens
   - 大文档可能产生较高费用
   - 建议先用 `--if-add-node-summary no` 测试

2. **速率限制**:
   - 免费层有较严格的速率限制
   - 付费账户享有更高限额

3. **Token 估算**:
   - 当前使用 tiktoken 估算 token 数
   - 与 Claude 实际计数可能有 5-10% 偏差

4. **重试机制**:
   - 遇到网络错误会自动重试 10 次
   - 每次重试间隔 2 秒

## 🐛 故障排除

### API Key 无效

```
❌ 401 Unauthorized - API密钥无效
```

**解决方法**:
1. 检查 API key 是否正确复制
2. 在 Console 重新生成 API key
3. 确认没有额外的空格或换行符

### 速率限制

```
⚠️  429 Rate Limit - 超过速率限制
```

**解决方法**:
1. 等待几分钟后重试
2. 升级到付费账户
3. 减少并发请求

### 余额不足

**解决方法**:
1. 在 Console 充值
2. 检查账户余额

## 📝 API 格式对比

### OpenAI API

```python
{
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "You are helpful"},
        {"role": "user", "content": "Hello"}
    ]
}
```

### Anthropic API

```python
{
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 4096,
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}
```

**主要区别**:
1. Anthropic 不支持 `system` role，需要将其合并到 `user` 消息
2. Anthropic 必须提供 `max_tokens` 参数
3. Headers 需要 `x-api-key` 和 `anthropic-version`

适配器已自动处理这些差异，无需手动转换。

## 📚 相关文档

- [Anthropic API 文档](https://docs.anthropic.com/)
- [Claude 模型对比](https://docs.anthropic.com/claude/docs/models-overview)
- [PageIndex 原理](README.md)
