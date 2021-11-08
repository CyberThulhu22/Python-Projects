import time
import concurrent.futures

def do_something(seconds):
    """ DOING SOME SLEEP"""
    print(f"Sleeping {seconds} second(s)...\n")
    time.sleep(seconds)
    return(f"Done Sleeping...{seconds}")

def main():
    """ MAIN PROG """
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)
        
#        results = [executor.submit(do_something, sec) for sec in secs]
#        for f in concurrent.futures.as_completed(results):
#            print(f.result())
        
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
    
if __name__ == "__main__":
    main()
