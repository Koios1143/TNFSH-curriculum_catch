import requests
from bs4 import BeautifulSoup
year_code = 101

for grade in range(1,4):
    for room in range(1,20):
        class_code = grade*100 + room
        site = "http://w3.tnfsh.tn.edu.tw/deanofstudies/course/C" + str(year_code) + str(class_code) + ".HTML"
        page = requests.get(site)
        if(page.status_code == requests.codes.ok):
            soup = BeautifulSoup(page.content, 'html.parser')
            soup.edcoding = 'utf-8'

            print("class:" + str(class_code))
            ordi = "mso-yfti-irow:"
            for i in range(2,10):
                col = ordi + chr(48+i)
                now = soup.find_all('tr',style=col)

                s = now[0].text.strip()
                fixed = s.split('\n')

                times = 0
                for j in range(len(fixed)):
                    times+=1
                    if(fixed[j] == ''):
                        continue;
                    if(times<=2):
                        print(fixed[j],end='')
                    elif(times==3):
                        print(fixed[j],end=' ')
                    elif(times<=8):
                        continue
                    elif((times-11)%4 == 0):
                        print(fixed[j].ljust(6,"一"),end=' ')
                    elif((times-12)%4 ==0):
                        # print(fixed[j],end=' ')
                        continue
                    else:
                        print(fixed[j].ljust(6,"一"),end=' ')
                print()
            print()
        else:
            print('Get page ERROR\nstatus code: ' + str(page.status_code))