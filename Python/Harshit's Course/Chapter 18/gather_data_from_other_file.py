
with open('data.txt','r') as f1:
    with open('data_extracted.txt','a') as f2:
        for line in f1.readlines():
            name,salary = line.split(',')
            f2.write(f'{name.title()}\'s salary is ${salary}')
