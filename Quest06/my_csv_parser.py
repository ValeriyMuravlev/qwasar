def my_csv_parser(arr, sep):
    return [[el for el in line.split(sep)] for line in arr.split("\n") if (len(line) > 0)]

print(my_csv_parser("a,b,c,e\n1,2,3,4\n", ","))
