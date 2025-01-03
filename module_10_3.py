import threading
from random import randint
from threading import Lock, Thread
from time import sleep


class Bank:
    def __init__(self, balance: int = 0, lock: Lock = Lock()):
        self.balance = balance  # баланс банка
        self.lock = lock  # объект класса Lock для блокировки потоков

    def deposit(self):
        for i in range(100):
            transfer = randint(50, 500)
            self.balance += transfer
            print(f'Пополнение: {transfer}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            transfer = randint(50, 500)
            print(f'Запрос на {transfer}')
            if transfer <= self.balance:
                self.balance -= transfer
                print(f'Снятие: {transfer}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

if __name__ == '__main__':
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')


