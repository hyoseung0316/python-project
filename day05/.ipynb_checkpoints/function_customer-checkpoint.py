import re
from secrets import choice

from zmq import PROTOCOL_ERROR_ZMTP_MALFORMED_COMMAND_MESSAGE

def customer_input(customer):
    pass
if choice=="I":
        customer={'name':'','gender':'','email':'','birthyear':''}
        customer['name']=input('이름 >>>')
        while True:
            customer['gender']=input('성별(M,F) >>>').upper()
            if customer['gender'] in ('M','F'):
                break
        while True:
            p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
            customer['email']=''
            while not p.search(customer['email']):
                customer['email']=input('email >>> ')
    
            check = 0
            for i in custlist:
            if i['email'] == customer['email']:
                check = 1
                break
        if check == 0:
            break
        print('중복되는 이메일이 있습니다.')
    while True:
        customer['birthyear'] = input('생년월일(4자리) >>> ')
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal()
            break
    custlist.append(customer)
    page = len(custlist)-1
    print(custlist)
    return page

def customer_c(custlist,page):
     if page < 0:
        print('입력된 정보가 없습니다.')
    else:
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])

def customer_p(custlist,page):
    if  page <= 0:
        print('첫번째 페이지 입니다.')
    else:
        page -= 1
        print(custlist[page])
    print(f'현재 페이지는 {page+1}페이지 입니다.')
    return page

def customer_n(custlist,page):
    if  page >= len(custlist)-1:
        print('마지막 페이지 입니다.')
    else:
        page += 1
        print(custlist[page])
    print(f'현재 페이지는 {page+1}페이지 입니다.')
    return page

def customer_update():
    while True:
        choice1 = input('수정하려는 이메일을 입력하세요')
        idx = -1
        for i in range(len(custlist)):
            if custlist[i]['email']==choice1

def customer_delete(custlist,page):
    print(custlist)
    choice1 = input('삭제하려는 이메일 주소를 입력하세요')
    delok = 0
    for i in range(len(custlist)):
        if custlist[i]['email'] == choice1:
            print(f'{custlist[i]["name"]}님의 정보가 삭제되었습니다')
            if page == len(custlist)-1:
                page -= 1
            del custlist[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 고객 정보입니다')
    print(custlist)
    return page 
