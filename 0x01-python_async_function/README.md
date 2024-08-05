# 0x01. Python - Async 
### Description
This project is about asynchronous programming in Python. It covers the basics of asynchronous programming, including the use of the asyncio library, coroutines, and tasks.

## Resources

**Read or watch**:

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/ "Async IO in Python: A Complete Walkthrough")
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html "asyncio - Asynchronous I/O")
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform "random.uniform")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"), **without the help of Google**:

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements

### General

- A `README.md` file, at the root of the folder of the project, is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using `wc`
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks, Files & Description
### 0. The basics of async 
- File: [`0-basic_async_syntax.py`](./0-basic_async_syntax.py "0-basic_async_syntax.py")
- Task: Implement the `wait_random` Asynchronous Coroutine
    - Define an async coroutine `wait_random` 
        - Takes one argument 
            - `max_delay`: `int` (default=10)
    - Generate random float delay between 0 and `max_delay` (inclusive) 
          - Using `random` module
    - Wait for the generated delay using `asyncio.sleep`
    - Return the delay value as a float
- Example Execution: ([`0-main.py`](./0-main.py "0-main.py"))
```

```
