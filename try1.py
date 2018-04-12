import nltk
from nltk.tokenize import word_tokenize 
import sys
import re

lc = 0
address_table = []
address_table1 = []
hex_dex_bin = []

def findMri(value):
    for i in address_table:
        if value == i[0]:
            return i[1]
    return None
mri = {
    'AND': 0x0,
    'ADD': 0x1,
    'LDA': 0x2,
    'STA': 0x3,
    'BUN': 0x4,
    'BSA': 0x5,
    'ISZ': 0x6,
    
}

Imri = {
    'AND': 0x8,
    'ADD': 0x9,
    'LDA': 0xA,
    'STA': 0xB,
    'BUN': 0xC,
    'BSA': 0xD,
    'ISZ': 0xE,
}

nonmri = {
    'CLA':  7800,
    'CLE':  7400,
    'CMA':  7200,
    'CME':  7100,
    'CIR':  7080,
    'CIL':  7040,
    'INC':  7020,
    'SPA':  7010,
    'SNA':  7008,
    'SZA':  7004,
    'SZE':  7002,
    'HLT':  7001,
    #io 
    'INP':  15800,
    'OUT':  15400,
    'SKI':  14200,
    'SKO':  15100,
    'ION':  15080,
    'IOF':  15040,
}
psuedo = ("ORG","ENG","DEC","HEC")


a = open("Instr.txt","r")
print(a.tell())
linec = 0
'''
read file and convert it's instr to uppercase
linec has final var
'''
line = a.readline()
lineup  = line.upper();
if re.search("ORG", lineup):
    if ',' in lineup:
        print("ERROR on line "+ str(linec))
        exit(1)         
    else:
        temp,ads = lineup.split(" ")
        lc = int(ads)
        print("LC is",lc)           

    
#print(a.tell())
print(lineup);
i=0
j = 0
while line[:-1]:
    line = line[:-1]
    print("Line {}:{}".format(linec,lineup.strip()))
     
    line = a.readline()
    #print(re.search("LDP", lineup)) 
    lineup = line.upper()

    #process of store adress symbol table
    
    temp1 = lineup.split(" ")[0]
    #print(linec+1, temp1)

    for v,k in mri.items():
        ak = k 
        if re.match(temp1,v):
            address_table.append([ak,lc])
            i=i+1
            lc = lc +1 
    
    if re.search("END", lineup):
        if ',' in lineup:
            print("ERROR on line "+ str(linec))
            exit(1)         
        else:
            temp = lineup.split() #temp is in form of list
            
            if len(temp[0])==3:
                #print("Now let's do 2nd phase")         
                pass
            else:
                print("Error in ending programm")
    # for psudoinstruction (DEC HEX) and also gives label 
    elif re.search(",", lineup):
        temp3, inst = lineup.split(",")
        
        if 'DEC' in inst:
            ads = inst[4:]
            val = int(ads)
            val = bin(val)
            val = val[2:] #first 2 digit is like ob 
            val = val.zfill(16)
            hex_dex_bin.append([val, lc])
        if 'HEX' in inst:
            ads = inst[4:]
            val = int(ads)
            val = bin(val)
            val = val[2:] #first 2 digit is like ob 
            val = val.zfill(16)
            hex_dex_bin.append([val, lc])    
            #print(ads)
            
        if len(temp3) > 3:
            print("ERROR on line "+ str(linec))
            exit(1)         
        an = re.findall('[^A-Z]', temp3[0])
        if len(an) > 0:
            print("Invalid Label : line no. "+ str(linec))
            exit(1)
        an = re.findall('[^A-Z0-9]', temp[1:])
        if len(an) > 0:
            print("Invalid Label : line no. "+ str(linec))
            exit(1)
        label1 = temp3
        i+=1;
        address_table.append([label1, lc])
        lc += 1
        linec += 1   



    
    
    
    linec+=1
#print(linec)   
a.close()  
#print(address_table)  
print("===============================")
i1 = i-7;
j1 = j -17;
print(address_table[0:i1])
print("HEX or DEX ",hex_dex_bin)
#print(address_table)
# def SecondPass(File):
#   lineNo = 0
#   lc = 0

#   for line in File:
#       if 'DEC' in line:
#           try:
#               temp,ads = line.split(" ")
#               a = re.findall('[^0-9]',ads[:-1])
#               if len(a) > 0:
#                   print("Invalid Address : line no. "+ str(lineNO))
#                   exit(1)
#               val = int(ads)
#               val = bin(val)
#               val = val[2:]
#               val = val.zfill(16)
#               hex_dex_bin.append([val, lc])
#               except ValueError:
#                   lc = 0
#               except Exception as e:
#                   print("ERROR on line "+ str(lineNO) + "\n" + str(e))
#                   exit(1)
#               lc += 1