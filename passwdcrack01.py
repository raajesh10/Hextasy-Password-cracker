import hashlib
import sys
import time
global stime

# Dictionary method
def dictionary():
    start_time=time.time()
    print('\nPlease enter the MD5 hash for the target password')
    p1=str(input('\n=>'))
    print('\n\n\n\nNote: You can either use our default wordlist or your customized wordlist for the attack (anything is fine). However our wordlist is very small and consists only of common password hashes.')
    d1=str(input('\nUse our default wordlist for the dictionary attack[Y/n] =>'))
    if (d1=='y' or d1=='Y'):
        file=open('default_dict.txt','r')
        data=file.read()
        file.close()
        #print(data)
    elif (d1=='n' or d1=='N'):
        while True:
            print('\nPlease enter the filename for the dictionary attack with proper location')
            fname=str(input('\n=>'))
            try:
                file=open(fname,'r')
                data=file.read()
                file.close()
                break
            except:
                print('\n\nError:File not found..........')
            
    else:
        print('\nInvalid option..........')
        return

    data=data.split('\n')
    if data[len(data)-1]=='':
        data.pop()
    count=0
    for i in data:
        h1=hashlib.md5(i.encode())
        h2=str(h1.hexdigest())
        #print('{',i,':',h2,'}')
        if p1 == h2:
            end_time=time.time() - start_time
            #print('\nPassword found, process successful....')
            print('\n\n\n\n',p1,'(',i,')')
            print('\nTime taken in seconds:',end_time)
            print('\n\nNumber of passwords attempted:',count)
            return
        count=count+1
    print('\nPassword cracking unsuccessful......')
    return

#Brute Force method
def brute_force(string,length,charset,inp,count):
    if len(string)==length:
        count=count+1
        return
    for char in charset:
        temp=string+char
        h1=hashlib.md5(temp.encode())
        h2=str(h1.hexdigest())
        print(h2)
        if inp==h2:
            print('\n\nHash cracked:\n\n')
            print(inp,'','(',temp,')')
            etime=time.time()-stime
            print('\n\nTime taken in seconds:',etime)
            print('\n\nNumber of passwords attempted:',count)
            exit()
        else:
            count=count+1
            brute_force(temp,length,charset,inp,count)
print('\nWelcome to ')
print('\n\n')
print('####################      ##    ##  #########   ##    ##   ############        #         #########   ##    ##   ####################')
print('####################      ##    ##  ##            #  #        ######          # #        ##           ##  ##    ####################')
print('####################      ########  ######         ##           ##           #####       #########     #  #     ####################')
print('####################      ########  ######         ##           ##          #######      #########      ##      ####################')
print('####################      ##    ##  ##            #  #          ##         #       #            ##      ##      ####################')
print('####################      ##    ##  #########   ##    ##        ##        #         #    #########      ##      ####################')
print('\n\n                      ############################## P@$$WORD CR@CKER ######################################')
    
while True:
    print('\n\n\n\n\n######################################################')
    print('###########################################################')
    print('\n\n\n\n Welcome to the {####p@$$cr@ck.py####}')
    print('\nNote: The password cracker is designed to run in an infinite loop, please pess ^C to exit the program anytime, Version 1.0 supports only MD5 hashing...')
    print('\nHappy Hacking.............')
    print('\nPlease select one among the below :')
    print('[1] Dictionary Attack')
    print('[2] Bruteforce Attack')
    opt=str(input('=> '))
    if opt=='1':
        print('\n\n\nDictionary attack selected....................')
        a1=dictionary()
    elif opt=='2':
        print('\n\n\nBruteforce attack selected....................')
        print('\n\nPlease select from one of the modes:')
        print('[1] Lowercase only [default]')
        print('[2] Lowercase and numbers only')
        print('[3] Lowercase, uppercase , numbers')
        print('[4] Lowercase, uppercase, numbers, special ch@racter$\n\n\n')
        opt=str(input('=> '))
        string=''
        if opt=='2':
            print('\n\nOption 2 selected.....')
            charset='abcdefghijklmnopqrstuvwxyz123456789'
        elif opt=='3':
            print('\n\n Note: option 3 selected, This may take huge amount of time (hours or days) and computing resources')
            charset='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
        elif opt=='4':
            print('\n\n Note: option 4 selected, This may take huge amount of time (hours or days) and computing resources')
            charset='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_?<>'
        else:
            print('\n\n\nDefault option selected............')
            charset='abcdefghijklmnopqrstuvwxyz'
        
        length=6
        print('\n\nPlease enter the hash to be cracked......\n\n')
        inp=str(input('=> '))
        stime=time.time()
        a2=brute_force(string,length,charset,inp,0)
    else:
        print('\n\n\nError:Invalid option')
        print('\nPlease choose a valid option or press ^C to exit for')
