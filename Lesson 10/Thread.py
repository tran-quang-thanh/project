from threading import Thread


def tinhtong():
    a = 5 + 6
    print(a)
    return a


def tru():
    a = 5 - 6
    print(a)
    return a

Thread(None, tinhtong).start()
# Thread(tru).start()
tru()

