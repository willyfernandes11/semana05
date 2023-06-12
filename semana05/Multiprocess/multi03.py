import time

start = time.perf_counter()


def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	return 'Done sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executor:
	f1 = executor.submit(do_something, 1)
	f2 = executor.submit(do_something, 1)

	print(f1.result())
	print(f2.result())

processes = []

for _ in range(10):
	p = multiprocessing.Process(target=do_something, args=[1.5])
	p.start()
	processes.append(p)

for process in processes:
	process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)'s)