# SheeshLang
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
$ python3 parser_main.py <filepath>
```
Note: ./default.sheesh will run if no arguments are given.
The following command will run the `lexer_main.py` file.
It will print a table of the tokens.


## IMPLEMENTATION DETAILS
- The lexer and parser are written in Python 3.6.
- Each file and funtion in the code is properly documented and commented about its input  arguments, return values and the functionality
- All the keywords, operators and delimeters are defined in the Grammer folder in the `hash_maps.py` file.
- Sheesh's CFG and corresponding parse table have also been defined in the Grammer folder as `Sheesh_CFG.txt` and `parse_LALR1_table.tsv`
- The `utils` folder provides with all the utility functions required for the lexer and parser.

##ADDITIONAL INFORMATION
- Logs for stack, error and input string are stored in the `Logs` folder. Logs are captured in each iteration of the parsing process.
- Testcases are provided in the `Testcases` folder. To run each of the testcases run the command:
  ```shell
  $ python3 parser_main.py Testcases/<filename>
  ```

## Functionalities [updated : 28/04/2022]:

### Lexer phase    
  - Lexes
  - 71 keywords.
  - Implemented custom keywords like shout, loop, yeet.
  - Can distinguish between various datatypes in the lexer phase.
  - distinguishes between string literal, integer literal, float literal and new line character.
  - Gives error on multiline strings and prints each error after reading through the file.
  - Output is properly printed in a table with four categories, namely:
    -  Token line
    -  Token
    -  Token value
    -  Token Category

Here's an example.
##### File:
```
def main() : void {
    int a = 4c
    return 0
    5
}
```
##### Command to test the file:
```shell
$ python3 lexer_main.py Testcases/fact.sheesh
```
##### Output:
Lexeme seperation successful.
| Token line | Token  | Token value | Token Category |
|------------|:-------:|:-------------:|----------------|
| 1          | def    | 38          | keyword        |
| 1          | main   | 70          | keyword        |
| 1          | (      | 23          | delimeter      |
| 1          | )      | 24          | delimeter      |
| 1          | :      | 10          | operator       |
| 1          | void   | 71          | keyword        |
| 1          | {      | 19          | delimeter      |
| 2          | NL     | 68          | new line       |
| 2          | int    | 63          | keyword        |
| 2          | a      | 73          | identifier     |
| 2          | =      | 12          | operator       |
| 3          | 4c     | err         | invalid        |
| 3          | NL     | 68          | new line       |
| 3          | return | 57          | keyword        |
| 4          | 0      | 74          | integer_lit    |
| 4          | NL     | 68          | new line       |
| 5          | 5      | 75          | integer_lit    |
| 5          | NL     | 68          | new line       |
| 5          | }      | 20          | delimeter      |


###Parser phase
  - Parses
  - Uses a custom CFG called Sheesh_CFG.
  - Parse table created using LALR(1) parsing technique.
  - Efficiently uses parse table to process the incoming input string.
  - Gives error on multiline strings and prints each error after reading through the file. Parser also prints the line at which the error occurs.
  - Errors are automatically dealt with by the parser. The parser will not stop on the first error and will continue finding more errors.
  - Output is properly printed in a table with four categories, namely:
    -  Token line
    -  Token
    -  Token value
    -  Token Category

Here's the same example.
##### File:
```
def main() : void {
    int a = 4c
    return 0
    5
}
```
#####Output:
`Parsed this bad boy.`
