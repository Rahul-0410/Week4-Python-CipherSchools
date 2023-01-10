# f=open('wfile.txt','r')
# print(f"cursor posion = {f.tell()}")
# print(f.read())
# print(f"cursor posion = {f.tell()}")
# f.seek(0)
# print("after seek method")
# print(f"cursor posion = {f.tell()}")
# print(f.read())

# print(f.readline())
# print(f.readline())

# print(f.readlines())

# print(f.name)
# print(f.closed)
# for line in f:
#     print(line,end='')
# f.close()

# with open('wfile.txt','r') as f:
#     data=f.read()
#     print(data)


# with open('wFile.txt','w') as f:
#     f.write('hello')
# f1=open('wFile.txt','w')
# f1.write('Hello there')
# f1.close()
# f2=open('wFile2.txt','w')
# f2.write("Hello there")

# append mode a 
# with open('wFile2.txt','a') as f:
#     f.write("How are you doing?\n what are u upto?")

# r+ mode 
# with open('wfile1.txt','r+') as f1:
#     f1.write("Hello!!, Welcome.\n How may i help you today? ")

# with open('wfile1.txt','r+') as f1:
#     f1.seek(len(f1.read()))
#     f1.write("Yes we have that drink for u ! Please be patient it will be delevered soon!!")

# Read and Write in Python
# with open('wfile1.txt','r') as rf:
#     with open('wFile.txt','w') as wf:
#         wf.write(rf.read())

# excercise 1
# with open('excerFile1.txt','r') as ex1r:
#     with open('ecerFile1_2.txt','w') as ex1w:
#         ex1w.write(ex1r.read())

#alternate solution 
# with open('excerFile1.txt','r') as ex1r:
#     with open('ecerFile1_2.txt','a') as ex1w:
#         for line in ex1r.readlines():
#             name,salary=line.split(',')
#             ex1w.write(f'{name}\'s salary is {salary}')

# excercise 2
# with open(r'C:\Users\RAHUL\OneDrive\Documents\python\Week4\Index.html','r') as webpage:
#     with open('output.txt','a') as wf:
        # for line in webpage.readlines():
        #     if '<a href=' in line:
        #         pos=line.find('<a href=')
        #         first_quote=line.find('\"',pos)
        #         second_quote=line.find('\"',first_quote+1)
        #         url=line[first_quote+1:second_quote]
        #         wf.write(url+'\n')

# with open(r'C:\Users\RAHUL\OneDrive\Documents\python\Week4\Index.html','r') as webpage:
#     with open('output2.txt','a') as wf:
#         page=webpage.read()
#         link_exist=True
#         while  link_exist:
#             pos=page.find('<a href=')
#             if pos==-1:
#                 link_exist=False
#             else:
#                  first_quote=page.find('\"',pos)
#                  second_quote=page.find('\"',first_quote+1)
#                  url=page[first_quote+1:second_quote]
#                  wf.write(url+'\n')
#                  page=page[second_quote:]




