from gilded_rose_refactorizado import *

if __name__ == '__main__':

    item = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    # chequeo herencia __repr__
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

    itemInterfaz = Interfaz()
    itemInterfaz.update_quality()
