# bingo
This repository contains a simple python script to generate minimalist html
bingo boards.

# Requirements

This script only requires `python3` and the standard library.

# Getting Started

To install, simply clone this reposity and run using `python3`.
```
$ git clone https://github.com/edelsonc/bingo
$ cd bingo
$ python3 bingo
```

The bingo board choices are specifies by the `bingo_choices.txt` file. To
update to custom choices, simply replace each of the `Choice` instances with
your own options. `bingo.py` makes 5x5 bingo boards, so you must feed it a list
of 24 choices.

# Examples
Calling the script with the default `bingo_choices.txt`  prints the following
`html` to terminal

```
$ python3 bingo.py

<!DOCTYPE html>
<html>
    <head>
        <style>
            table th { border: 1px solid black }
        </style>
    </head>
    <body>
        <h1>Bingo time!</h1>
<table>
<tr>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th></tr>

<tr>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th></tr>

<tr>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">free</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th></tr>

<tr>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th></tr>

<tr>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th>
<th><input type="checkbox" name="bingo">Choice</th></tr>
</table>

    </body>
</html>
```

To instead create an `html` file simply pipe the output to the appropriate
file
```
$ python3 bingo.py > my_bingo.html
```
