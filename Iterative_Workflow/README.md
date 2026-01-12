# Iterative LLM-Powered Tweet Generation and Refinement with LangGraph

<img width="368" height="399" alt="Screenshot from 2026-01-12 18-34-56" src="https://github.com/user-attachments/assets/47df11f7-bc53-414a-9ea8-873da99f744a" />


This notebook demonstrates how to build an autonomous, iterative content generation and refinement system using LangGraph, a library for building stateful, multi-actor applications with LLMs.

## What you will learn:

*   **LangGraph Fundamentals**: Understand how to define a `StateGraph`, add nodes (representing LLM agents or functions), and establish edges to control the flow of execution.
*   **Iterative Workflow Design**: Implement a feedback loop where an initial draft (tweet) is generated, evaluated by a critic LLM, and then optimized based on the feedback, repeating until the content meets specific criteria or a maximum number of iterations is reached.
*   **Multi-Agent Collaboration**: See how multiple Large Language Models (LLMs) can be orchestrated to perform distinct roles:
    *   **Generator LLM**: Creates initial content (e.g., a tweet).
    *   **Evaluator LLM**: Critically assesses the generated content based on predefined rules.
    *   **Optimizer LLM**: Refines the content using the feedback from the evaluator.
*   **Structured Output with Pydantic**: Learn to enforce structured output from LLMs using Pydantic models, ensuring reliable and parseable feedback for downstream processing.
*   **Conditional Routing**: Utilize LangGraph's conditional edges to dynamically route the workflow based on the evaluation result (e.g., `Approved` vs. `Needs_Improvement`).
*   **LLM Integration**: How to integrate Google Gemini models (via LangChain) into a LangGraph workflow.

## Project Overview:

The notebook sets up a workflow for generating a humorous tweet on a given topic. The process involves:

1.  **Generate**: An LLM (acting as a "funny and clever Twitter influencer") creates an initial tweet.
2.  **Evaluate**: Another LLM (acting as a "ruthless Twitter critic") assesses the tweet for humor, originality, virality, and format, providing structured feedback and an `Approved` or `Needs_Improvement` status.
3.  **Optimize**: If the tweet `Needs_Improvement`, a third LLM (acting as a "tweet punch-up artist") re-writes the tweet based on the feedback.
4.  **Loop**: The optimized tweet is then re-evaluated, continuing the cycle until approved or a set number of iterations is reached.

This architecture provides a robust framework for autonomous content creation and quality assurance.
