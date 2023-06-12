import time

start = time.perf_counter()


def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
	results = [executor.submit(do_something, 1) for _ range(10)]

