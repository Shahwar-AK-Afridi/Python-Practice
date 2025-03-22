fname = "A:\Coursera\Python\py4e\Python-Practice\Chapter 13 (Databases)\Counting Emails of Organization\mbox.txt"

with open(fname,"r",encoding='cp1252') as fhand:
    lst_email = []
    dic = {}
    for line in fhand:
        if line.startswith("From"):
            data = line.split(" ")
            email = data[1]
            data2 = email.split("@")
            org = data2[-1]   

            lst_email.append(data[1])
            if org not in dic:
                dic[org] = 1
            dic[org] += 1
    print(dic)

max_email = sorted(dic, key = lambda key:dic[key], reverse=True)[0]
print(max_email)

