Description
What is a the CSV? :-)
It's a format very often use, Microsoft Excel is using it.
It's a 2d array: row and column.
Row are separated by "line" (the character "
") and columns are separated by ",". (Separator can be different, it can also be ";")

Your mission here, is to transform a string following the CSV format to a 2d array.

Your function will takes two arguments, the content of a CSV as a string and a separator.
Your function will return an arrays (lines) of arrays (columns).

In this assignement, you will have to solve a problem: how to transform a string into an array of array.

Example 00

Input: "a,b,c,e\n1,2,3,4\n" && ","
Output: 
Return Value: [["a", "b", "c", "e"], ["1", "2", "3", "4"]]
