from abc import abstractmethod, ABC


class Protocol(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class IM(Protocol):

    def format(self):
        return ''.join(["I'm ", self.text])


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):

    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: Protocol):
        self.__sender = sender.format()

    def set_receiver(self, receiver: Protocol):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email()
sender = IM('gmal')
receiver = IM('james')
email.set_sender(sender)
email.set_receiver(receiver)
content = HTML('Hello, there!')
email.set_content(content)
print(email)
