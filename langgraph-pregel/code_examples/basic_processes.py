from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count
import time

def sleep_for_s(s: int) -> str:
    time.sleep(s)
    return f"Slept for {s} seconds"

if __name__ == "__main__":
    executor = ProcessPoolExecutor()
    futures = [executor.submit(sleep_for_s, i) for i in range(1, cpu_count() + 1)]
    for future in as_completed(futures):
        print(future.result())