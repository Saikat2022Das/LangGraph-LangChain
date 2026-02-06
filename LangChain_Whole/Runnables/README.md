

# LCEM — LangChain Expression Language

**LCEM (LangChain Expression Language)** is a concise, composable way to build LangChain pipelines using a pipe-style syntax.  
It allows you to express chains as readable dataflows instead of deeply nested function calls.

---

## Core Idea

A `RunnableSequence` can be written using the pipe (`|`) operator:

```python
prompt | model | parser
```

## Here I hands on all Runnable Objects.
### from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

### from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableBranch,
    RunnableLambda,
)


