import time
import multiprocessing

def do_something(seconds):
    """ DOING SOME SLEEP"""
    print(f"Sleeping {seconds} second(s)...\n")
    time.sleep(seconds)
    print(f"Done Sleeping...{seconds}")

def main():
    """ MAIN PROG """
    start = time.perf_counter()

    # Method 1
#    p1 = multiprocessing.Process(target=do_something, args=[1])
#    p2 = multiprocessing.Process(target=do_something, args=[1])
#    p1.start()
#    p2.start()
#    p1.join()
#    p2.join()

    # Method 2
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    
if __name__ == "__main__":
    main()
