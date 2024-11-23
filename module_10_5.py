from datetime import datetime
from multiprocessing import Pool


def read_info(name):          #name - название файла
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for name in filenames:
        read_info(name)
    print(datetime.now() - start_time, '(линейный)')

    start_time = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start_time, '(многопроцессный)')