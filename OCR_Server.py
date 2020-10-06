# @Author  :  lijishi
# @Contact :  lijishi@emails.bjut.edu.cn
# @Software:  Pycharm & Python 3.7
# @EditTime:  Jan 23, 2020
# @Version :  1.0
# @describe:  Confirm Availability of Text Identify --Server
# @LICENSE :  GNU GENERAL PUBLIC LICENSE Version 3

# References
# https://blog.csdn.net/c_chuxin/article/details/100586079

# Warning
# This version is not identical to the actual server deployment version
# Unknown bugs are possible，Be very careful when deploying

# V1.0 Server Transfer Module
# Has Stopped !!!!!!!!!!!!!!!

import socket
import os
import sys
import csv
import time

max_mode = 16
change_site = 0
change_num = 0
client_ip = ' '
data_name = ' '
send_data = ' '

def socket_server_receive_data():
    global client_ip
    global change_num
    global data_name
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #s.bind(('127.0.0.1', 6666))  # local test
        s.bind(('Your IP', 6666))
        # If it is a cloud host, remember to use the Intranet address!!
        s.listen(10)

    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while True:
        sock, addr = s.accept()
        buf = sock.recv(1024)
        buf = buf.decode()
        # s.send(buf.encode())
        client_ip = str(addr[0])

        log_name = 'log.txt'
        with open(log_name, 'a') as log:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log.write(now_time)
            log.write(" From ")
            log.write(str(addr[0]))
            log.write(" Received ")
            log.write(str(buf))
            log.write("\n")
        log.close()
        
        if str(buf)[0:2] == '00':

            month = time.strftime("%Y-%m", time.localtime())
            data_name = 'OCR_Data_' + month + '.csv'
            if os.path.exists(data_name):
                print('Pass!')
            else:
                Initial(data_name)
            
            data = '2+' + str(Query_Left(str(buf)[3:]))

            log_name = 'log.txt'
            with open(log_name, 'a') as log:
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                log.write(now_time)
                log.write(" From ")
                log.write("127.0.0.1 ")
                log.write("Send ")
                log.write(str(data))
                log.write("\n")
            log.close()
        
            sock.send(data.encode())
            sock.close()
            return


        month = time.strftime("%Y-%m", time.localtime())
        data_name = '  '
        if os.path.exists(data_name):
            print('Pass!')
        else:
            Initial(data_name)

        csv_name = 'OCR_Server.csv'
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        headers = ['Date', 'IP', 'Apply', 'Key', 'IsOK']
        flag_IsOK = IsOK(str(buf))
        row = {'Date':now_time, 'IP':str(addr[0]), 'Apply':str(buf)[0:2], 'Key':str(buf)[3:10], 'IsOK':flag_IsOK}

        if change_num > 0:
            errorcode = '101'
        else:
            errorcode = '102'

        if flag_IsOK:
            data = '1+' + str(change_num)
        else:
            data = '0+' + errorcode

        log_name = 'log.txt'
        with open(log_name, 'a') as log:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log.write(now_time)
            log.write(" From ")
            log.write("127.0.0.1 ")
            log.write("Send ")
            log.write(data)
            log.write("\n")
        log.close()
        
        sock.send(data.encode())
        sock.close()

        #print(row)
        with open(csv_name, 'a', newline='') as server:
            #server_csv = csv.writer(server)
            server_csv = csv.DictWriter(server, headers)
            server_csv.writerow(row)
        server.close()

def socket_server_send_data(flag):
    global client_ip
    global change_num

    if change_num > 0:
        errorcode = '101'
    else:
        errorcode = '102'

    if flag:
        data = '1+' + str(change_num)
    else:
        data = '0+' + errorcode

    log_name = 'log.txt'
    with open(log_name, 'a') as log:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log.write(now_time)
        log.write(" From ")
        log.write("127.0.0.1 ")
        log.write("Send ")
        log.write(data)
        log.write("\n")
    log.close()

    s.send(data.encode())
    #s.close()

def IsOK(item):
    global change_site
    global change_num
    left = Query_Left(item[0:2])
    change_num = left-1
    if left > 0:
        if Check_Key(item[3:10]):
            #socket_server_send_data(1)
            Sub_Left(left)
            return 1
        else:
            #socket_server_send_data(0)
            return 0
    else:
        #socket_server_send_data(0)
        return 0

def Check_Key(key):
    if key == '1234567':
        return 1
    else:
        return 0

def Query_Left(item):
    global data_name
    global change_site
    with open(data_name, 'r') as data:
        reader = csv.reader(data)
        result = list(reader)
        for i in range(max_mode+1):
            if result[i][0] == item :
                #print(result[i])
                num = int(result[i][1])
                change_site = i
                break
    data.close()
    return num

def Sub_Left(change):
    global data_name
    global change_site
    with open(data_name, 'r') as data:
        reader = csv.reader(data)
        result = list(reader)
        result[change_site][1] = str(change-1)
    data.close()
    with open(data_name, 'w', newline='') as data:
        #headers = ['Item', 'Left']
        data_csv = csv.writer(data)
        #data_csv = csv.DictWriter(data, headers)
        #data_csv.writerow(headers)
        data_csv.writerows(result)
    data.close()

def Initial(path):
    headers = ['Item', 'Left']
    rows = [ [11, 1000], [12, 1000], [13, 1000], [14, 1000], [15, 1000], [21, 1000], [22, 1000], [23, 1000], [24, 1000], [31, 1000], [32, 1000], [41, 1000], [42, 1000], [43, 1000], [51, 1000], [52, 1000] ]
    with open(path, 'w', newline='') as data:
        data_csv = csv.writer(data)
        #data_csv = csv.DictWriter(data, headers)
        data_csv.writerow(headers)
        data_csv.writerows(rows)
    data.close()

        # return buf
        # sock.close()

if __name__ == '__main__':

    server_name = r'OCR_Server.csv'
    if os.path.exists(server_name):
        print('Pass!')
    else:
        headers = ['Date', 'IP', 'Apply', 'Key', 'IsOK']
        with open(server_name, 'w', newline='')as server:
            server_csv = csv.DictWriter(server,headers)
            server_csv.writeheader()
        server.close()

    while True:
        socket_server_receive_data()
