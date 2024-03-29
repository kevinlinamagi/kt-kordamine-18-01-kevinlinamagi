import math

"""Kordamine."""


def timeformating(minutes: int) -> str:
    """
    Saad sisendiks minuteid täisarvuna.
    Väljundiks peab olema sõne,
    kus on aeg õiges formaadis. Ehk : 0tundi 0minutit.
    Kontrolli et sisend oleks loogiline.

    Näide
    timeformating(63)-> 1tundi 3minutit
    timeformating(163)-> 2tundi 43minutit

    :param minutes: aeg minutites
    :return: aeg formadiis xtundi xminutit
    """

    if minutes < 60:
        return "Vigane sisend"

    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}tundi ja {remaining_minutes}minutit"

def countvowels(word: str) -> int:
    """
    Sisendiks on sõne, tagasta täishäälikute arv sõnes.
    Tee ise funktsioon-boolean iscontainvowels(word: str),
    mis kontrollib, kas sõnas on üldse täishäälikuid.
    Kui sõnas ei ole täishäälikuid, siis tagastab 0.

    countVowels(LaEvAd) -> 3

    :param word: sõna kus peab täishäälikuid kokku lugema
    :return:
    """

    counter = 0

    for letter in word:
        if letter in "aeiouAEIOU":
            counter += 1

    return counter

def iscontainvowels(word: str) -> bool:

    for letter in word:
        if letter in "aeiouAEIOU":
            return True
        else:
            return False

def longshortstring(a: str, b: str) -> str:
    """
    Sisendiks on kaks sõne, üks on lühem kui teine.
    Alati üks nedest on kas lühem või pikem kui teine.
    Väljundiks peab olema sõne, kus alguses ja lõpus on
    lüheim sõne suurte tähtedega ja nende keskel pikim
    väikeste tähtedega.

    E.g.
    longshortstring(Hello, Hi) -> HIhelloHI

    :param a: sisestatav sõne
    :param b: sisestatav sõne
    :return: sõne alguses ja lõpus - lüheim, keskel pikim
    """

    len_a = len(a)
    len_b = len(b)

    if len_a < len_b:
        return a.upper() + b.lower() + a.upper()
    else:
        return b.upper() + a.lower() + b.upper()

def makeiteven(nums: list) -> list:
    """
    Sisendiks on arvude järjend, kus on nii paaris- kui ka
    paaritud arvud.
    Tagastama peab järjendi kus on ainult paaris arvud.

    E.g.
    makeiteven([1, 1, 2, 5, 8, 9, 12, 6])
    ->
    [2, 8, 12, 6]

    :param nums: järjend täisarvudega
    :return: järjend paarisarvudega
    """
    result = []

    for num in nums:
        if num % 2 == 0:
            result.append(num)

    return result

def speedticket(speed: int, isbirthday: bool) -> int:
    """
    Sisendiks on kiirus ja boolean kas sõidukijuhil
    on sünnipäev või ei ole.
    Tagastab täisarvu kas 0, 1 või 2.
    Lubatud kiirus on 60.

    Iga number vastab erinevatele olukordadele.
    0 - trahvi välja ei kirjutata,
    kuna kiirus ei ole üle lubatud kiiruse.
    1- trahv kirjutatakse välja kuna kiiruseületus
    on 61-79 piires.
    2 - trahv kirjutatakse välja kuna kiiruseületus
    on 80 ja suurem.

    Kui sõidukijuhil on sünnipäev, siis kõik kiirusepiirid
    on 5 võrra suurem.

    E.g.
    speedticket(65,False) -> 1
    speedticket(65,True) -> 0

    :param speed: kiirus täisarvuna
    :param isbirthday: tõeväärsus kas on sünnip. või ei
    :return: täisarv vastavalt olukorrale
    """

    if isbirthday:
        speed = speed - 5

    if speed <= 60:
        return 0

    if speed > 60 and speed < 80:
        return 1

    if speed >= 80:
        return 2

def findarea(figure: int, a: int, b: int) -> float:
    """
    Sisendiks on täisarv 0-3, mis tähistab kujundit:
    0- ruut
    1- rööpkülik
    2- kolmnurk
    3- ring

    Sisendiks on veel täisarvud mis tähistavad
    külje pikkust ning  vajadusel kõrgust või teise külje pikkust.

    Tagastama peab kujundi pindalad float numbrina.
    Kui vaja, siis vastus ümardada kahe komakohani.

    E.g.
    findarea(0,4,4) ->  16
    findarea(3,4,0) -> 50.27
    findarea(1,5,10) -> 50


    :param figure: täisarv, mis tähistab kujundit
    :param a: külje pikkus või raadius
    :param b: teise külje pikkus või kolmnurga kõrgus
    :return: pindala ujukomaarvuna
    """

    if figure == 0:
        result = a * b

    if figure == 1:
        result = a * b

    if figure == 2:
        result = 0.5 * a * b

    if figure == 3:
        PI = 3.141592653589793
        result = PI * (a ** 2)

    result = round(result, 2)
    return result

def salesnight(price: int, sale: int, client: bool) -> str:
    """
    Kui kasutajal on kliendikaart, siis allahindlusprotsent
    on 10% võrra suurem.
    Tavaline allahindlus ei saa olla suurem kui 70%.
    Sellisel juhul allahindlus on 50%.

    E.g.
    salesnight(50,20,False) ->  40.0 €
    salesnight(50,10,True) ->  40.0 €
    salesnight(50,80,True) ->  20.0 €

    :param price: täisarv, mis tähistab hinda
    :param sale: täisarv, mis tähistab allahindluse protsenti
    :param client: tõeväärsus kas on kliendikaart või mitte
    :return: hind peale allahindlust
    """

    if client:
        client_discount = 10
    else:
        client_discount = 0

    if sale >= 79:
        discount = (price * (50 + client_discount)) / 100
    else:
        discount = (price * (sale + client_discount)) / 100

    result = price - discount
    return f"{result} €"


# Krijuta siia kas funktsioon või meetod, mis tagastab või prindib konsooli
# nii mitu rida, kui palju kasutaja sisestab kordi.
# Sinu otsustada kas metood tagastab või prindib konsooli sõne,
# mis on sisestatud kasutja poolt või metoodisse/funktsiooni sisse kirjutatud.

if __name__ == '__main__':
    print(timeformating(163))  # -> 2tundi 43minutit
    print(countvowels("LaEvAd"))  # -> 3
    print(longshortstring("Hello", "Hi"))  # -> HIhelloHI
    print(longshortstring("Hi", "Hello"))  # -> HIhelloHI
    print(makeiteven([1, 1, 2, 5, 8, 9, 12, 6]))    # -> [2, 8, 12, 6]
    print(speedticket(65, False))  # -> 1
    print(speedticket(65, True))  # -> 0
    print(findarea(0, 4, 4))  # -> 16.0 (ruut külgedega 4x4)
    print(findarea(3, 4, 0))  # -> 50.27 (ring raadiusega 4)
    print(salesnight(50, 80, True))   # -> 20.0 €
