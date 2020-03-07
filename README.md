Soldatov Denis
1.How did you understand what is interface in Software Engineering?

Интерфейсы  - это некое формальное представление, для какого-то вида классов. Позволяет нам создавать много классов с похожим поведением.

2.Provide some example of interface in Python.
Java:
	public interface Messenger	{

     public void get_all_messages();

     public void send_message();
}

Python:
from abc import ABC, abstractmethod

3.
class BaseObject(ABC):

    @abstractmethod
    def description(self): pass

    @abstractmethod
    def short_description(self): pass

4.
class IPrint(ABC):
    @abstractmethod
    def print_(self, str): pass

class ConsolePrinter:
	def __init__(self):
		pass
    
    def print_(self, str):
    	print(str)

class FilePrinter:
    def __init__(self, printer):
		self.file = file
    
    def print_(self, str):
    	with open(file, wb) as f:
    		f.write(str)
5.
	class BaseObject():
		def __init__(self, desc, short_desc):
			self.desc = desc
			self.short_desc = short_desc
		
	    def description(self): 
	    	return desc
    		#FilePinrter(printer).print(desc)
	    def short_description(self):
	    	return short desc
    		#FilePinrter(printer).print(desc)

2 Раздел
	

1. What do you think about layering of applications?

Разбитие на слои приложения помогает сделать код более масштабируемым и читаемым. Правильная архитектура приложения может ускорить разработку, вникание в проект и последующее улучшение

2. на листочке
3. на листочке

3 Раздел

1. https://github.com/dsoldatow/software-engeneering-python/tree/lecture3

2. Интерфейсы Объектов BaseObject и Команд BaseCommand (абстрактные классы), Классы объектов (Numbers), command/ Реализация команд (implementation)

3. GUI - консоль, Implementation - реализация команд, бизнес логика объекты и взаимодействие с ними, интерфейсы - interfaces
