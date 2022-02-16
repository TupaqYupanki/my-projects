import os
# from datetime import datetime, date, time

f = open('/backup/scripts/backup_sw/sw_list', 'r')
y = f.read()
x = y.split('\n')

i=0
while i<len(x)-1:
    if x[i][0] == '#':
        x.remove(x[i])
    else:
        i=i+1

# for i in x:
#     print(i)

switches = {}

i=0
while i<len(x):
    z = x[i].split(' ')
    z = list(filter(None, z))
    switches[z[1]] = {'model': z[0], 'name': z[2]}
    i = i+1



dirname = '/backup/hourly.1/config/tftp/config'
files = os.listdir(dirname)

dirname_1tvch  = '/backup/hourly.1/config/tftp/config/1tvch'
files_1tvch = os.listdir(dirname_1tvch)

dirname_a2 = '/backup/hourly.1/config/tftp/config/a2'
files_a2 = os.listdir(dirname_a2)

dirname_dlk = '/backup/hourly.1/config/tftp/config/dlk'
files_dlk = os.listdir(dirname_dlk)

dirname_ia = '/backup/hourly.1/config/tftp/config/ia'
files_ia = os.listdir(dirname_ia)

dirname_ms = '/backup/hourly.1/config/tftp/config/ms'
files_ms = os.listdir(dirname_ms)

dirname_pioner = '/backup/hourly.1/config/tftp/config/pioner'
files_pioner = os.listdir(dirname_pioner)

dirname_sudoma = '/backup/hourly.1/config/tftp/config/sudoma'
files_sudoma = os.listdir(dirname_sudoma)

dirname_ts = '/backup/hourly.1/config/tftp/config/ts'
files_ts = os.listdir(dirname_ts)


for i in switches:
    zzz=True
    if '1tvch' in switches[i]['name']:
        for s in files_1tvch:
            if switches[i]['name'] in str(s):
                print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/1tvch')
    elif 'a2' in switches[i]['name']:
        for s in files_a2:
            if switches[i]['name'] in str(s):
                print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/a2')
    elif 'dlk' in switches[i]['name']:
        for s in files_dlk:
            if switches[i]['name'] in str(s):
                print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/dlk')
    elif 'ia' in switches[i]['name']:
        for s in files_ia:
            if switches[i]['name'] in str(s):
                print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/ia')
    elif 'ms' in switches[i]['name']:
        for s in files_ms:
            if switches[i]['name'] in str(s):
                print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/ms')
    elif 'pioner' in switches[i]['name']:
        for s in files_pioner:
            if switches[i]['name'] in str(s):
                print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/pioner')
    elif 'sudoma' in switches[i]['name']:
        for s in files_sudoma:
            if switches[i]['name'] in str(s):
                print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/sudoma')
    for s in files:
        if switches[i]['name'] in str(s):
            print(str(switches[i]['name'])+' in /backup/hourly.1/config/tftp/config/')
            zzz=False
            break
    if zzz:
        print(str(switches[i]['name'])+' not found')
