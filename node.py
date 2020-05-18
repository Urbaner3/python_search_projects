import sys
import numpy as np
import time

#in node.py
class operation:
    def __init__(self,old_state,new_state,msize):
        self.o_state = old_state
        self.n_state = new_state
		self.size = msize


    def expand(self):
        #check the 2n+2 states is appliable with how large substration
        child =[]
        check = np.zeros([1,2*msize+2]).tolist()[0]
        #incase min is negative
        if self.o_state.max()<0:
            print 'wrong matrix<0'
            return 0
        for code in range(2*msize+2):
            if code/msize == 0 :
                flag = self.o_state[code%msize,:].min()
                print 'flag', flag, 'check',check,'code',code
                if flag != 0:
 	            check[code]=flag
        	else :
 	            check[code]=-1
            elif code/msize == 1 : #cloumn
	        flag = self.o_state[:,code%msize].min()
	        print 'flag', flag, 'check',check,'code',code
                if flag != 0:
 	            check[code]=flag
	        else :
 	            check[code]=-1
            elif code == 2*msize:
	        temp=[]
	        for i in range(msize):
	            temp.append(self.o_state[i,i])
	
	        flag = min(temp)
	        if flag != 0:
 	            check[code]=flag
	        else :
 	            check[code]=-1
	        print 'flag', flag, 'check',check,'code',code
            elif code == 2*msize+1 :
	        temp=[]
	        for i in range(msize):
	            temp.append(state[i,msize-1-i])
	
	        flag = min(temp)
	        if flag != 0:
 	            check[code]=flag
	        else :
 	            check[code]=-1
	        print 'flag', flag, 'check',check,'code',code
            #only take ops with positive subs
        check =[ (x,y) for x,y in enumerate(check) if y > 0]
        print 'check',check,'child',child
        child += check
        print 'check',check,'child',child
        return child

    def new_state(self,code,addor):  #para in tuple 
        #run the operations   
        A = np.mat(state)
        if code<0 or code>2*msize+1:
            return A
        if code<msize :  #row ops
            A[code+1-1,:]=A[code+1-1,:]+addor*np.ones([1,msize])
        elif code>=msize and code<2*msize : #column ops
            code = np.mod(code, msize)
            A[:,code+1-1]=A[:,code+1]+addor*np.ones([msize,1])
        elif code == 2*msize : #left diag op
            for ii in range(msize+1):
                A[ii,ii]+=addor
            
        elif code == 2*msize+1 : #right diag op
            for ii in range(msize+1):
                A[ii,msize-1-ii]+=addor
      
        return A



