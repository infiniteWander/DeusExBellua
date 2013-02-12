DeusExBellua
============

A character aggregator for game masters

Usage
===========
The following commands are available:

+ `show <character>`
+ `find <expression>`
+ `set <system>`
+ `help`

The `help` command will give you basic information, about the commands (although they are very straightforward).
However some clarification might be needed on the expression formatting (see: [search pattern](#search-pattern))

Notes
-----------
This program is `ledit` friendly (and I recomand using it if you don't want to feel very very frustrated)

The models are stored in `models/` and I strongly recomand using/creating and maintening them.

Search pattern
-----------
The help state:

+ `<expression> = <field> [=><?!] <value> ( [&|] <expression> )`

Witch means an expression is composed of a field (witch would be looked for presence in the characters) an operator and a value to compare. This expression can be completed by a logical operator and eventualy another expression.

It is important to note that the `<field>` is compared for inclusion in ALL the fields of ALL charaters, 
hence meaning that "magic>4" will list all character who have "magic" in a characteristic  to a level greater than 4.

### Operator signification
+ `'<'` and `'>'` : supperior and inferior
+ `'='` and `'!'` : equal and different
+ `'?'` : includes

+ `'&'` : and
+ `'|'` : or

### Examples
+ `magic>4` : will list any character with magic inside a field at a level above 4
	+ `White magic = 5`
	+ `magic = 9`
+ `str>4 & magic< 3` : will list any character with a str above 4 and magic below 3
	+ `str = 5` , `magic=0`
	+ `striper = 6`, `magic =2`

TODO
===========
+ Upgrade error handling
+ Implement a correct system changing
+ Context overflow is also an issue

Tao Te Ching
------------

Do not seek fame. Do not make plans. Do not think that you know.

Be awareof all that is and dwell in the infinite. Wander where there is no path.

Be empty that is all.

Licence
-----------
DeusExBellua is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
