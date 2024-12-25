# The Lesser Known Side of Python

_By: Ahmed Mohamed_

<figure>

<image src="images/python_cartoon.png" alt="scary cartoon python" width=250>

<figcaption>
Figure 1: Python in Attack Mode
</figcaption>

</figure>

<br>

Today, I spent some time learning some Python fundamentals...

No, I'm not talking about what a `for` loop is, or what the `try...except` block does! I was mostly learning about how Python figures out the value that a name references.

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

A) "Guido"

B) "Ahmed"

<br>

**_Hint:_**

The variable `name` exists in `print_name`'s outer scope. As such, the function `print_name` only looks up the value of `name` when the function is called.

**_Answer:_**

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

**_Answer:_**

In the beginning, both `lst_A` and `lst_B` refer to `[]`. We then _rebind_ `lst_A` to `[] + [1]`, which evaluates to `[1]`. This means that we're changing what `lst_A` refers to, but we're not _mutating_ the original, empty list! So, `lst_B` still refers to `[]`.

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

**_Hint:_**

It's not A...⁉️

**_Answer_**

Conceptually, we think of `A += B` as `A = A + B`. But, in Python, this is only true for immutable types!

In this case, the line `lst_A += [1]` is actually evaluated as `lst_A = lst_A.__iadd__([1])`. The **pseudocode** for the dunder method `__iadd__` looks like this:

```python
# pseudocode!
class List:
    def __iadd__(self, other):
        self.extend(other)
        return self
```

Yes, that's right! The `+=` first _extends_ the list with the iterable. Then, the list is simply rebound (past tense of rebind) back to itself. It's functionally equivalent to doing:

```python
lst_A.extend([1])
lst_A = lst_A
```

> Note: This example was taken from Ned Batchelder's presentation at PyCon 2015! Click [here][pycon-2015] to watch it.

In the previous example with `lst_A = lst_A + [1]`, Python used the dunder method `__add__` (not `__iadd__`), which does not mutate the value of `lst_A` in place.

The reason we don't have to think about the `+=` operator with immutable types (like `int`) is because they're immutable! You cannot mutate the value that they reference. So, using the `+=` with immutable types will bind a variable to the `other` value.

---

Before we continue, I should note that these examples are _intended_ to mess you up. They definitely don't mean that you're bad at Python! They're just a series of lesser-known Pythonic fundamentals that might help you in your next debugging session! 💪

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

**_Answer:_**

In Python, default arguments are only assigned once! They're not rebound (again, past tense of rebind!) every time a function is called.

So, the first time we called the function `make_scary`, the default argument was appended with `"Argghh! Gimme your gold!!"`. Then, that same default argument was appened again when we called `make_scary` a second time!.

Thus, the correct answer was Option B! 🦜🏴‍☠️

> Note: This example, along with the following one, were both taken from _The Hitchhiker's Guide to Python_. Check it out [here][hitch]!

---

Alright, alright... I think we're really digging into mutability here! Why don't we step out into something a bit more pythonic... inner functions!

## Example 4: The Inner World of Inner Functions

Python lets you define functions inside other functions. Take a look:

```python
def get_cakes():
    bakery = ['🧑‍🍳'] * 3

    def bake_cakes():
        cakes = ['🍰' for baker in bakery]
        return cakes

    return bake_cakes()

print(get_cakes())
```

Similarly to regular functions, we can call inner functions as long as they've been defined first. Moreover, just like we saw in [Example 1](#example-1-rebound-variables), inner functions access the values they need when they're called, and not when the inner function is defined.

This gets a little interesting when we return inner functions!

Take a look at the following example:

```python
def get_bakery(cakes_needed: int):
    bakers = ['🧑‍🍳'] * cakes_needed

    def bake_cakes():
        cakes = ['🍰' for baker in bakers]
        return cakes

    # job layoffs (˘･_･˘)
    try:
        bakers.pop()
    except IndexError:
        print("We don't even have bakers to layoff...")

    return bake_cakes

bakery = get_bakery(3)
print(bakery())
```

If you've understood [Example 1](#example-1-rebound-variables), then you'd know that the output will be:

`['🍰', '🍰']`

That's because the function `make_cakes` is only being called _after_ we pop off one of the bakers. So, when the value of `bakers` is looked up, it will roughly refer to the value of `['🧑‍🍳', '🧑‍🍳']`. As such, only 2 🍰 will be generated.

But what if we call the function multiple times...

Take a look at the final example in this section:

```python
def get_bakery(cakes_needed: int):
    bakers = ['🧑‍🍳'] * cakes_needed

    def make_cakes():
        cakes = ['🍰' for baker in bakers]
        return cakes

    # job layoffs (˘･_･˘)
    try:
        bakers.pop()
    except IndexError:
        print("We don't even have bakers to layoff...")

    return make_cakes

mini_bakery = get_bakery(3)
big_bakery = get_bakery(6)

print(mini_bakery())
```

What will the output be? Pick an option!

A) `['🍰', '🍰']`

B) `['🍰', '🍰', '🍰']`

C) `['🍰', '🍰', '🍰', '🍰', '🍰']`

D) `['🍰', '🍰', '🍰', '🍰', '🍰', '🍰']`

<br>

**_Answer:_**

If you guessed **A**, you're correct! But, how does `mini_bakery` still reference the old value of `bakers`, even if it was seemingly changed by `big_bakery`??

This is where **closures** come into play!

We know that the inner function `make_cakes` references variables in its enclosing (surrounding) scope! We also know that after we returned back an instance of `make_cakes`, it was able to access its own copy of variables in its enclosing scope.

This means that the `make_cakes` instance we returned was a closure!

To quote the website [Real Python][real-py-clo]:

> The closure isn’t the inner function itself but the inner function along with its enclosing environment. The closure captures the local variables and name in the containing function and keeps them around.

In the previous example, we know that `mini_bakery` references the closure created from `make_cakes`, and its enclosing environment. In this case, its enclosing environment contained a distinct copy of `bakers`. So, when was we call `mini_bakery`, we're using the copy of `bakers` that existed when the closure was created, which was: `['🧑‍🍳', '🧑‍🍳']`.

In other words, the closures that `mini_bakery` and `big_bakery` reference have different copies of `bakers`. So, calling `mini_bakery` will output `['🍰', '🍰']`.

That's why **A** is correct!! 🥳

## Concluding Away...

Hope you enjoyed these series of problems! To reiterate, these questions were meant to trick you, so they are not an indication of a lack of skill!

If you learned something, great! Here's a final problem that tries to combine all of the material from the previous sections. Feel free to give it a go, or send it to a friend and watch them fall into anguish! 😁

### Aladdin and Jasmine's Trip to the Cave...

```python
# Aladdine and Jasmine share gold_coins!
gold_coins = ['🪙']
aladdins_coins = gold_coins
jasmines_coins = gold_coins

def genie_lamp(gold_bag: list = []):

    def genie():
        # (used to access and reassign gold_bag)
        nonlocal gold_bag

        # the genie gives us a gold_bag!
        gold_bag += ['🪙']
        gold_coins.extend(gold_bag)

    return genie

# Aladdin finds a gold coin when exploring a cave...
aladdins_coins += ['🪙']

# Aladdin and Jasmine find a genie_lamp, and they rub it to get a blue_genie!
blue_genie = genie_lamp()

# blue_genie grants each of them 1 wish
blue_genie()
blue_genie()

# Aladdin finds another coin as he leaves the cave
aladdins_coins = aladdins_coins + ['🪙']

# how many coins does jasmine have?
print(jasmines_coins)
```

What's the output that we shall expect to see? Run the program to check your answer!!

👋

<!--Source Links-->

[pycon-2015]: https://www.youtube.com/watch?v=_AEJHKGk9ns
[hitch]: https://docs.python-guide.org/writing/gotchas/
[real-py-clo]: https://realpython.com/inner-functions-what-are-they-good-for/#:~:text=The%20closure%20isn't%20the,function%20and%20keeps%20them%20around.
