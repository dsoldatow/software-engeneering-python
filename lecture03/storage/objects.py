from abc import ABC

from storage.base_object import BaseObject


class Numbers(BaseObject):
    @staticmethod
    def short_description():
        print("Numbers")

    @staticmethod
    def description():
        print("yoy it is Numbers")


class Complex(BaseObject):
    @staticmethod
    def short_description():
        print("Complex")

    @staticmethod
    def description():
        print("yoy it is Complex")


class Integers(BaseObject):
    @staticmethod
    def short_description():
        print("Integers")

    @staticmethod
    def description():
        print("yoy it is Integers")


Objects = {
    'numbers': Numbers,
    'integers': Integers,
    'complex': Complex,
}
