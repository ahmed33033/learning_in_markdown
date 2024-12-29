# What's this about?

LangGraph's state-graph architecture is interesting. It allows end-users (like us) to compose AI applications out of _nodes and edges_. Nodes contain a regular function at their heart. Nodes take the output of a function and pass it along the graph's edges. These outputs then serve as the inputs of other nodes. The LangGraph glossary says it's "inspired by Google's Pregel System".

I found a bug a few months ago, and I later submitted an [issue on Github][git-issue]. The bug was verified by LangChain engineers. The bug still exists as of the current version of LangGraph. I thought it could be a cool way to contribute to open-source (and beef up my resume) by fixing the bug.

So, this learning path is an attempt at gaining a better understanding of LangGraph's state-graph architecture.

<!--Links-->

[git-issue]: https://github.com/langchain-ai/langgraph/issues/2504
