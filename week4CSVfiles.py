from csv import reader
with open('file.csv','r') as f:
    csv_reader=reader(f)
    # print(csv_reader)
    # next(csv_reader)
    for row in csv_reader:
        print(row)

from csv import DictReader
with open('file.csv','r') as f:
    csv_reader=DictReader(f)
    for row in csv_reader:
        # print(row)
        print(row['name'])

from csv import writer
with open('file2.csv','w',newline='') as f:
    csv_writer=writer(f)
    csv_writer.writerow([ 'name','countries'])
    csv_writer.writerow([ 'rahul','India'])
    csv_writer.writerow([ 'jenni','Finland'])
    csv_writer.writerows([[ 'name','countries'],[ 'rahul','India'],[ 'jenni','Finland']])

from csv import DictWriter
with open('file3.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'firstname':'Rahul',
        'lastname':'Gupta',
        'age':20
    })
    csv_writer.writerow({
        'firstname':'Rakesh',
        'lastname':'Gupta',
        'age':26
    })
    csv_writer.writerow({
        'firstname':'Ravi',
        'lastname':'Gupta',
        'age':23
    })

from csv import DictReader,DictWriter
with open('file3.csv','r',newline='') as rf:
    with open('file4.csv','w') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age=row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({
                'first_name':fname.upper(),
                'last_name':lname.upper(),
                'age':age
            })


