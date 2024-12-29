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
from multiprocessing import Pool

class Echo:
    def invoke(self, value: Any) -> Any:
        return value

    def stream(self, value: Any) -> Any:
        for chunk in value:
            yield chunk

    def batch(self, args: list[Any]) -> list[Any]:
        with Pool(len(args)) as p:
            outputs = p.map(self.invoke, args)
        return outputs

if __name__ == "__main__":
    echo = Echo()
    print(echo.batch([1,2,3,'hi']))
```

Using LangChain, we can get the same functionality with the following:

```python
from langchain_core.runnables import RunnableLambda

echo = RunnableLambda(lambda value: value)
```

Helps simplifies things a lot!
