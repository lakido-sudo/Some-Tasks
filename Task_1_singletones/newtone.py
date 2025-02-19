class Singleton:
    """
    Класс, реализующий паттерн "Синглтон".

    Этот класс гарантирует, что у него будет только один экземпляр.
    При попытке создать новый экземпляр, будет возвращен уже существующий.

    Атрибуты:
        _instance: Хранит единственный экземпляр класса.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Вызывается при создании нового экземпляра класса.

        Если экземпляр еще не существует, создается новый экземпляр
        и сохраняется в атрибуте `_instance`. Если экземпляр уже существует,
        возвращается существующий.

        Args:
            cls: Ссылка на класс, для которого создается экземпляр.
            *args: Произвольные позиционные аргументы, передаваемые конструктору.
            **kwargs: Произвольные именованные аргументы, передаваемые конструктору.

        Returns:
            Экземпляр класса (единственный).
        """
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        """
        Конструктор класса.

        Инициализирует атрибут `value` только при первом создании экземпляра.

        Args:
            value: Значение для инициализации атрибута `value`.
        """
        if not hasattr(self, 'value'):  # Инициализируем только один раз
            self.value = value


# Пример использования
singleton1 = Singleton("Первый экземпляр")
singleton2 = Singleton("Второй экземпляр")

print(singleton1 is singleton2)  # Вывод: True
print(singleton1.value)  # Вывод: Первый экземпляр
