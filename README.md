# schnitzel

## A high-level DSL for defining arbitrarily complex UI tests

---
### Overview

UI tests are generally cumbersome to define and maintain, and even more so
to develop usefully complex ones that can serve as both regression
tests and development drivers. Schnitzelscript is intended to be a very 
simple abstraction over Python and webdriver, allowing rapid development
of arbitrarily complex UI tests with strong validation, usable by (technical) 
non- programmers. Here's a quick example that loads a webpage, enters text and 
clicks a button:

```
loadpage "https://www.goodeggs.com"
entertext #username "testpassword"
click #submit
```

As you can see, schnitzelscript comprises commands and 'operands'.
Here's a list of common commands:

- `loadpage`
- `click`
- `entertext`
- `scroll`
- `screenshot`

Schnitzelscript also understands *functions*, inasmuch as you can
label groups of commands to be executed by named invocation:

```
define login:
    loadpage "https://www.goodeggs.com"
    entertext #email "sam.wainwright@goodeggs.com"
    entertext #password "testpassword"
    click #submit
    
login()
```

An important function of UI tests is content/behavior validation.
Schnitzelscript provides a number of ways to perform assertions
with commands:

```
login()

assert-pagename is "market"
```

```
login()

assert-text #banner is "Welcome!"
```

Because the real crux of the complexity of UI tests is *element
identification*, which would generally rely on some type of selector
derived system and thus require extra work/maintenance on the
engineering side, schnitzelscript allows you to identify elements
based on content, context or position as well:

```
entertext input (has-label: "password") "password"
click button (contains-text: "submit")
click button (directly-below: #signup)
click button (color: green, right-of: #logout)
entertext input (directly-below: input (color: green, has-label: "password"))
```

You can also define variables for reuse throughout scripts. These variables
can be strings, numbers, or color hex literals:

```
let label = "label"
let counter = 1
let red = #0xff0000
```

Simple control flow constructs also exist to make some complex
assertions more simple. You can iterate through elements by using
`foreach`:

```
foreach input as i:
    entertext i "hello ${i}"
```

You can also branch conditionally using `if` statements. If statements can
compare two values of the same type, e.g. two strings, two numbers, or two
colors.


Schnitzel supports simple moduling for script organization and uses relative
filepaths by default. You can also set import paths by setting the SCHNITZ_PATH
env var. The loaded modules will execute before the file importing them, so any
function names will be available but any top-level commands will also be run:

```
import ./login.sch
import ./logout.sch as logout  # elect to namespace any imported symbols
import navigate_market.sch  # discovered on SCHNITZ_PATH 
```

For a complete language specification, see [this page](https://www.github.com/budleigh).
