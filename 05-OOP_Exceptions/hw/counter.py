"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.instances_counter = 0

    def __new__(cls, *args, **kwargs):
        cls.instances_counter += 1
        return super(cls, cls).__new__(cls)

    @classmethod
    def get_created_instances(cls):
        return cls.instances_counter

    @classmethod
    def reset_instances_counter(cls):
        inst_count_before_reset = cls.instances_counter
        cls.instances_counter = 0
        return inst_count_before_reset

    cls.__new__ = __new__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3