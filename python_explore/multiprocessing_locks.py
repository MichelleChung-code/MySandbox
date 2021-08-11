import multiprocessing as mp
import os
import fasteners
from timing_dec import timing


@fasteners.interprocess_locked('temp_lock')
def write_num_to_file(file, count_per_process):
    for n in range(count_per_process):
        with open(file, 'r') as f:
            try:
                num = int(f.read())
            except:
                num = 0
        with open(file, 'w') as f:
            f.write(str(num + 1))


@timing
def run_process(file, counts):
    with open(file, 'w') as f:  # reset back to empty
        pass

    num_cores = mp.cpu_count()

    process_ls = []
    for p in range(num_cores):
        proc = mp.Process(target=write_num_to_file, args=(file, counts))
        proc.start()
        process_ls.append(proc)

    for p in process_ls:
        p.join()  # wait for all the processes to complete before moving on in code

    with open(file, 'r') as f:
        num_actual = int(f.read())

    assert num_actual == int(num_cores * counts)  # check that count is as expected

    os.system('more ' + file)  # view contents of the file


if __name__ == '__main__':
    FILENAME = 'multiprocessing_locks.txt'
    COUNTS = 1000
    run_process(FILENAME, COUNTS)
