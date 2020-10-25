# Во время парсинга встроенного локальных переменных, заполняем поле message

class message:
    """
    Если во время парсинга локальных переменных функции среди них обнаруживается экземпляр данного класса, содержимое экземпляра используется как текст сообщения при логировании.
    Это позволяет не делать лишних логов внутри функции, а лишь модифицировать поведение декоратора.
    """
    def __init__(self, text):
        """
        Аргумент функции приводится к типу str.
        """
        self.message = str(text)

    def __repr__(self):
        full_string = f'message("{self.message}")'
        return full_string
