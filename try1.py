import nltk
from nltk.tokenize import word_tokenize 
import sys
import re

lc = 0
address_table = []
address_table1 = []
hex_dex_bin = []

def search(myDict, search1):
    search.a=[]
    for key, value in myDict.items():
        if search1 in value:
            search.a.append(key)


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
    'CLA': 0x7800,
    'CLE': 0x7400,
    'CMA': 0x7200,
    'CME': 0x7100,
    'CIR': 0x7080,
    'CIL': 0x7040,
    'INC': 0x7020,
    'SPA': 0x7010,
    'SNA': 0x7008,
    'SZA': 0x7004,
    'SZE': 0x7002,
    'HLT': 0x7001,
    #io 
'INP': 0xF800,
    'OUT': 0xF400,
    'SKI': 0xF200,
    'SKO': 0xF100,
    'ION': 0xF080,
    'IOF': 0xF040,
}
#psuedo = ("ORG","ENG","DEC","HEC")



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
    
    tempo = lineup.split(" ")
    #print(tempo)
    #non_mri = tempo[0]
    mri_get = len(tempo)
    
    if mri_get==1:
        non_mri = tempo[0]
        if non_mri == 'END':
            #print("END the line")
            exit(1)
        # else:

            #print(non_mri)
         #search(nonmri, str(non_mri))
    #     print(search.a)
        for v,k in nonmri.items():
            if re.match(tempo[0],v):
                address_table.append([k,lc])
            # else:
            #     print("wrong instruction")        
        # for v,k in nonmri.items():
        #     if re.match('END',non_mri):
        #         pass
        #     elif re.match(non_mri,v):
        #         address_table1.append([tempo[0],lc])


            # non_mri = tempo[0]
            # print(type(non_mri))
            # for v,k in nonmri.items():
 
    #             if re.match(non_mri,v):
    #                 print(nonmri)
    #                 print(v)
    #                 address_table1.append([ak,lc])
    #                 i=i+1
    #                 lc = lc +1 
            # if non_mri in nonmri.values():
            #     print("wahh")
            # # for v,k in nonmri.items():
            #     address_table.append([tempo[0],lc])
            #     if re.match(tempo[0],v):
                    
            #         lc = lc +1 
 

    #process of store adress symbol table
    
    temp1 = lineup.split(" ")[0]
    #print(linec+1, temp1)
    #works well with MRI instruction
    for v,k in mri.items():
        ak = bin(k) 
        ak = ak[2:] #first 2 digit is like ob 
        ak = ak.zfill(16)
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
        i+=1
        # labeli = int(label1)
        # labeli = bin(labeli)
        # # labeli = label1[2:]
        # labeli = labeli.zfill(16)
        # #label1 = bin(label1)
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
print(address_table1)
