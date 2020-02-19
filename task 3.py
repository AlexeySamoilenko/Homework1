from threading import Thread, Lock

lock = Lock()
a = 0


def function(arg):
    global a
    lock.acquire()
    for _ in range(arg):
        a += 1
    lock.release()

def main():
    threads = []
    for i in range(5):
        i = Thread(target=function, args=(1000000,))
        i.start()
        threads.append(i)

  
    
    
        
    [t.join() for t in threads]
    print("----------------------", a)  # ???


main()
