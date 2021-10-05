import datetime


def my_data_transform(param_1):
    my = param_1.split("\n")
    val = []
    for i in my:
        val.append(i.split(','))
    val.pop(len(val) - 1)

    j = 0
    for i in val:
        if j == 0:
            j += 1
        else:
            temp = i[4].split('@')
            i[4] = temp[1]

            date_time_obj = datetime.datetime.strptime(i[9], '%Y-%m-%d %H:%M:%S')
            b = date_time_obj.hour
            if b >= 6 and b < 12:
                i[9] = "morning"
            elif b < 18:
                i[9] = "afternoon"
            elif b <= 23:
                i[9] = "evening"

            a = int(i[5])
            if a >= 1 and a <= 20:
                i[5] = "1->20"
            elif a <= 40:
                i[5] = "21->40"
            elif a <= 65:
                i[5] = "41->65"
            elif a <= 99:
                i[5] = "66->99"
        list = []
        for i in val:
            string = ""
            for j in i:
                string += j + ","
            string = string[: -1]
            list.append(string)
    return list


print(my_data_transform(
    "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"))
