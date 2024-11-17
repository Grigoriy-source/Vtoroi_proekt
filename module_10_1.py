import threading
import time


def write_words(word_count, file_name):
    # word_count - количество записываемых слов
    # file_name - название файла, куда будут записываться слова
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(1, word_count + 1 ):
            file.write(f'Какое-то слово № {word}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


current_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

curr_time = time.time()
print(f'Работа функций: {curr_time - current_time}')

run_time = time.time()

thread = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread1 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread2 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread3 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread.start()
thread1.start()
thread2.start()
thread3.start()

thread.join()
thread1.join()
thread2.join()
thread3.join()

start_time = time.time()
print(f'Работа потоков: {start_time - run_time}')

