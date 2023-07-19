# Example Grid

[<br>
["0", "0", "0", "0", "0", "0"],<br>
["0", "a", "d", "x", "a", "0"],<br>
["0", "x", "x", "x", "x", "0"],<br>
["0", "a", "b", "x", "a", "0"],<br>
["0", "x", "c", "c", "x", "0"],<br>
["0", "c", "O", "O", "c", "0"],<br>
["0", "0", "0", "0", "0", "0"]<br>
]<br>

# Rules

The outer rows and columns are padding and are always "0" -> (zero)

Long vertical blocks are represented as "a"<br>
Long horizontal blocks are represented as "b"<br>
Single square blocks are represented as "c"<br>
The goal block is represented as "d"<br>

All those names are placed where the top-left part of the block would be.<br>
The rest of the space that the block occupies is represented with "x".<br>
Empty space is "O" -> (CAPITAL Oh)

# Modify starting position

Modify the .jsons provided or make your own.<br>
Change the argument in main.py to choose your own .json
