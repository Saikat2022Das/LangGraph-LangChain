# UPSC Parallel Workflow (summary)

Short description
- This notebook implements a parallel evaluation workflow for an essay using LangGraph + LangChain chat models.

What the workflow does
- Uses `StateGraph` to run three evaluation nodes in parallel: language, analysis, and clarity.
- Each node calls a structured model (`struct_model`) that returns `feedback` and a numeric `score` using a Pydantic `EvaluationSchema`.
- A final node aggregates the feedbacks and computes the average score.

Key implementation details
- Model: initialized with `init_chat_model(model="google_genai:gemini-2.5-flash-lite")` and wrapped with `.with_structured_output(EvaluationSchema)`.
- Each node returns plain Python primitives (str, list, float) so the graph can merge state.
- Important: call model objects with `.invoke(prompt)` (not by calling the model directly) to avoid a `RunnableSequence` TypeError.
- Final evaluation extracts plain text from the model response and safely computes the average (handles empty lists).

How to run
- Set credentials: `GOOGLE_APPLICATION_CREDENTIALS` (service account JSON) or `GOOGLE_API_KEY` in environment.
- Activate the virtualenv and run the notebook or script.

What you can learn
- Building parallel workflows with LangGraph and merging results.
- Using structured outputs (Pydantic) to get typed responses from LLMs.
- Defensive coding with model responses and error handling (quota/errors, non-serializable returns).

Notes and troubleshooting
- If you see `NOT_FOUND` or `RESOURCE_EXHAUSTED` errors, check model name availability and GCP quotas/billing.
- Ensure returned objects are serializable (str/int/float/list/dict) when used in graph state merging.

