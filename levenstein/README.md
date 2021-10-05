My Levenshtein
Remember to git add && git commit && git push each exercise!

We will execute your function with our test(s), please DO NOT PROVIDE ANY TEST(S) in your file

For each exercise, you will have to create a folder and in this folder, you will have additional files that contain your work. Folder names are provided at the beginning of each exercise under submit directory and specific file names for each exercise are also provided at the beginning of each exercise under submit file(s).

My Levenshtein	
Submit directory	ex00
Submit file	my_levenshtein*
Languages	javascript => .js, python => .py, ruby => .rb, c => .c, ...
Description
Calculate the Levenshtein number between two words.

The Levenshtein number is simple, it is just a value that represents how close two given strings are.
It is found by comparing two strings and returning the difference between them.

Let’s look at the following example:

  abc
  dbc
  ^  
The Levenshtein difference between these two strings is 3. The two strings are almost identical, other than one letter. That letter, 'd’, is close to the example, 'a’, meaning the Levenshtein value will be small.

Instructions
Your function must take in 2 strings with the exact number of characters and return an integer representing the difference between them.

If your parameters are not the same size then your function will return -1.

If the two strings are the same size, you must then iterate through each string and determine which characters are different.

For any characters where the two strings are different, you must then calculate the difference between them and return the overall distance upon the completion of your function.

fn my_levenshtein(s1: &String, s2: &String) -> i32 {
	...
}
TIPS (only for Rust)
https://doc.rust-lang.org/std/iter/struct.Zip.html

Example 00

Input: "GGACTGA" && "GGACTGA"
Output: 
Return Value: 0
Example 01

Input: "ACCAGGG" && "ACTATGG"
Output: 
Return Value: 2
Example 02

Input: "GGACGGATTCTG" && "AGG"
Output: 
Return Value: -1
Example 03

Input: "" && ""
Output: 
Return Value: 0
