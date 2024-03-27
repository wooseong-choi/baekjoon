# 왜 안되는 것이지?

import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input().rstrip())

class maxHeap:
    def __init__(self):
        self.heap = []

    def add(self, val):
        self.heap.append(val)  

        tn = len(self.heap)-1
        #print(f'tn = {tn} ')
        while(tn > 0) :
            if self.heap[tn] > self.heap[tn//2]:
                #print( str(self.heap[tn]) +' '+ str(self.heap[tn//2])+ '<=>'+str(self.heap[tn//2])  +' '+ str(self.heap[tn])+ '\n')
                self.heap[tn], self.heap[tn//2] = self.heap[tn//2], self.heap[tn]
                tn//=2
            else:
                break
        
             

    def out(self):
        if len(self.heap) > 0:
            x = self.heap[0]
            del self.heap[0]

            tn = 0
            while(len(self.heap)-1 > tn*2):
                if self.heap[tn*2] == 0 and self.heap[tn*2+1] == 0:
                    break
                if self.heap[tn] < max(self.heap[tn*2], self.heap[tn*2+1]):
                    temp = self.heap[tn]
                    if self.heap[tn*2] > self.heap[tn*2+1]:
                        self.heap[tn] = self.heap[tn*2]
                        self.heap[tn*2] = temp
                        tn *= 2
                    else:
                        self.heap[tn] = self.heap[tn*2+1]
                        self.heap[tn*2+1] = temp
                        tn = tn*2+1
                else:
                    break
        

            return x 
        else :
            return 0
    
if __name__ == '__main__' : 

    hip = maxHeap()
    for i in range(n):
        val = int(input().rstrip())
        
        if val > 0 :
            hip.add(val)
        else :
            print(str(hip.out())+'\n')            