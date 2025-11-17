#!/usr/bin/env python3
"""Anthropic API 诊断工具"""

import os
import requests
import sys

def test_anthropic_api(api_key):
    """测试 Anthropic API 连接"""

    print("=" * 70)
    print("Anthropic API 诊断工具")
    print("=" * 70)
    print(f"\n✅ API Key: {api_key[:20]}...{api_key[-5:]}")
    print(f"   长度: {len(api_key)} 字符")

    # 测试不同的模型
    models = [
        "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022",
        "claude-3-opus-20240229",
    ]

    for model_name in models:
        print(f"\n{'='*70}")
        print(f"测试模型: {model_name}")
        print(f"{'='*70}")

        url = "https://api.anthropic.com/v1/messages"

        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }

        payload = {
            "model": model_name,
            "max_tokens": 100,
            "messages": [
                {"role": "user", "content": "Say hello in one word"}
            ]
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )

            print(f"状态码: {response.status_code}")

            if response.status_code == 200:
                print("✅ 成功!")
                result = response.json()
                if "content" in result:
                    text = result["content"][0]["text"]
                    print(f"响应: {text}")
                    print(f"使用模型: {result.get('model', 'N/A')}")
                    print(f"Stop reason: {result.get('stop_reason', 'N/A')}")
                    print(f"输入tokens: {result.get('usage', {}).get('input_tokens', 'N/A')}")
                    print(f"输出tokens: {result.get('usage', {}).get('output_tokens', 'N/A')}")
                    return model_name
            elif response.status_code == 401:
                print("❌ 401 Unauthorized - API密钥无效")
                print(f"   响应: {response.text}")
            elif response.status_code == 403:
                print("❌ 403 Forbidden - 无权限访问")
                print(f"   响应: {response.text}")
            elif response.status_code == 404:
                print("⚠️  404 Not Found - 模型不存在或已弃用")
            elif response.status_code == 429:
                print("⚠️  429 Rate Limit - 超过速率限制")
                print(f"   响应: {response.text}")
            else:
                print(f"❌ 错误: {response.status_code}")
                print(f"   响应: {response.text[:300]}")
        except requests.exceptions.Timeout:
            print("❌ 请求超时")
        except requests.exceptions.ConnectionError:
            print("❌ 连接失败，请检查网络")
        except Exception as e:
            print(f"❌ 异常: {e}")

    return None

def test_simple_prompt(api_key):
    """测试简单的提示"""
    print(f"\n{'='*70}")
    print("测试完整的对话功能")
    print(f"{'='*70}")

    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    payload = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 200,
        "messages": [
            {"role": "user", "content": "What is 2+2? Answer in one sentence."}
        ]
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            text = result["content"][0]["text"]
            print(f"✅ 问题: What is 2+2?")
            print(f"✅ 回答: {text}")
            return True
        else:
            print(f"❌ 测试失败: {response.status_code}")
            print(f"   {response.text}")
            return False
    except Exception as e:
        print(f"❌ 异常: {e}")
        return False

if __name__ == "__main__":
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("错误: ANTHROPIC_API_KEY 环境变量未设置")
        print("\n设置方法:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        print("\n或创建 .env 文件:")
        print("  echo 'ANTHROPIC_API_KEY=your-api-key-here' > .env")
        print("\n获取 API key: https://console.anthropic.com/")
        sys.exit(1)

    # 测试基本连接
    result = test_anthropic_api(api_key)

    if result:
        print(f"\n{'='*70}")
        print(f"✅ 找到可用模型: {result}")
        print(f"{'='*70}")

        # 测试完整对话
        test_simple_prompt(api_key)

        print(f"\n{'='*70}")
        print("✅ 所有测试通过！可以使用 Anthropic API")
        print("=" * 70)
        print("\n使用方法:")
        print("  python3 run_pageindex_anthropic.py --pdf_path your_file.pdf")
    else:
        print(f"\n{'='*70}")
        print("❌ 所有测试都失败了")
        print("=" * 70)
        print("\n建议:")
        print("1. 检查 API key 是否正确")
        print("2. 确认账户有足够的余额")
        print("3. 在 Anthropic Console 重新生成 API key")
        print("   https://console.anthropic.com/")
        sys.exit(1)
