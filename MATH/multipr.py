import multiprocessing as mp
import numpy as np
import time

CORE_COUNT = mp.cpu_count()

def random_square(seed):
    np.random.seed(seed)
    random_num = np.random.randint(0,10)
    return random_num**2

def benchmark(function: callable):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        output = function(*args,**kwargs)
        t1 = time.time()
        elapsed_time = t1-t0
        print(f'Excecution Time {round(elapsed_time, 5)}s\'')
        return elapsed_time
    return wrapper

@benchmark
def serial_test(iterations):
    results = []
    for i in range(iterations):
        results.append(random_square(i))
    return results

@benchmark
def parallel_test(iterations):
    pool = mp.Pool(processes = CORE_COUNT)
    results = [pool.map(random_square,range(iterations))]
    return results

def main():
    n = 1000000
    a = serial_test(n)
    b = parallel_test(n)
    print(a)
    print(b)

if __name__ == '__main__':
    main()