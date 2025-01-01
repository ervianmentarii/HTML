from abc import ABC, abstractmethod # type: ignore

class Button(ABC):
    def __init__(self,link):
        self.link=link
    @abstractmethod
    def click(self):
        pass
    @property
    @abstractmethod
    def link(self):
        pass
class Pushbutton(Button):
    def click(self):
        print("Go to :{}".format(self.link))
    @Button.link.getter
    def link(self):
        return self.__link
    @link.setter
    def link(self,input):
        self.__link=input
button=Pushbutton("www.id.com")
button.click()
