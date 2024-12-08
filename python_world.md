# The Unknown Side of Python

*By: Ahmed Mohamed*

![Python in Attack Mode](python_cartoon.png){width=200px}

Today, I spent some time learning about some fundamentals about Python...

No, I'm not talking about what a `for` loop is, or what the `try...except` block does! I was mostly learning about how Python figures out what value is a name referring to. 

Don't get me? Let me show you.

## Example 1: Rebound Variables

Consider the following code:

```python
name = "Guido"

def print_name():
    print(name)
    
name = "Ahmed"

print_name()
```

What is the output gonna be? Is it:

A)  "Guido"

B)  "Ahmed"

<br>

***Hint:***

The variable `name` exists in `print_name`'s outer scope. As such, the function `print_name` only looks up the value of `name` when the function is called. 

***Answer:***

Since we call `print_name` after we bind `name` to `"Ahmed"`, this means that the output will, understandably, be `"Ahmed"`!

---

Pretty easy, eh? All we had to do was figure 


