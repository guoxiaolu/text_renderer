from multiprocessing.dummy import Process as Thread
from multiprocessing.dummy import Queue
import time

def func1(qm1, q12):
    while True:
        qget = qm1.get()
        if qget is not None:
            if qget is 'over':
                q12.put('over')
                break
            print ('Thread1 recv: %s'%qget)
            q12.put('1_%s'%(qget))
        
        time.sleep(1)

def func2(q12, q23):
    while True:
        qget = q12.get()
        if qget is not None:
            if qget is 'over':
                q23.put('over')
                break
            print ('Thread2 recv: %s'%qget)
            q23.put('2_%s'%(qget))
        time.sleep(0.7)

def func3(q23, q3m):
    while True:
        qget = q23.get()
        if qget is not None:
            if qget is 'over':
                q3m.put('over')
                break
            print ('Thread3 recv: %s'%qget)
            q3m.put('3_%s'%(qget))
        time.sleep(1.3)

def main():
    qm1 = Queue()
    q12 = Queue()
    q23 = Queue()
    q3m = Queue()
    t1 = Thread(target=func1,args=(qm1, q12))
    t2 = Thread(target=func2,args=(q12, q23))
    t3 = Thread(target=func3,args=(q23, q3m))
    t1.start()
    t2.start()
    t3.start()
    for i in range(100):
        qm1.put('%d'%(i))
        print ('Main send: %d'%i)
        time.sleep(0.5)
    qm1.put('over')
    result = []
    while True:
        qget = q3m.get()
        if qget is not None:
            if qget is 'over':
                break
            result.append('m_%s'%(qget)) 
            print ('Main recv: %s,%d'%(qget, len(result)))
    t3.join()
    t2.join()
    t1.join()

if __name__ == "__main__":
    main()
