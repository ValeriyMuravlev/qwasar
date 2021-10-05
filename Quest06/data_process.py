def my_data_process(arr):
    res = dict()
    for key in arr[0].split(","):
        res[key] = dict()
    arr = [el.split(",") for el in arr]
    col = 0
    for key in res.keys():
        for row in range(1, len(arr)):
            if (arr[row][col] in res[key].keys()):
                res[key][arr[row][col]] += 1
            else:
                res[key][arr[row][col]] = 1
        col += 1
    del res["FirstName"], res["LastName"], res["UserName"], res["Coffee Quantity"]
    return str(res).replace(", ", ",").replace(": ", ":").replace("'", '"')

print(my_data_process(["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]))
