#!/usr/bin/env python3
"""Test script to verify GPT Researcher configuration with NVIDIA API and DeepSeek model"""

import os
import sys
import asyncio
from gpt_researcher import GPTResearcher
from gpt_researcher.config import Config

# First, set up environment variables
os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_BASE_URL"] = "https://integrate.api.nvidia.com/v1/chat/completions"
os.environ["FAST_LLM"] = "deepseek:deepseek-v3.2"
os.environ["SMART_LLM"] = "deepseek:deepseek-v3.2"
os.environ["STRATEGIC_LLM"] = "deepseek:deepseek-v3.2"
os.environ["EMBEDDING"] = "openai:text-embedding-3-small"
os.environ["DEEPSEEK_API_KEY"] = "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"

# Tavily API key for web search
os.environ["TAVILY_API_KEY"] = "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"

print("Testing GPT Researcher Configuration")
print("="*50)

# Test 1: Check Config initialization
print("\n1. Testing Config initialization...")
try:
    config = Config()
    print(f"✓ Config loaded successfully")
    print(f"  - FAST_LLM: {config.fast_llm}")
    print(f"  - SMART_LLM: {config.smart_llm}")
    print(f"  - STRATEGIC_LLM: {config.strategic_llm}")
    print(f"  - EMBEDDING: {config.embedding}")
    print(f"  - FAST_LLM_PROVIDER: {config.fast_llm_provider}")
    print(f"  - FAST_LLM_MODEL: {config.fast_llm_model}")
    print(f"  - SMART_LLM_PROVIDER: {config.smart_llm_provider}")
    print(f"  - SMART_LLM_MODEL: {config.smart_llm_model}")
except Exception as e:
    print(f"✗ Config initialization failed: {e}")

# Test 2: Check environment variables
print("\n2. Testing environment variables...")
print(f"  - OPENAI_API_KEY: {os.environ.get('OPENAI_API_KEY', 'NOT SET')[:20]}...")
print(f"  - OPENAI_BASE_URL: {os.environ.get('OPENAI_BASE_URL', 'NOT SET')}")
print(f"  - DEEPSEEK_API_KEY: {os.environ.get('DEEPSEEK_API_KEY', 'NOT SET')[:20]}...")
print(f"  - TAVILY_API_KEY: {os.environ.get('TAVILY_API_KEY', 'NOT SET')[:20]}...")

# Test 3: Initialize GPTResearcher (without actual research)
print("\n3. Testing GPTResearcher initialization...")
try:
    # Initialize with a simple query
    researcher = GPTResearcher("test query")
    print(f"✓ GPTResearcher initialized successfully")
    print(f"  - Query: {researcher.query}")
    print(f"  - Config: {type(researcher.config).__name__}")

    # Check researcher's config
    if hasattr(researcher, 'config'):
        print(f"  - Researcher FAST_LLM: {researcher.config.fast_llm}")
        print(f"  - Researcher SMART_LLM: {researcher.config.smart_llm}")

except Exception as e:
    print(f"✗ GPTResearcher initialization failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*50)
print("Configuration test completed.")

# Note: We're not running actual research to avoid API costs
print("\n⚠️  Note: Actual research not performed to avoid API costs.")
print("To test full functionality, run the MCP server and try a query.")