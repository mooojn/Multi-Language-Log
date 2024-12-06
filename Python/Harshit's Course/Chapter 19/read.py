from csv import Reader,DictReader

with open("usr_info.csv",'r') as f:
    csv_read=DictReader(f)
    
    for i in csv_read:
        print(i['age'])

