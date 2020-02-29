from commands.base_command import BaseCommand
from storage.objects import Objects


class Description:
    @staticmethod
    def info():
        print('DESCRIPTION (OBJECT)')

    @staticmethod
    def run(**kwargs):
        obj = kwargs.get('object')
        if Objects.get(obj) is not None:
            Objects[obj].description()
        else:
            print('ERROR')


class ShortDescription:
    @staticmethod
    def info():
        print('SHORT DESCRIPTION (OBJECT)')

    @staticmethod
    def run( **kwargs):
        obj = kwargs.get('object')
        if Objects.get(obj) is not None:
            Objects[obj].short_description()
        else:
            print("ERROR")


def info():
    print('exit')


class Exit:
    @staticmethod
    def info():
        print('SHORT DESCRIPTION (OBJECT)')
    
    @staticmethod
    def run(**kwargs):
        print("goodbye")
        exit()


Commands = {
    'exit': Exit,
    'short_desc': ShortDescription,
    'desc': Description
}
