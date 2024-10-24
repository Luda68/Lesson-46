""""Методы Юнит-тестирования"
Цель: освоить методы, которые содержит класс TestCase.

Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub.
(Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый
класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую
нужно пробежать и список участников. Также присутствует метод start, который реализует
логику бега по предложенной дистанции.
Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие
методы:
setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который
будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.
Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию
90. У объекта класса Tournament запускается метод start, который возвращает словарь в
переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются
последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя
последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament
соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.
"""
from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_variants = []

    def setUp(self):
        self.first = Runner('Усейн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)
        self.name = "Ник"

    def test_first_tournament(self):
        tournament = Tournament(90, self.first, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == self.name)


    def test_second_tournament(self):
        tournament = Tournament(90, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[2] == self.name)


    def test_third_tournament(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        results = tournament.start()
        TournamentTest.all_variants.append(results)
        self.assertTrue(results[3] == self.name)

    @classmethod
    def tearDownClass(cls):
        for k, v in enumerate(cls.all_variants):
            print(f'{k+1}: {v}')



if __name__ == '__main__':
    unittest.main()



