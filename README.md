# Awesome Open Source AI Alternatives 🚀

> A curated list of open-source alternatives to proprietary AI tools (OpenAI, Anthropic, Google, etc.)
> Last updated: July 2026

![Last Updated](https://img.shields.io/badge/last%20updated-July%202026-blue)
![Awesome](https://awesome.re/badge.svg)
![GitHub stars](https://img.shields.io/github/stars/JeevaVenkidu/awesome-open-ai-alternatives?style=social)
![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

This list focuses on practical **ChatGPT alternatives**, self-hostable AI, open model weights, and open-source tools. Check each project's own license before using it commercially; “open weights” is not always the same as an OSI-approved open-source license.

## 📚 Table of Contents
- [🧠 Large Language Models (LLMs)](#llms)
- [🤖 AI Agents & Multi-Agent Frameworks](#agents)
- [💻 Coding Assistants & Dev Tools](#coding)
- [🔍 RAG & Document AI](#rag)
- [🎨 Image Generation](#image)
- [🎬 Video Generation](#video)
- [🗣️ Voice & Audio](#voice)
- [🏠 Local Deployment & Inference](#local)
- [🔧 No-Code / Low-Code AI Platforms](#nocode)
- [📊 Observability & Monitoring](#observability)
- [⚡ Quick Start Guides](#quickstart)
- [📜 License](#license)

<a id="llms"></a>
## 🧠 Large Language Models (LLMs)

| Model | Architecture | Best For | License | VRAM (Approx) | Context | Release Date |
|---|---|---|---|---:|---:|---|
| **GLM-5.2** 🔥 | 744B MoE / 40B active | Coding and reasoning | [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) | Multi-GPU | 1M | 2026 |
| **Kimi K3** 🔥 *(coming July 27)* | 2.8T MoE / 16B active | Frontier reasoning | [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) | Multi-GPU | TBD | 2026-07-27 planned |
| **DeepSeek V4 Pro / Flash** | 1.6T/49B and 284B/13B MoE | Cost-efficient inference | [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) | Multi-GPU | 1M | 2026 |
| **Qwen3.6** | 35B-A3B MoE | Coding on one GPU | [![Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) | ~20 GB | TBD | 2026 |
| **Gemma 4 12B** 🔥 | 11.95B dense, multimodal | General use and local multimodal AI | [![Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) | ~8 GB | TBD | 2026 |
| **Phi-4 Reasoning** | 14B dense | Edge and mobile reasoning | [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) | ~8 GB | TBD | 2025 |
| **Mistral Large 3** | 675B MoE / 41B active | Multilingual generation | [![Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) | Multi-GPU | TBD | 2025 |
| **Llama 4 Scout** | 109B MoE / 17B active | Long-context multimodal work | Llama license | Multi-GPU | 10M | 2025 |
| **MiMo-V2.5** | 1.02T MoE | Agentic coding | [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) | Multi-GPU | 32K native | 2026 |
| **Qwen3** | 235B-A22B MoE | General reasoning | [![Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) | Multi-GPU | 128K | 2025 |
| **DeepSeek R1** | 671B MoE | Open reasoning | [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) | Multi-GPU | 128K | 2025 |
| **Llama 3.3** | 70B dense | Multilingual chat | Llama license | ~40 GB | 128K | 2024 |

*MoE = Mixture of Experts (total parameters / active parameters). VRAM figures are rough inference estimates and depend on quantization, batch size, and context length. Benchmark scores are reported project claims, not independent rankings.*

<a id="agents"></a>
## 🤖 AI Agents & Multi-Agent Frameworks

| Project | Description | GitHub stars | Key feature | License | Status |
|---|---|---|---|---|---|
| **browser-use** | Make websites accessible for AI agents | [![GitHub stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social)](https://github.com/browser-use/browser-use) | Browser automation | [![License](https://img.shields.io/github/license/browser-use/browser-use.svg)](https://github.com/browser-use/browser-use) | Self-Hostable ✅ |
| **CrewAI** | Assemble teams of AI agents | [![GitHub stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social)](https://github.com/crewAIInc/crewAI) | Role-based crews | [![License](https://img.shields.io/github/license/crewAIInc/crewAI.svg)](https://github.com/crewAIInc/crewAI) | Self-Hostable ✅ |
| **AutoGPT** | The original autonomous agent | [![GitHub stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=social)](https://github.com/Significant-Gravitas/AutoGPT) | Autonomous workflows | [![License](https://img.shields.io/github/license/Significant-Gravitas/AutoGPT.svg)](https://github.com/Significant-Gravitas/AutoGPT) | Self-Hostable ✅ |
| **Letta** | Portable AI agents with `.af` files | [![GitHub stars](https://img.shields.io/github/stars/letta-ai/letta?style=social)](https://github.com/letta-ai/letta) | Stateful memory | [![License](https://img.shields.io/github/license/letta-ai/letta.svg)](https://github.com/letta-ai/letta) | Self-Hostable ✅ |
| **eliza** | Autonomous agents for everyone | [![GitHub stars](https://img.shields.io/github/stars/elizaOS/eliza?style=social)](https://github.com/elizaOS/eliza) | Extensible agent runtime | [![License](https://img.shields.io/github/license/elizaOS/eliza.svg)](https://github.com/elizaOS/eliza) | Self-Hostable ✅ |
| **CAMEL OWL** | Multi-agent collaboration; reports 58.18 on GAIA | [![GitHub stars](https://img.shields.io/github/stars/camel-ai/owl?style=social)](https://github.com/camel-ai/owl) | Research agent teams | [![License](https://img.shields.io/github/license/camel-ai/owl.svg)](https://github.com/camel-ai/owl) | Self-Hostable ✅ |
| **CAMEL** | Multi-agent role-play framework | [![GitHub stars](https://img.shields.io/github/stars/camel-ai/camel?style=social)](https://github.com/camel-ai/camel) | Society-of-agents simulations | [![License](https://img.shields.io/github/license/camel-ai/camel.svg)](https://github.com/camel-ai/camel) | Self-Hostable ✅ |
| **SuperAGI** | Dev-first autonomous AI agent framework | [![GitHub stars](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI?style=social)](https://github.com/TransformerOptimus/SuperAGI) | Visual agent management | [![License](https://img.shields.io/github/license/TransformerOptimus/SuperAGI.svg)](https://github.com/TransformerOptimus/SuperAGI) | Self-Hostable ✅ |
| **Agentlas OS** | Build, borrow, and orchestrate specialist agents locally | [![GitHub stars](https://img.shields.io/github/stars/agentlas-ai/Agentlas-OS?style=social)](https://github.com/agentlas-ai/Agentlas-OS) | Model-agnostic Agent Operation Environment (AOE) | [![License](https://img.shields.io/github/license/agentlas-ai/Agentlas-OS.svg)](https://github.com/agentlas-ai/Agentlas-OS) | Self-Hostable ✅ |
| **AgentGPT** | Deploy autonomous AI agents in a browser | [![GitHub stars](https://img.shields.io/github/stars/reworkd/AgentGPT?style=social)](https://github.com/reworkd/AgentGPT) | Browser UI | [![License](https://img.shields.io/github/license/reworkd/AgentGPT.svg)](https://github.com/reworkd/AgentGPT) | Deprecated: repository archived ⚠️ |

### Agent Protocols & Standards

- **MCP (Model Context Protocol)**: widely adopted universal tool and context-calling protocol. [Specification](https://modelcontextprotocol.io/) · [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- **A2A Protocol**: Google's agent-to-agent communication standard. [Repository](https://github.com/google/A2A) · [![GitHub stars](https://img.shields.io/github/stars/google/A2A?style=social)](https://github.com/google/A2A)

<a id="coding"></a>
## 💻 Coding Assistants & Dev Tools

| Project | Description | GitHub stars | Key feature | License / access |
|---|---|---|---|---|
| **Continue** | Open-source AI coding assistant | [![GitHub stars](https://img.shields.io/github/stars/continuedev/continue?style=social)](https://github.com/continuedev/continue) | IDE extensions and chat | [![License](https://img.shields.io/github/license/continuedev/continue.svg)](https://github.com/continuedev/continue) |
| **aider** | AI pair programming in the terminal | [![GitHub stars](https://img.shields.io/github/stars/paul-gauthier/aider?style=social)](https://github.com/paul-gauthier/aider) | Git-aware edits | [![License](https://img.shields.io/github/license/paul-gauthier/aider.svg)](https://github.com/paul-gauthier/aider) |
| **Tabby** | Self-hosted AI coding assistant | [![GitHub stars](https://img.shields.io/github/stars/TabbyML/Tabby?style=social)](https://github.com/TabbyML/Tabby) | Private code completion | [![License](https://img.shields.io/github/license/TabbyML/Tabby.svg)](https://github.com/TabbyML/Tabby) |
| **Codeium** | Free AI code completion | [![GitHub stars](https://img.shields.io/github/stars/Exafunction/codeium.vim?style=social)](https://github.com/Exafunction/codeium.vim) | Vim integration | [![License](https://img.shields.io/github/license/Exafunction/codeium.vim.svg)](https://github.com/Exafunction/codeium.vim); hosted service ⚠️ |
| **Claude Code** | Agentic coding tool, included as a proprietary benchmark | [![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-code?style=social)](https://github.com/anthropics/claude-code) | Terminal coding agent | Proprietary, API Only ⚠️ |

<a id="rag"></a>
## 🔍 RAG & Document AI

| Project | Description | GitHub stars | Key feature | License |
|---|---|---|---|---|
| **RAGFlow** | Enterprise-grade RAG with deep document understanding | [![GitHub stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social)](https://github.com/infiniflow/ragflow) | Layout-aware parsing | [![License](https://img.shields.io/github/license/infiniflow/ragflow.svg)](https://github.com/infiniflow/ragflow) |
| **Mem0** | Universal memory layer for AI agents | [![GitHub stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social)](https://github.com/mem0ai/mem0) | Persistent agent memory | [![License](https://img.shields.io/github/license/mem0ai/mem0.svg)](https://github.com/mem0ai/mem0) |
| **PrivateGPT** | Private document Q&A | [![GitHub stars](https://img.shields.io/github/stars/zylon-ai/private-gpt?style=social)](https://github.com/zylon-ai/private-gpt) | Local retrieval | [![License](https://img.shields.io/github/license/zylon-ai/private-gpt.svg)](https://github.com/zylon-ai/private-gpt) |
| **Kotaemon** | RAG-based document chat | [![GitHub stars](https://img.shields.io/github/stars/Cinnamon/kotaemon?style=social)](https://github.com/Cinnamon/kotaemon) | Visual document QA | [![License](https://img.shields.io/github/license/Cinnamon/kotaemon.svg)](https://github.com/Cinnamon/kotaemon) |
| **Quivr** | Opinionated RAG for applications | [![GitHub stars](https://img.shields.io/github/stars/QuivrHQ/quivr?style=social)](https://github.com/QuivrHQ/quivr) | Knowledge assistants | [![License](https://img.shields.io/github/license/QuivrHQ/quivr.svg)](https://github.com/QuivrHQ/quivr) |
| **RAG Techniques** | Collection of advanced RAG methods | [![GitHub stars](https://img.shields.io/github/stars/NirDiamant/RAG_Techniques?style=social)](https://github.com/NirDiamant/RAG_Techniques) | Practical notebooks | [![License](https://img.shields.io/github/license/NirDiamant/RAG_Techniques.svg)](https://github.com/NirDiamant/RAG_Techniques) |

<a id="image"></a>
## 🎨 Image Generation

| Project | Description | GitHub stars | License | Hosting |
|---|---|---|---|---|
| **ComfyUI** | Node-based visual workflow builder | [![GitHub stars](https://img.shields.io/github/stars/comfyanonymous/ComfyUI?style=social)](https://github.com/comfyanonymous/ComfyUI) | [![License](https://img.shields.io/github/license/comfyanonymous/ComfyUI.svg)](https://github.com/comfyanonymous/ComfyUI) | Self-Hostable ✅ |
| **Stable Diffusion WebUI (AUTOMATIC1111)** | Mature Stable Diffusion interface | [![GitHub stars](https://img.shields.io/github/stars/AUTOMATIC1111/stable-diffusion-webui?style=social)](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | [![License](https://img.shields.io/github/license/AUTOMATIC1111/stable-diffusion-webui.svg)](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Self-Hostable ✅ |
| **Fooocus** | Easy offline image generator | [![GitHub stars](https://img.shields.io/github/stars/lllyasviel/Fooocus?style=social)](https://github.com/lllyasviel/Fooocus) | [![License](https://img.shields.io/github/license/lllyasviel/Fooocus.svg)](https://github.com/lllyasviel/Fooocus) | Self-Hostable ✅ |
| **InvokeAI** | Professional creative tools | [![GitHub stars](https://img.shields.io/github/stars/invoke-ai/InvokeAI?style=social)](https://github.com/invoke-ai/InvokeAI) | [![License](https://img.shields.io/github/license/invoke-ai/InvokeAI.svg)](https://github.com/invoke-ai/InvokeAI) | Self-Hostable ✅ |
| **SUPIR** | Real-world image restoration | [![GitHub stars](https://img.shields.io/github/stars/Fanghua-Yu/SUPIR?style=social)](https://github.com/Fanghua-Yu/SUPIR) | [![License](https://img.shields.io/github/license/Fanghua-Yu/SUPIR.svg)](https://github.com/Fanghua-Yu/SUPIR) | Self-Hostable ✅ |

<a id="video"></a>
## 🎬 Video Generation

| Project | Description | GitHub stars | License | Hosting |
|---|---|---|---|---|
| **LatentSync** | Lip sync for video | [![GitHub stars](https://img.shields.io/github/stars/bytedance/LatentSync?style=social)](https://github.com/bytedance/LatentSync) | [![License](https://img.shields.io/github/license/bytedance/LatentSync.svg)](https://github.com/bytedance/LatentSync) | Self-Hostable ✅ |
| **MoneyPrinterPlus** | AI short video generation | [![GitHub stars](https://img.shields.io/github/stars/ddean2009/MoneyPrinterPlus?style=social)](https://github.com/ddean2009/MoneyPrinterPlus) | [![License](https://img.shields.io/github/license/ddean2009/MoneyPrinterPlus.svg)](https://github.com/ddean2009/MoneyPrinterPlus) | Self-Hostable ✅ |

<a id="voice"></a>
## 🗣️ Voice & Audio

| Project | Description | GitHub stars | License | Hosting |
|---|---|---|---|---|
| **GPT-SoVITS** | Voice conversion and cloning | [![GitHub stars](https://img.shields.io/github/stars/RVC-Boss/GPT-SoVITS?style=social)](https://github.com/RVC-Boss/GPT-SoVITS) | [![License](https://img.shields.io/github/license/RVC-Boss/GPT-SoVITS.svg)](https://github.com/RVC-Boss/GPT-SoVITS) | Self-Hostable ✅ |
| **ChatTTS** | Conversational text-to-speech | [![GitHub stars](https://img.shields.io/github/stars/2noise/ChatTTS?style=social)](https://github.com/2noise/ChatTTS) | [![License](https://img.shields.io/github/license/2noise/ChatTTS.svg)](https://github.com/2noise/ChatTTS) | Self-Hostable ✅ |
| **CosyVoice** | Multilingual voice generation | [![GitHub stars](https://img.shields.io/github/stars/FunAudioLLM/CosyVoice?style=social)](https://github.com/FunAudioLLM/CosyVoice) | [![License](https://img.shields.io/github/license/FunAudioLLM/CosyVoice.svg)](https://github.com/FunAudioLLM/CosyVoice) | Self-Hostable ✅ |
| **MockingBird** | Five-second voice cloning | [![GitHub stars](https://img.shields.io/github/stars/babysor/MockingBird?style=social)](https://github.com/babysor/MockingBird) | [![License](https://img.shields.io/github/license/babysor/MockingBird.svg)](https://github.com/babysor/MockingBird) | Self-Hostable ✅ |
| **Sesame CSM** | Conversational speech model | [![GitHub stars](https://img.shields.io/github/stars/SesameAILabs/csm?style=social)](https://github.com/SesameAILabs/csm) | [![License](https://img.shields.io/github/license/SesameAILabs/csm.svg)](https://github.com/SesameAILabs/csm) | Self-Hostable ✅ |
| **VoiceStar** | Duration-controllable TTS | [![GitHub stars](https://img.shields.io/github/stars/jasonppy/VoiceStar?style=social)](https://github.com/jasonppy/VoiceStar) | [![License](https://img.shields.io/github/license/jasonppy/VoiceStar.svg)](https://github.com/jasonppy/VoiceStar) | Self-Hostable ✅ |

<a id="local"></a>
## 🏠 Local Deployment & Inference

| Project | Description | GitHub stars | License | Hosting |
|---|---|---|---|---|
| **Ollama** | Docker-like experience for running LLMs | [![GitHub stars](https://img.shields.io/github/stars/ollama/ollama?style=social)](https://github.com/ollama/ollama) | [![License](https://img.shields.io/github/license/ollama/ollama.svg)](https://github.com/ollama/ollama) | Self-Hostable ✅ |
| **Open WebUI** | ChatGPT-like self-hosted UI | [![GitHub stars](https://img.shields.io/github/stars/open-webui/open-webui?style=social)](https://github.com/open-webui/open-webui) | [![License](https://img.shields.io/github/license/open-webui/open-webui.svg)](https://github.com/open-webui/open-webui) | Self-Hostable ✅ |
| **llama.cpp** | GGUF quantization and edge inference | [![GitHub stars](https://img.shields.io/github/stars/ggerganov/llama.cpp?style=social)](https://github.com/ggerganov/llama.cpp) | [![License](https://img.shields.io/github/license/ggerganov/llama.cpp.svg)](https://github.com/ggerganov/llama.cpp) | Self-Hostable ✅ |
| **vLLM** | High-throughput LLM serving | [![GitHub stars](https://img.shields.io/github/stars/vllm-project/vllm?style=social)](https://github.com/vllm-project/vllm) | [![License](https://img.shields.io/github/license/vllm-project/vllm.svg)](https://github.com/vllm-project/vllm) | Self-Hostable ✅ |
| **LocalAI** | OpenAI API drop-in replacement | [![GitHub stars](https://img.shields.io/github/stars/mudler/LocalAI?style=social)](https://github.com/mudler/LocalAI) | [![License](https://img.shields.io/github/license/mudler/LocalAI.svg)](https://github.com/mudler/LocalAI) | Self-Hostable ✅ |
| **GPT4All** | No-code desktop AI | [![GitHub stars](https://img.shields.io/github/stars/nomic-ai/gpt4all?style=social)](https://github.com/nomic-ai/gpt4all) | [![License](https://img.shields.io/github/license/nomic-ai/gpt4all.svg)](https://github.com/nomic-ai/gpt4all) | Self-Hostable ✅ |
| **Jan** | Polished desktop local AI experience | [![GitHub stars](https://img.shields.io/github/stars/janhq/jan?style=social)](https://github.com/janhq/jan) | [![License](https://img.shields.io/github/license/janhq/jan.svg)](https://github.com/janhq/jan) | Self-Hostable ✅ |

### Recommended Model + Tool Combinations

- **Beginner:** Gemma 4 12B + Ollama + Open WebUI
- **Developer:** Qwen3.6 + Continue + Ollama
- **Enterprise:** DeepSeek V4 + vLLM + RAGFlow
- **Edge:** Phi-4 Reasoning + llama.cpp + Jan

<a id="nocode"></a>
## 🔧 No-Code / Low-Code AI Platforms

| Project | Description | GitHub stars | License | MCP | Hosting |
|---|---|---|---|---|---|
| **n8n** | Workflow automation with AI nodes | [![GitHub stars](https://img.shields.io/github/stars/n8n-io/n8n?style=social)](https://github.com/n8n-io/n8n) | [![License](https://img.shields.io/github/license/n8n-io/n8n.svg)](https://github.com/n8n-io/n8n) | Integrations available | Self-Hostable ✅ |
| **Langflow** | Visual builder for AI agents | [![GitHub stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=social)](https://github.com/langflow-ai/langflow) | [![License](https://img.shields.io/github/license/langflow-ai/langflow.svg)](https://github.com/langflow-ai/langflow) | ✅ Supported | Self-Hostable ✅ |
| **Dify** | Full-stack AI application platform | [![GitHub stars](https://img.shields.io/github/stars/langgenius/dify?style=social)](https://github.com/langgenius/dify) | [![License](https://img.shields.io/github/license/langgenius/dify.svg)](https://github.com/langgenius/dify) | ✅ Supported | Self-Hostable ✅ |
| **AnythingLLM** | All-in-one AI platform | [![GitHub stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=social)](https://github.com/Mintplex-Labs/anything-llm) | [![License](https://img.shields.io/github/license/Mintplex-Labs/anything-llm.svg)](https://github.com/Mintplex-Labs/anything-llm) | ✅ Supported | Self-Hostable ✅ |
| **LibreChat** | Multi-provider ChatGPT clone | [![GitHub stars](https://img.shields.io/github/stars/danny-avila/LibreChat?style=social)](https://github.com/danny-avila/LibreChat) | [![License](https://img.shields.io/github/license/danny-avila/LibreChat.svg)](https://github.com/danny-avila/LibreChat) | ✅ Supported | Self-Hostable ✅ |
| **Flowise** | No-code LLM app builder | [![GitHub stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social)](https://github.com/FlowiseAI/Flowise) | [![License](https://img.shields.io/github/license/FlowiseAI/Flowise.svg)](https://github.com/FlowiseAI/Flowise) | Check current release | Self-Hostable ✅ |

<a id="observability"></a>
## 📊 Observability & Monitoring

| Project | Description | GitHub stars | License | Hosting |
|---|---|---|---|---|
| **Langfuse** | LLM engineering and tracing platform | [![GitHub stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social)](https://github.com/langfuse/langfuse) | [![License](https://img.shields.io/github/license/langfuse/langfuse.svg)](https://github.com/langfuse/langfuse) | Self-Hostable ✅ |
| **Phoenix** | AI observability and evaluation | [![GitHub stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social)](https://github.com/Arize-ai/phoenix) | [![License](https://img.shields.io/github/license/Arize-ai/phoenix.svg)](https://github.com/Arize-ai/phoenix) | Self-Hostable ✅ |
| **Helicone** | Open-source LLM observability | [![GitHub stars](https://img.shields.io/github/stars/Helicone/helicone?style=social)](https://github.com/Helicone/helicone) | [![License](https://img.shields.io/github/license/Helicone/helicone.svg)](https://github.com/Helicone/helicone) | Self-Hostable ✅ |

<a id="quickstart"></a>
## ⚡ Quick Start Guides

### Docker All-in-One

```bash
# Ollama + Open WebUI
docker run -d -p 3000:8080 --gpus all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

### Install Ollama + Run Latest Models

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run gemma4:12b
ollama run qwen3.6
ollama run phi4-reasoning
```

### Self-Hosted API (LocalAI)

```bash
docker run -p 8080:8080 --gpus all localai/localai:latest-aio-gpu-nvidia-cuda-12
```

<a id="license"></a>
## 📜 License

The contents of this directory are licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Please give appropriate credit and indicate changes. Individual projects retain their own licenses, shown where known.

## 🤝 Contributing

Suggestions, corrections, and new alternatives are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the curation and verification rules.
