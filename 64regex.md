Regex Quick Reference
=====================

Special characters
------------------

- `.` matches any character 
- `^` matches start of the string
- `$` matches end of the string or just before newline at end of string
- `|` to say 'or' (a|b match a or b)
- `*` 0 or more
- `+` greedy; keeps searching until it reaches last token (1 or more)
- `+?` not greedy; searches to next occurence of token
- `.+` matches all characters to end of the line
- `\.` matches an actual dot
- `()` capturing groups
- `\(` matches left paranthese 
- `\<` start of word
- `\>` end of word

Quantifiers
-----------
- `{3}` exactly 3
- `{3,}` 3 or more
- `{3,5}` 3, 4, or 5

Characters
----------

- `\A` start of string
- `\Z` end of string
- `\c` control character
- `\b` word boundry
- `\B` not work boundry
- `\n` new lines
- `\r` carriage return
- `\s` space characters
- `\S` not white space
- `\t` tab
- `\v` vertical tab
- `\w` matches word character
- `\W` not word
- `\d` digits 0-9
- `\D` not digit
- `\x` hexadecimal digit
- `\O` octal digit

Lookahead and Lookbehind
------------------------

- `(?<!` negative look behind
- `(?<=` positive look behind
- `(?=`  positive look ahead
- `(?!`  negative look ahead

Groups and Ranges
-----------------
- `(...)` Group
- `(?...)` Passive group
- `[abc]` range a or b or c
- `[^abc]` not a or b or c
- `[a-q]` matches lowercase from a to q
- `[A-Q]` matches uppercase letter from A to Q
- `[0-7]` digit 0 to 7
- `\x` group/subpattern number "x"

POSIX
-----

- `[:upper:]` upper case letters
- `[:lower:]` lower case letters
- `[:alpha:]` all letters
- `[:alnum:]` digits and letters
- `[:digit:]` digits
- `[:xdigit:]` hexade­cimal digits
- `[:punct:]` punctuation
- `[:space:]` blank characters
- `[:cntrl:]` control characters
- `[:print:]` printed characters and spaces
- `[:word:]` digits, letters and underscore

Substitutions
-------------

- `$n` substring matched by group number n
- `$&` copy of whole match
- `$'` after matched string (use '`' instead of ''' for before)
- `$+` last matched string

Flags
-----

- `g` global match more than once
- `m` forces $ and ^ to match each newline individually
- `i` make regex case-insensitive
