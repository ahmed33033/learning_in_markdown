# LangChain Runnables

🦜🔗🏃‍♂️

## What is it?

Runnables is one of those things that can be best defined by describing what it does, rather than what it is.

A runnable is a foundational object in LangChain that can be:

- invoked: called syncronously
- batched: called in a group simultaneously, syncronously
- streamed: have its output streamed, syncronously
- inspected: return information about its input and output schemas, along with config
- composed: chained together with other runnables

The power of runnables over regular ol' functions is _explictly_ evident in their ability to be composed or chained togher.

Additionally, the power of runnables is _implictly_ evident through the beautiful layer of abstraction that they provide. For example, we can naively implement a set of Runnable methods as follows:

```python
from typing import Any

class Echo:
    def invoke(self, value: Any) -> Any:
        return value

    def stream(self, value: Any) -> Any:
        for chunk in value:
            yield chunk

    def batch(self, args: list[Any]) -> list[Any]:
        outputs = []
        for arg in args:
            outputs.append(self.invoke(arg))
        return args

echo = Echo()
```

Using LangChain, we can get the same functionality with the following:

```python
from langchain_core.runnables import RunnableLambda

echo = RunnableLambda(lambda value: value)
```

Helps simplifies things a lot!
