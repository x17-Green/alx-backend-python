# 0x02. Python - Async Comprehension
### Project Description
This project is about asynchronous comprehensions in Python. It involves creating a program that uses asynchronous comprehensions to fetch data from a URL and then process the data.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/ee85b9f67c384e29525b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240806%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240806T115425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2a963d8e22b2d9669fcbb5e6a0d848a1148c9d60a26554103a64b02873f928ab)

## Resources

**Read or watch**:

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/ "PEP 530 -- Asynchronous Comprehensions")
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/ "What’s New in Python: Asynchronous Comprehensions / Generators")
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3 "Type-hints for generators")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/_jK22HqiCeh5NjKJ4ZHBww "explain to anyone"), **without the help of Google**:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

### Tasks, Files & Description
### 0. Async Generator
- File: [`0-async_generator.py`](./0-async_generator.py "0-async_generator.py")
- [x] Task: Implement the `async_generator` coroutine with the following specifications:
	- Takes no arguments
	- Loops 10 times, performing the following actions on each iteration:
	    - Asynchronously waits for 1 second
	    - Yields a random number between 0 and 10 (inclusive) using the `random` module
- Example Execution: ([`0-main.py`](./0-main.py "0-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 0-main.py 
    #!/usr/bin/env python3

    import asyncio

    async_generator = __import__('0-async_generator').async_generator

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
    ╭─green@greenhouse 
    ╰─➤  ./0-main.py
    [2.018700910474718, 4.775486313111395, 1.6940470664422136, 8.953690480774315, 6.013884069585254, 7.8502592240651055, 6.534399779687323, 4.485440533373559, 8.290247687262838, 0.3515917957562431]
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 1. Async Comprehensions
- File: [`1-async_comprehension.py`](./1-async_comprehension.py "1-async_comprehension.py")
- [x] Task: Implement the `async_comprehension` coroutine with the following specifications:
	- Imports and utilizes the `async_generator` coroutine from the previous task
	- Takes no arguments
	- Uses an asynchronous comprehension to collect 10 random numbers from `async_generator`
	- Returns the list of 10 collected random numbers
- Example Implementation: ([`1-main.py`](./1-main.py "1-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 1-main.py
    #!/usr/bin/env python3

    import asyncio

    async_comprehension = __import__('1-async_comprehension').async_comprehension


    async def main():
        print(await async_comprehension())

    asyncio.run(main())

    ╭─green@greenhouse 
    ╰─➤  ./1-main.py 
    [8.931384904902714, 2.2045355903843946, 2.8114379414544977, 0.744205703591414, 5.963635733816121, 2.704494981402167, 4.0001991033891695, 6.986255803168482, 1.603244979009929, 1.1699399575980274]
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 2. Run time for four parallel comprehensions
- File: [`2-measure_runtime.py`](./2-measure_runtime.py "2-measure_runtime.py")
- [x] Task: Implement the `measure_runtime` coroutine with the following specifications:
    - Import and utilize the `async_comprehension` coroutine from the previous file
    - Execute `async_comprehension` four times in parallel using `asyncio.gather`
    - Measure and return the total runtime of the parallel execution
- Example Execution: ([`2-main.py`](./2-main.py "2-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 2-main.py
    #!/usr/bin/env python3

    import asyncio


    measure_runtime = __import__('2-measure_runtime').measure_runtime


    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )

    ╭─green@greenhouse 
    ╰─➤  ./2-main.py
    10.011858224868774
    ╭─green@greenhouse 
    ╰─➤  
    ```
