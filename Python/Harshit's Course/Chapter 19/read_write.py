from csv import DictReader,DictWriter

with open('read.csv','r') as rf:
    with open('w.csv','w',newline='') as wf:
        csv_read=DictReader(rf)
        csv_write=DictWriter(wf, fieldnames=['Name','Age','Class'])
        csv_write.writeheader()
       
        for row in csv_read:
            nm,ag,cls=row['name'],row['age'],row['class']
            csv_write.writerows([{'Name':nm.title(),'Age':ag,"Class":cls}])
