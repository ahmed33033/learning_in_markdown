from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def sleep_for_s(s: int) -> str:
    time.sleep(s)
    return f"Done sleeping for {s} seconds."

executor = ThreadPoolExecutor()
futures = [executor.submit(sleep_for_s, i) for i in range(1, 4)]

for future in as_completed(futures):
    print(future.result())

executor.shutdown()