#3. Given a list L = [1,2,3,4], we want to convert the list to the string '1234'. We tried ''.join([i for i in L]),
# #but it didn't work. Fix it.

L = [1,2,3,4]
string = ''.join([str(i) for i in L])

print(string)