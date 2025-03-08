# interface_calculator
>Tkinter Usage: The code uses the tkinter library to create a GUI-based calculator named "Bunnyulator".

>Math Library: The math module is imported for mathematical functions like square root, logarithm, and factorial.

>GUI Setup:
The window title is set as "Bunnyulator".
The background color is black.
The window size is 680x486, positioned at (100,100) on the screen.

>Entry Field:
An Entry widget is created for user input.
It has a bold Arial font, white text, and black background.

>Buttons Layout:
Buttons are arranged in a grid layout with labels corresponding to calculator functions.
Some placeholders (θ-θ) are present, which seem unnecessary.

>Button Functionality (click Function):
Handles different button clicks.
Supports basic operations (+, -, *, /) and advanced functions (square root, cube root, power, log, factorial).
Handles errors using a try-except block.
Uses eval() to compute mathematical expressions.

>Event Handling:
The command attribute in buttons uses lambda to pass the button value to the click function.
Special functions like C (delete last digit) and CE (clear all input) are implemented.

>Loop for Button Placement:
A loop iterates over the button_text_list and places buttons in an 8-column layout.
When a row is full, it moves to the next row.

>Main Event Loop:
The root.mainloop() function runs the Tkinter GUI indefinitely.







