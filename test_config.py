#!/usr/bin/env python3
"""Test script to verify environment variable overrides"""

import os
import sys

# Import the modified server.py to trigger environment variable setup
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# First, let's see what the environment variables are before import
print("Before importing server.py:")
print(f"OPENAI_API_KEY: {os.environ.get('OPENAI_API_KEY', 'NOT SET')[:20]}...")
print(f"OPENAI_BASE_URL: {os.environ.get('OPENAI_BASE_URL', 'NOT SET')}")
print(f"FAST_LLM: {os.environ.get('FAST_LLM', 'NOT SET')}")
print(f"SMART_LLM: {os.environ.get('SMART_LLM', 'NOT SET')}")
print(f"STRATEGIC_LLM: {os.environ.get('STRATEGIC_LLM', 'NOT SET')}")
print(f"DEEPSEEK_API_KEY: {os.environ.get('DEEPSEEK_API_KEY', 'NOT SET')[:20]}...")

print("\n" + "="*50 + "\n")

# Now import server.py which will set the environment variables
import server

print("After importing server.py:")
print(f"OPENAI_API_KEY: {os.environ.get('OPENAI_API_KEY', 'NOT SET')[:20]}...")
print(f"OPENAI_BASE_URL: {os.environ.get('OPENAI_BASE_URL', 'NOT SET')}")
print(f"FAST_LLM: {os.environ.get('FAST_LLM', 'NOT SET')}")
print(f"SMART_LLM: {os.environ.get('SMART_LLM', 'NOT SET')}")
print(f"STRATEGIC_LLM: {os.environ.get('STRATEGIC_LLM', 'NOT SET')}")
print(f"DEEPSEEK_API_KEY: {os.environ.get('DEEPSEEK_API_KEY', 'NOT SET')[:20]}...")

print("\n" + "="*50 + "\n")

# Test that environment variables are not leaked to parent process
print("Environment variable verification:")
print(f"OPENAI_API_KEY starts with 'nvapi-': {os.environ.get('OPENAI_API_KEY', '').startswith('nvapi-')}")
print(f"OPENAI_BASE_URL is NVIDIA endpoint: {os.environ.get('OPENAI_BASE_URL', '') == 'https://integrate.api.nvidia.com/v1/chat/completions'}")
print(f"FAST_LLM is openai:deepseek-ai/deepseek-v3.2: {os.environ.get('FAST_LLM', '') == 'openai:deepseek-ai/deepseek-v3.2'}")
print(f"SMART_LLM is openai:deepseek-ai/deepseek-v3.2: {os.environ.get('SMART_LLM', '') == 'openai:deepseek-ai/deepseek-v3.2'}")
print(f"STRATEGIC_LLM is openai:deepseek-ai/deepseek-v3.2: {os.environ.get('STRATEGIC_LLM', '') == 'openai:deepseek-ai/deepseek-v3.2'}")