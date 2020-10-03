import pickle
import random
import time




def ayok():
          
    num_lines = sum(1 for line in open('Names.txt'))
    time.sleep(1)
    print('exit_key')
    
    oml = []
    
    x = 0
    fparse = open('Names.txt', 'r')
    while x < num_lines:

        try:
            err1 = 'revision'
            err2 = 'User'
            err3 = 'html'
            x+=1

            z = str(fparse.readline())
            #print(z)

            if err1 in z or err2 in z or err3 in z:
                #print('error')
                pass
                #time.sleep(.1)
        
            else:
                oml.append(z) 
                #time.sleep(.1)
                #print(z)
        except:
            pass
            #print(oml)
        
    return oml

        

                


 

    


