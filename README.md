# Calculator
Reverse Polish Notation Calculator

Reverse Polish Notation Calculator
This is a command line application that evaluates mathematical expressions specified in Reverse Polish Notation (RPN). The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division, as well as additional functions like square root, sine, cosine, average, and modulus.

Usage
Create an input file containing the RPN expressions you want to evaluate. Each expression should be on a separate line, with individual parameters separated by spaces.

Example input file (input.txt):

1 2 +
3 4 *
6 3 * 2 - sqrt
Run the calculator by executing the rpn.py script and passing the input file as a command line argument:

python rpn.py input.txt
The calculator will process each line of the input file and display the results:

1 2 + = 3.0
3 4 * = 12.0
