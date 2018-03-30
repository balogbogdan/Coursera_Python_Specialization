"""
Regular expresions guide:

^  Matches the beginning of a line
$  Matches the end of the line
.  Matches any character
\s Matches whitespace
\S Matches any non-whitespace character

* Repeats a char zero or more times
*? Repeats a char zero or more times (non-greedy)
+ Repeats a char one or more times
+? Repeats a char one or more times (non-greedy)

[aeiou] Matches a single char in the listed set
[^XYZ} Matches a single char not in the listed set
[a-z0-9] The set of chars can include a range
( Indicates where string extraction is to start
) Indicates where string extraction is to end

"""
