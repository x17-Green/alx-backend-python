# 0x00. Python - Variable Annotations 
### Description
This project is about variable annotations in Python. It covers the basics of variable annotations, how to use them, and how to use them with type checkers.

### Concepts

_For this project, we expect you to look at this concept:_
- [Advanced Python](https://intranet.alxswe.com/concepts/554)

![](https://i.redd.it/y9y25tefi5401.png)

## Resources
**Read or watch**:

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html "Python 3 typing documentation")
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html "MyPy cheat sheet")

## Learning Objectives

### General

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"), **without the help of Google**:

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks, Files & Description
### 0. Basic annotations - add
- File: [`0-add.py`](./0-add.py "0-add.py")
- [x] Task: Write a type-annotated function `add`
	- Takes two float arguments
		- `a`: (Float)
		- `b`: (Float)
	- Returns:
		- `sum`: (Float)
- Example Execution: ([`0-main.py`](./0-main.py "0-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 0-main.py 
    #!/usr/bin/env python3
    add = __import__('0-add').add

    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
    ╭─green@greenhouse 
    ╰─➤  ./0-main.py 
    True
    {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 1. Basic annotations - concat
- File: [`1-concat.py`](./1-concat.py "1-concat.py")
- [x] Task: Write a type-annotated function `concat`
	- Takes two float arguments
		- `str1`: (String)
		- `str2`: (String)
	- Returns:
		- Concatenated `str1 + str2`: (String)
- Example Execution: ([`1-main.py`](./1-main.py "1-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 1-main.py 
    #!/usr/bin/env python3
    concat = __import__('1-concat').concat

    str1 = "egg"
    str2 = "shell"

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)

    ╭─green@greenhouse 
    ╰─➤  ./1-main.py 
    True
    {'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 2. Basic annotations - floor
- File: [`2-floor.py`](./2-floor.py "2-floor.py")
- [x] Task: Write a type-annotated function `floor`
	- Takes a float argument
		- `n`: (Float)
    - Returns:
	    - `floor` of (Float)
- Example Execution: ([`2-main.py`](./2-main.py "2-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 2-main.py
    #!/usr/bin/env python3

    import math

    floor = __import__('2-floor').floor

    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

    ╭─green@greenhouse 
    ╰─➤  ./2-main.py
    True
    {'n': <class 'float'>, 'return': <class 'int'>}
    floor(3.14) returns 3, which is a <class 'int'>
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 3. Basic annotations - to string 
- File: [`3-to_str.py`](./3-to_str.py "3-to_str.py")
- [x] Task: Write a type-annotated function `to_str`
    - Takes a float argument
      - `n`: (Float)
    - Returns:
      - `string` of `n`: (Float)
- Example Execution: ([`3-main.py`](./3-main.py "3-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 3-main.py 
    #!/usr/bin/env python3
    to_str = __import__('3-to_str').to_str

    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

    ╭─green@greenhouse 
    ╰─➤  ./3-main.py  
    True
    {'n': <class 'float'>, 'return': <class 'str'>}
    to_str(3.14) returns 3.14 which is a <class 'str'>
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 4. Define variables 
- File: [`4-define_variables.py`](./4-define_variables.py "4-define_variables.py")
- [x] Task: Define the following variables with the specified values and type
    - `a`: (Int) = 1
    - `pi`: (Float) = 3.14
    - `i_understand_annotations`: (Boolean) = True
    - `school`: (String) = "Holberton"
- Example Execution: ([`4-main.py`](./4-main.py "4-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 4-main.py 
    #!/usr/bin/env python3

    a = __import__('4-define_variables').a
    pi = __import__('4-define_variables').pi
    i_understand_annotations = __import__('4-define_variables').i_understand_annotations
    school = __import__('4-define_variables').school

    print("a is a {} with a value of {}".format(type(a), a))
    print("pi is a {} with a value of {}".format(type(pi), pi))
    print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
    print("school is a {} with a value of {}".format(type(school), school))

    ╭─green@greenhouse 
    ╰─➤  ./4-main.py 
    a is a <class 'int'> with a value of 1
    pi is a <class 'float'> with a value of 3.14
    i_understand_annotations is a <class 'bool'> with a value of True
    school is a <class 'str'> with a value of Holberton
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 5. Complex types - list of floats 
- File: [`5-sum_list.py`](./5-sum_list.py "5-sum_list.py")
- [x] Task: Define a type-annotated function `sum_list` 
    - Takes a list of floats as argument
        - `input_list`: (`list`: Float)
    - Returns:
        - Sum of all the elements in the list as `float`
- Example Execution: ([`5-main.py`](./5-main.py "5-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 5-main.py
    #!/usr/bin/env python3

    sum_list = __import__('5-sum_list').sum_list

    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))

    ╭─green@greenhouse 
    ╰─➤  ./5-main.py 
    True
    {'input_list': typing.List[float], 'return': <class 'float'>}
    sum_list(floats) returns 6.470000000000001 which is a <class 'float'>
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 6. Complex types - mixed list 
- File: [`6-sum_mixed_list.py`](./6-sum_mixed_list.py "6-sum_mixed_list.py")
- [x] Task: Define a type-annotated function `sum_mixed_list`
    - Takes a list of mixed types as argument
        - `sum_mixed_list`: (List: `int`, `float`)
- Example Execution: ([`6-main.py`](./6-main.py "6-main.py"))
	```
	╭─green@greenhouse 
	╰─➤  cat 6-main.py  
	#!/usr/bin/env python3
	
	sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list
	
	print(sum_mixed_list.__annotations__)
	mixed = [5, 4, 3.14, 666, 0.99]
	ans = sum_mixed_list(mixed)
	print(ans == sum(mixed))
	print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
	
	╭─green@greenhouse 
	╰─➤  
	```

### 7. Complex types - string and int/float to tuple 
- File: [`7-to_kv.py`](./7-to_kv.py "7-to_kv.py")
- [x] Task: Define a type-annotated function named `to_kv` 
	- Prototype: `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`
	- Function takes two arguments:
	    - `k`: a string (`str`)
	    - `v`: an integer (`int`) or a float (`float`)
	- The function returns a tuple with two elements:
	    - The first element is string `k` (`str`)
	    - The second element is the square of the value `v`, annotated as a float (`float`)
- Example Execution: ([`7-main.py`](./7-main.py "7-main.py"))
	```
	╭─green@greenhouse 
	╰─➤  cat 7-main.py 
	#!/usr/bin/env python3
	
	to_kv = __import__('7-to_kv').to_kv
	
	print(to_kv.__annotations__)
	print(to_kv("eggs", 3))
	print(to_kv("school", 0.02))
	
	╭─green@greenhouse 
	╰─➤  ./7-main.py
	{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
	('eggs', 9.0)
	('school', 0.0004)
	╭─green@greenhouse 
	╰─➤  
	```

### 8. Complex types - functions 
- File: [`8-is_kind_of_class.py`](./8-is_kind_of_class.py "8-is_kind_of_class.py")
- [x] Task: Define a type-annotated function named `make_multiplier`
    - Prototype: `make_multiplier(multiplier: float) -> callable[[float], float]
    - Function takes one argument:
		- `multiplier`:  (Float)
	- The function returns another function that:
		- Takes one argument: a floating-point number (`float`)
		- Returns the product of the input float and the `multiplier` value
- Example Execution: ([`8-main.py`](./8-main.py "8-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 8-main.py
    #!/usr/bin/env python3

    make_multiplier = __import__('8-make_multiplier').make_multiplier
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))

    ╭─green@greenhouse 
    ╰─➤  ./8-main.py 
    {'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
    4.928400000000001
    ╭─green@greenhouse 
    ╰─➤  
    ```

### 9. Let's duck type an iterable object 
- File: [`9-element_length.py`](./9-element_length.py "9-element_length.py")
- [x] Task: Annotate the function `element_length` with the correct types for its parameters and return values.
	- The function takes one argument:
	    - `lst`: a list of strings (or other sequences) (`list[str]`)
	- The function returns a list of tuples, where each tuple contains:
	    - A string (or other sequence) (`str`)
	    - The length of that string (`int`)
	```
	def element_length(lst):
		return [(i, len(i)) for i in lst]
	```
- Example Execution: ([`9-main.py`](./9-main.py "9-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 9-main.py
    #!/usr/bin/env python3

    element_length =  __import__('9-element_length').element_length

    print(element_length.__annotations__)

    ╭─green@greenhouse 
    ╰─➤  ./9-main.py 
    {'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}

    ╭─green@greenhouse 
    ╰─➤  
    ```

### 10. Duck typing - first element of a sequence 
- File: [`100-safe_first_element.py`](./100-safe_first_element.py "100-safe_first_element.py")
- [x] Task: Augment the following code with the correct duck-typed annotations:
    ```
    # The types of the elements of the input are not know
    def safe_first_element(lst):
        if lst:
            return lst[0]
        else:
            return None
    ```
- Example Execution: ([`100-main.py`](./100-main.py "100-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 100-main.py 
    #!/usr/bin/env python3

    safe_first_element =  __import__('100-safe_first_element').safe_first_element

    print(safe_first_element.__annotations__)

    ╭─green@greenhouse 
    ╰─➤  ./100-main.py 
    {'lst': typing.Sequence[typing.Any], 'return': typing.Optional[typing.Any]}

    ╭─green@greenhouse 
    ╰─➤  
    ```

### 11. More involved type annotations 
- File: [`101-safely_get_value.py`](./101-safely_get_value.py "101-safely_get_value")
- [x] Task: Add type annotations to the function using the `TypeVar` type from the `typing` module.
	```
	def safely_get_value(dct, key, default = None):
	    if key in dct:
	        return dct[key]
	    else:
	        return default
	```
- Example Execution: ([`101-main.py`](./101-main.py "101-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  cat 101-main.py 
    #!/usr/bin/env python3

    safely_get_value = __import__('101-safely_get_value').safely_get_value
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print( ("{}: {}".format(k, v)))

    ╭─green@greenhouse 
    ╰─➤  ./101-main.py 
    Here's what the mappings should look like
    dct: typing.Mapping
    key: typing.Any
    default: typing.Optional[~T]
    return: typing.Union[typing.Any, ~T]

    ╭─green@greenhouse 
    ╰─➤  
    ```

### 12. Type Checking 
- File: [`102-type_checking.py`](./102-type_checking.py "102-type_checking.py")
- [x] Task: Use `mypy` to validate the given piece of code:
    ```
    def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
        zoomed_in: Tuple = [
            item for item in lst
            for i in range(factor)
        ]
        return zoomed_in


    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3.0)
    ```
- Example Execution: ([`102-main.py`](./102-main.py "102-main.py"))
    ```
    ╭─green@greenhouse 
    ╰─➤  mypy 102-type_checking.py 
    Success: no issues found in 1 source file
    ╭─green@greenhouse 
    ╰─➤  cat 102-main.py 
    #!/usr/bin/env python3

    zoom_array =  __import__('102-type_checking').zoom_array

    print(zoom_array.__annotations__)

    ╭─green@greenhouse 
    ╰─➤  ./102-main.py 
    {'lst': typing.Tuple, 'factor': <class 'int'>, 'return': typing.List}
    ```