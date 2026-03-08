# AI Engineering Path: Learn → Build

> **Where you are now:** You can call LLMs via Python.
> **How to use this:** Learn the concept from the resource → pick 1-2 projects → build and deploy.

---

## 1. RAG (Retrieval Augmented Generation)

**Learn from:** Your YouTube RAG Crash Course (2 hrs) + [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)

**Build:**
- 🔥 **Enterprise RAG with Ollama** — company uploads internal docs, everything runs locally (Ollama + ChromaDB), no data leaves the server. Deploy on an Oracle Cloud VM.
- **AI Customer Support Bot** — feed it product docs/FAQs, it answers customer questions with cited sources. Add a Gradio UI, deploy on HuggingFace Spaces.
- **Research Paper Q&A** — upload arxiv papers, ask questions across all of them. Hybrid search (keyword + semantic).

---

## 2. Agents + Tool Calling

**Learn from:** [HuggingFace Agents Course](https://huggingface.co/learn/agents-course/) (Module 1-3)

**Build:**
- 🔥 **AI Travel Planner** — takes destination + dates + budget, searches flights/hotels/activities via APIs, builds a complete itinerary. Multi-tool agent.
- **GitHub Issue Solver** — reads a repo, understands the codebase, suggests fixes for open issues with code snippets.
- **Personal Finance Agent** — connects to bank CSV exports, categorizes spending, answers questions about your finances, gives saving tips.

---

## 3. LangGraph + Multi-Agent Systems

**Learn from:** Your YouTube LangGraph Parts 1 & 3 + [LangGraph Tutorials](https://langchain-ai.github.io/langgraph/tutorials/)

**Build:**
- 🔥 **AI Content Studio** — one agent researches a topic, another writes a blog post, another creates social media posts from it, another generates SEO metadata. Supervisor orchestration.
- **Automated Code Review Pipeline** — PR reviewer agent + security scanner agent + documentation checker agent. Connect to GitHub webhooks.
- **AI Hiring Assistant** — resume screener agent + question generator agent + evaluation agent. Upload JD + resumes → get ranked candidates with interview questions.

---

## 4. Observability + Tracing

**Learn from:** Your YouTube LangGraph Part 2 (LangSmith) + [LangSmith docs](https://docs.smith.langchain.com/)

**Build:**
- Go back to projects from Phases 1-3 → **add LangSmith tracing to all of them**. Screenshot the traces, add to your README. This isn't a separate project — it's a production habit you add to everything.

---

## 5. Memory Systems

**Learn from:** [Mem0 docs](https://docs.mem0.ai/) + [LangGraph Persistence docs](https://langchain-ai.github.io/langgraph/concepts/persistence/)

**Build:**
- 🔥 **AI Study Buddy** — remembers what topics you've covered, what you struggled with, adapts explanations to your level. Long-term memory across sessions.
- **AI Journaling App** — write daily entries, it remembers themes, tracks your mood patterns over time, surfaces insights from past entries.

---

## 6. Evals (Testing AI Systems)

**Learn from:** [Evidently AI LLM Eval Course](https://www.evidentlyai.com/llm-evaluation-course) (free, hands-on Python tutorials)

**Build:**
- 🔥 **Eval suite for your RAG project** — 50+ test cases, measure faithfulness/relevancy/correctness with RAGAS, automate with pytest. Show scores in a dashboard.
- **Prompt A/B Testing Tool** — input two prompt variants, run both against test cases, compare which performs better with metrics. Deploy on HuggingFace Spaces.

---

## 7. FastAPI + React (for full-stack AI apps)

**Learn from:** [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) (first 5 sections) + [React Quick Start](https://react.dev/learn) (one page)

**Build:**
- Go back to your best project from above → **add a FastAPI backend + React frontend** → deploy (backend on Render, frontend on Vercel). This transforms a script into a product.

---

## 8. Fine-Tuning (use Colab for this)

**Learn from:** [mlabonne/llm-course](https://github.com/mlabonne/llm-course) — follow the fine-tuning Colab notebooks

**Build:**
- 🔥 **Domain-specific expert model** — pick a niche (code review, legal, medical Q&A), curate 500+ examples, fine-tune with LoRA using Unsloth, evaluate base vs fine-tuned. Publish model on HuggingFace Hub.
- **Custom writing style model** — fine-tune a model to write in a specific tone/style. DPO to align preferences. Deploy demo on HuggingFace Spaces.

---

## The Order

```
1. RAG                    ← most in-demand skill, start here
2. Agents + Tools         ← second most in-demand
3. LangGraph + Multi-Agent
4. Observability          ← add to all previous projects
5. Memory
6. Evals                  ← add to your RAG project
7. FastAPI + React        ← upgrade your best project to full-stack
8. Fine-Tuning            ← Colab only
```

> [!TIP]
> **Pick the 🔥 project from each section** — those are the ones that will get you noticed and are closest to what companies actually pay for.

## Deploy & Share

| What | Where |
|------|-------|
| AI demos | [HuggingFace Spaces](https://huggingface.co/spaces) |
| React frontends | [Vercel](https://vercel.com) |
| FastAPI backends | [Render](https://render.com) |
| Fine-tuned models | [HuggingFace Hub](https://huggingface.co) |
| Full VMs | [Oracle Cloud Free Tier](https://www.oracle.com/cloud/free/) |

After every project: **record a demo, post on X + LinkedIn, share the live link.** A deployed product beats a GitHub repo every time.
