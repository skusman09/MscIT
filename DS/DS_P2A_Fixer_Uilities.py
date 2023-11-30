
print("#Removing leading or lagging spaces")
baddata="  Too Many Space Is very bad   "
print('>',baddata,'<')
cleandata=baddata.strip()
print(">",cleandata,"<")
print("\n#Removing non-printable characters")
import string
printable=set(string.printable)
baddata="Data\x00science with too many funny\x01 characters is \x10bad!!!"
cleandata=''.join(filter(lambda x:x in string.printable,baddata))
print("Baddata:",baddata)
print("Cleandata:",cleandata)
print('\n#Reformatting date entry')
print('#Convert YYYY/MM/DD TO DD Month YYYY')
import datetime
baddate = datetime.date(2019,10,31)
baddata = format(baddate,'%Y-%m-%d')
gooddate = datetime.datetime.strptime(baddata,'%Y-%m-%d')
gooddata = format(gooddate,'%d %B %Y')
print('BadData: ',baddata)
print('GoodData: ',gooddata)