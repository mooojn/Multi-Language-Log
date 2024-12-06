from csv import DictWriter

with open('write.csv','w',newline='') as f:
    csv_write=DictWriter(f,fieldnames=['name','age','class'])
    csv_write.writeheader()

    # csv_write.writerow({'name':'moon',"age":21,'class':'13'})
    # csv_write.writerow({'name':'saliq',"age":18,'class':'14'})
    # csv_write.writerow({'name':'meeral',"age":14,'class':'10'})
    
    # csv_write.writerows([ {'name':'moon',"age":21,'class':'13'},
    #                      {'name':'saliq',"age":18,'class':'14'},
    #                      {'name':'meeral',"age":14,'class':'10'}])
