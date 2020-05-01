#!/usr/bin/python3
import sys
import ply.lex as lex
import ply.yacc as yacc


naam=0
live={}
turn=0

tokens = (
        'ID', 'RULE','BODY'
)




filename1=sys.argv[1]
filenamel1=filename1.split(".")
filename1=filenamel1[0]
filenamed=filename1+"g.dot"
file1 = open(filenamed, "w")
str1="digraph G { ordering=out "
file1.write(str1)
file1.write("\n")
words=[]
filename = filename1+"g"+".py"
file = open(filename, "w")





t_ID = r'[a-zA-Z][0-9a-zA-Z]*'
t_RULE=r'(.+)[;]'
t_BODY=r'[#](.+)[#]'


t_ignore = " \t\n"


def t_error(t):
	print("Illegal character %s" % t.value[0])
	t.lexer.skip(1)




def p_s(p):
       '''S : E E E  '''
       global words
       global naam
       global live
       global turn
       save=[]
       flag=1
       s='''n'''+str(naam)+''' [ label = "S"]'''+";"
    #print(s)
       live.update({"n"+str(naam):0})
    #print(live)
       file1.write(s)
       file1.write("\n")
       #naam+=1
       print(str(p[1])+str(p[2])+str(p[3]))
       s1=str(p[2])
       s1="'''"+s1[1:len(s1)-2]+"'''"
       print(s1)
       words.append(str(p[1]))
       print(words)

       if (str(p[3])=='d'):
           s="\ndef p_"+str(p[1])+"(p):\n\t "+s1+"\n\t"
           file.write(s)
       elif str(p[3]=='f'):
           s="\ndef p_"+str(p[1])+"(p):\n\t "+s1+"\n\t"
           file.write(s)
       


       for i in range(naam-1,0,-1):
        
        if turn % 2 == 0:

          if i % 2 == 1 and flag <=3 :

                zz="n"+str(i)
                if(live[zz]==0):
                  s="n"+str(naam)+"->"+"n"+str(i)+";"
                  save.append(s)
               #print(s)
                  zz="n"+str(i)
                  live[zz]=1
               #print(live)
                  flag+=1
               #file.write(s)
                if(i==naam-2):
                  s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
                  save.append(s)
                #print(s)
                  zz="n"+str(naam-1)
                  live[zz]=1
                #file.write(s) 

        elif turn % 2 == 1:


          if i % 2 == 0 and flag <=3 :

                zz="n"+str(i)
                if(live[zz]==0):
                  s="n"+str(naam)+"->"+"n"+str(i)+";"
                  save.append(s)
               #print(s)
                  zz="n"+str(i)
                  live[zz]=1
               #print(live)
                  flag+=1
               #file.write(s)
                if(i==naam-2):
                  s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
                  save.append(s)
                #print(s)
                  zz="n"+str(naam-1)
                  live[zz]=1
                #file.write(s) 

 

       for i in range(len(save)-1,-1,-1):
        file1.write(save[i])
        file1.write("\n")

       naam+=1
       flag=0
       turn+=1
       #del save[:]



def p_s67(p):
       '''S : E E E E '''
       global words
       global naam
       global live
       global turn
       save=[]
       flag=1
       s='''n'''+str(naam)+''' [ label = "S"]'''+";"
    #print(s)
       live.update({"n"+str(naam):0})
    #print(live)
       file1.write(s)
       file1.write("\n")
       #naam+=1
       print(str(p[1])+str(p[2])+str(p[3]))
       s1=str(p[2])
       s1="'''"+s1[1:len(s1)-2]+"'''"
       print(s1)
       words.append(str(p[1]))
       print(words)

       if (str(p[3])=='d'):
           s="\ndef p_"+str(p[1])+"(p):\n\t "+s1+"\n\t"
           file.write(s)
       elif str(p[3]=='f'):
           s="\ndef p_"+str(p[1])+"(p):\n\t "+s1+"\n\t"
           file.write(s)
           s=str(p[4])
           s=s[1:len(s)-1]
    
           se=s.split(";")
           for i in range(len(se)):

              file.write(se[i]+"\n\t")
       


       for i in range(naam-1,0,-1):
        
        if turn % 2 == 0:

          if i % 2 == 1 and flag <=4 :

                zz="n"+str(i)
                if(live[zz]==0):
                  s="n"+str(naam)+"->"+"n"+str(i)+";"
                  save.append(s)
               #print(s)
                  zz="n"+str(i)
                  live[zz]=1
               #print(live)
                  flag+=1
               #file.write(s)
                if(i==naam-2):
                  s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
                  save.append(s)
                #print(s)
                  zz="n"+str(naam-1)
                  live[zz]=1
                #file.write(s) 

        elif turn % 2 == 1:


          if i % 2 == 0 and flag <=4 :

                zz="n"+str(i)
                if(live[zz]==0):
                  s="n"+str(naam)+"->"+"n"+str(i)+";"
                  save.append(s)
               #print(s)
                  zz="n"+str(i)
                  live[zz]=1
               #print(live)
                  flag+=1
               #file.write(s)
                if(i==naam-2):
                  s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
                  save.append(s)
                #print(s)
                  zz="n"+str(naam-1)
                  live[zz]=1
                #file.write(s) 

 

       for i in range(len(save)-1,-1,-1):
        file1.write(save[i])
        file1.write("\n")

       naam+=1
       flag=0
       turn+=1
       #del save[:]








def p_e(p):
    'E : ID  '
    global naam
    global live

    p[0]=p[1]
    print("Found an identifier \n")
    s='''n'''+str(naam)+''' [ label = "Identifier:'''+str(p[1])+'''"]'''+";"
    #print(s)



    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    naam+=1

    s='''n'''+str(naam)+''' [ label = "E"]'''+";"
    #print(s)
    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
    zz="n"+str(naam-1)
    live[zz]=1
    #print(s)

    file1.write(s)
    file1.write("\n")
    naam+=1


def p_e1(p):
    'E : RULE '
    global naam
    global live

    p[0]=p[1]
    print("Found a regex \n")
    s='''n'''+str(naam)+''' [ label = "Rule:'''+str(p[1])+'''"]'''+";"
    #print(s)



    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    naam+=1

    s='''n'''+str(naam)+''' [ label = "E"]'''+";"
    #print(s)
    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
    zz="n"+str(naam-1)
    live[zz]=1
    #print(s)

    file1.write(s)
    file1.write("\n")
    naam+=1
    
        
def p_s2(p):
    " E : BODY "
    global naam
    global live
    
    print("found a def")
    

    p[0]=p[1]
    print("Found a definition \n")
    s='''n'''+str(naam)+''' [ label = "Body:'''+str(p[1])+'''"]'''+";"
    #print(s)



    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    naam+=1

    s='''n'''+str(naam)+''' [ label = "E"]'''+";"
    #print(s)
    live.update({"n"+str(naam):0})
    #print(live)
    file1.write(s)
    file1.write("\n")
    s="n"+str(naam)+"->"+"n"+str(naam-1)+";"
    zz="n"+str(naam-1)
    live[zz]=1
    #print(s)

    file1.write(s)
    file1.write("\n")
    naam+=1
        


def p_error(p):
	if p:
		print("syntax error at {0}".format(p.value))
	else:
		print("syntax error at EOF")


def process(data):
	lex.lex()
	yacc.yacc()
	yacc.parse(data)



if __name__ == "__main__":
    aaa=filename1+".g"    
    
    file2 = open(aaa, "r")
    s=""
    s1=""
    flag=0
    f1=file2.read()
    for i in range(len(f1)):
        if f1[i] != '\n':
              if f1[i] != '#':
               s1=s1+f1[i]
               print(s1)
        elif s1.endswith('d'):
            process(s1)
            s1=""
        elif s1.endswith('f'):
            if f1[i+1] == '#' and flag == 0:
               
               s1=s1+"\n"+'#'
               flag=1
              
        




        else:
           if i == len(f1)-1:
            s1=s1+'#'
            print(s1)
            process(s1)
            s1=""
            flag=0
           elif f1[i+1] != '#':
            s1=s1+'#'
            print(s1)
            process(s1)
            s1=""
            flag=0
           else: 
            s1=s1+";"



            
    str1="}"
    file1.write(str1)
   
   
