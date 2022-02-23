# SheeshLang

```{r}
((((((()))))))
```


## [SHEEEEEEEEESH !!!]
## How to run: 

### Make a virtual environment:
```shell
$ virtualenv venv
```

### Then we activate the virtual environment (if on `linux` or `mac`):

```shell
$ source venv/bin/activate
```
**OR**
(if on `windows`)
```shell
$ ./venv/Scripts/activate
```


### We install the required dependencies for this project:
```shell
$ pip install -r /requirements.txt
```
### Run the following command to run the lexer:
```shell
$ python3 lexer_main.py <filepath>
```
The following command will run the `lexer_main.py` file.
It will print a table of the tokens.


## NOTE
- Each file and funtion in the code is properly documented and commented about its input  arguments, return values and the functionality
- All the keywords, operators and delimeters are defined in the `data.hash_maps.py` file
- The `utils` folder provides with all the utility functions required for the lexer.
- Testcases are provided in the `Testcases` folder. To run each of the testcases run the command:
  ```shell
  $ python3 lexer_main.py Testcases/<filename>
  ```

# Functionalities [updated : 22/02/2022]:

## Lexer phase    
  - 60 keywords.
  - Can distinguish between various datatypes in the lexer phase.
  - Implemented custom keywords like shout
  - distinguishes between string literal, integer literal, float literal and new line character.
  - Gives error on multiline strings and prints each error after reading through the file.
  - Output is properly printed in a table with four categories, namely:
    -  Token line
    -  Token
    -  TOken value
    -  Token Category

# Example:

```shell
$ python3 lexer_main.py Testcases/fact.sheesh
```
```shell
Lexeme seperation successful.
+------------+--------+-------------+----------------+
| Token line | Token  | Token value | Token Category |
+------------+--------+-------------+----------------+
| 1          | int    | 65          | keyword        |
| 1          | fun    | 71          | identifier     |
| 1          | (      | 25          | delimeter      |
| 1          | int    | 65          | keyword        |
| 1          | n      | 72          | identifier     |
| 1          | )      | 26          | delimeter      |
| 1          | {      | 21          | delimeter      |
| 2          | ------ | 70          | new line       |
| 2          | if     | 49          | keyword        |
| 2          | (      | 25          | delimeter      |
| 2          | n      | 72          | identifier     |
| 2          | <=     | 18          | operator       |
| 2          | 1      | 73          | integer_lit    |
| 2          | )      | 26          | delimeter      |
| 2          | {      | 21          | delimeter      |
| 3          | ------ | 70          | new line       |
| 3          | return | 59          | keyword        |
| 4          | 1      | 73          | integer_lit    |
| 4          | ------ | 70          | new line       |
| 4          | }      | 22          | delimeter      |
| 5          | ------ | 70          | new line       |
| 5          | return | 59          | keyword        |
| 5          | n      | 72          | identifier     |
| 5          | *      | 3           | operator       |
| 5          | fact   | 74          | identifier     |
| 5          | (      | 25          | delimeter      |
| 5          | n      | 72          | identifier     |
| 5          | -      | 2           | operator       |
| 5          | 1      | 73          | integer_lit    |
| 5          | )      | 26          | delimeter      |
| 6          | ------ | 70          | new line       |
| 6          | }      | 22          | delimeter      |
| 7          | ------ | 70          | new line       |
| 8          | ------ | 70          | new line       |
| 8          | void   | 75          | identifier     |
| 8          | main   | 76          | identifier     |
| 8          | (      | 25          | delimeter      |
| 8          | void   | 75          | identifier     |
| 8          | )      | 26          | delimeter      |
| 8          | {      | 21          | delimeter      |
| 9          | ------ | 70          | new line       |
| 9          | int    | 65          | keyword        |
| 9          | x      | 77          | identifier     |
| 10         | ------ | 70          | new line       |
| 10         | x      | 77          | identifier     |
| 10         | =      | 14          | operator       |
| 10         | +      | 1           | operator       |
| 10         | 1.3    | 78          | float_lit      |
| 11         | ------ | 70          | new line       |
| 11         | t      | 79          | identifier     |
| 11         | :=     | 11          | operator       |
| 12         | 1      | 73          | integer_lit    |
| 12         | ------ | 70          | new line       |
| 12         | while  | 62          | keyword        |
| 12         | (      | 25          | delimeter      |
| 12         | x      | 77          | identifier     |
| 12         | <=     | 18          | operator       |
| 12         | 10     | 80          | integer_lit    |
| 12         | )      | 26          | delimeter      |
| 12         | {      | 21          | delimeter      |
| 13         | ------ | 70          | new line       |
| 15         | shout  | 60          | keyword        |
| 15         | (      | 25          | delimeter      |
| 15         | x      | 77          | identifier     |
| 15         | )      | 26          | delimeter      |
| 16         | ------ | 70          | new line       |
| 16         | shout  | 60          | keyword        |
| 16         | (      | 25          | delimeter      |
| 16         | fact   | 74          | identifier     |
| 16         | (      | 25          | delimeter      |
| 16         | x      | 77          | identifier     |
| 16         | )      | 26          | delimeter      |
| 16         | )      | 26          | delimeter      |
| 17         | ------ | 70          | new line       |
| 17         | x      | 77          | identifier     |
| 17         | =      | 14          | operator       |
| 17         | x      | 77          | identifier     |
| 17         | +      | 1           | operator       |
| 17         | 1      | 73          | integer_lit    |
| 18         | ------ | 70          | new line       |
| 18         | }      | 22          | delimeter      |
| 19         | ------ | 70          | new line       |
| 19         | }      | 22          | delimeter      |
+------------+--------+-------------+----------------+
```