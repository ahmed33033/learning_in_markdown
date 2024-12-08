# The Lesser Known Side of Python

*By: Ahmed Mohamed*

<figure>

<image src="python_cartoon.png" alt="scary cartoon python" width=250>

<figcaption>
Figure 1: Python in Attack Mode
</figcaption>

</figure>

Today, I spent some time learning some Python fundamentals...

No, I'm not talking about what a `for` loop is, or what the `try...except` block does! I was mostly learning about how Python figures out the value that a name refers to. 

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

Pretty easy, eh? All we had to do was figure out that the value of `name` that `print_name` was accessing!

 Let's now look at a different example:

## Example 2: List Mutability

Take a look at the following code:

```python
lst_A = []
lst_B = lst_A

lst_A.extend([1])
print(lst_B)
```

What's the output here? If you guessed `[1]`, you're correct! That was even easier than the first example 😁

How about now:
```python
lst_A = []
lst_B = lst_A

lst_A = lst_A + [1]
print(lst_B)
```
What should the output look like? Will we see:

A) `[]`

B) `[1]`

<br>

***Answer:***

In the beginning, both `lst_A` and `lst_B` refer to `[]`. We then *rebind* `lst_A` to `[] + [1]`, which evaluates to `[1]`. This means that we're changing what `lst_A` refers to, but we're not *mutating* the original, empty list! So, `lst_B` still refers to `[]`.

So, Option A was correct! 🙌

Still too easy? How about the final example in this section:

```python
lst_A = []
lst_B = lst_A

lst_A += [1]
print(lst_B)
```
What will the output be? 🤔

A) `[]`

B) `[1]`

<br>

***Hint:***

It's not A...⁉

***Answer***

Conceptually, we think of `A += B` as `A = A + B`. But, in Python, this is only true for immutable types! 

In this case, the line `lst_A += [1]` is actually evaluated as `lst_A = lst_A.__iadd__([1])`. The **pseudocode** for the dunder method `__iadd__` looks like this:

```python
# pseudocode!
class List:
    def __iadd__(self, other):
        self.extend(other)
        return self
```

Yes, that's right! The `+=` first *extends* the list with the iterable. Then, the list is simply rebound (past tense of rebind) back to itself. It's functionally equivalent to doing:

```python
lst_A.extend([1])
lst_A = lst_A
```

> Note: This example was taken from Ned Batchelder's presentation at PyCon 2015! Click [here][pycon-2015] to watch it.

In the previous example with `lst_A = lst_A + [1]`, Python used the dunder method `__add__` (not `__iadd__`), which does not mutate the value of `lst_A` in place.

The reason we don't have to think about the `+=` operator with immutable types (like `int`) is because they're immutable! You cannot mutate the value that they refer to. So, using the `+=` with immutable types will bind a variable to the `other` value.  

---

Before we continue, I should note that these examples are *intended* to mess you up. They definitely don't mean that you're bad at Python! They're just a series of lesser-known Pythonic fundamentals that might help you in your next debugging session! 💪

## Example 3: Another Round of Mutability!

Some of the lesser used features of Python are function default arguments. Let's take a look at what that looks like: 

```python
def parrot(word: str = "Argghh!"):
    print(word)

parrot()
```
Default arguments are used when a particular function parameter does not receive.. well, an argument.

So, when we run the last piece of code, we should see `Argghh!` printed to the console. However, had we instead called the `parrot` function as follows:
```python
parrot("I'm a scarrryy pirate!")
```
The output, as you might expect, should say: `"I'm a scarrryy pirate!"`

Now, what happens if we use a mutable default argument. Let's take a look!

```python
def make_scary(lst: list = []):
    lst.append("Argghh! Gimme your gold!!")
    print(lst)

make_scary()
make_scary()
```
> Note: The double function call is not a misprint.

What will the output be? Pick an option!

A) 
```python
["Argghh! Gimme your gold!!"]
["Argghh! Gimme your gold!!"]
```

<br>

B) 
```python
["Argghh! Gimme your gold!!"]
["Argghh! Gimme your gold!!", "Argghh! Gimme your gold!!"]
```

<br>

***Answer:***

In Python, default arguments are only assigned once! They're not rebound (again, past tense of rebind!) every time a function is called. 

So, the first time we called the function `make_scary`, the default argument was appended with `"Argghh! Gimme your gold!!"`. Then, that same default argument was appened again when we called `make_scary` a second time!. 

Thus, the correct answer was Option B! 🦜🏴‍☠️

> Note: This example, along with the following one, were both taken from *The Hitchhiker's Guide to Python*. Check it out [here][hitch]!
---

Alright, alright... I think we're really digging into mutability here! Why don't we step out into something a bit more pythonic... inner functions!

## Example 4: The Inner World of Inner Functions

Python lets you define functions inside other functions. Take a look:

```python

```
<!--Source Links-->

[pycon-2015]: https://www.youtube.com/watch?v=_AEJHKGk9ns
[hitch]: https://docs.python-guide.org/writing/gotchas/