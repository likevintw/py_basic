

def get_reminder(dividend: int, divisor: int) -> int:
    '''
    %
    remider
    (5,3)=2
    '''
    return dividend % divisor


def show_xor_example(x, y):
    '''
    x^0=x
    x^x=0
    '''
    return x ^ y


class PropertyExampler:
    '''
    encapsulation
    property
    '''

    def __init__(self, email):
        self.__email = email

    @property
    def email_special_api(self):
        return self.__email

    @email_special_api.setter
    def email_special_api(self, value):
        self.__email = value

    @email_special_api.getter
    def email_special_api(self):
        return self.__email

    @email_special_api.deleter
    def email_special_api(self):
        del self.__email


class CheckDataExampler:
    '''
    dynamic check attribute
    '''
    __id: int

    def __init__(self, id, is_valid_id) -> None:
        self.id = id
        self.is_valid_id = is_valid_id

    def update_id(self, new_id):
        if self.is_valid_id(new_id):
            self.id = new_id
            return True
        return False

    @staticmethod
    def check_id(id):
        if len(id) < 6:
            return False
        return True


class EnterExitExampler:
    def __init__(self) -> None:
        self.message = ["__init__"]

    def __enter__(self):
        self.message.append("__enter__")
        return self

    def __exit__(self, type, value, traceback):
        self.message.append("__exit__")


class CallExampler:
    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        return True


class ItemExampler:
    def __init__(self, key, value):
        self.classmate = {}
        self.classmate[key] = value

    def __getitem__(self, key):
        return self.classmate[key]

    def __setitem__(self, key, value):
        self.classmate[key] = value

    def __delitem__(self):
        del self.classmate


class Iterator:
    def __init__(self) -> None:
        self.index = 0
        self.max = 10

    def __next__(self):
        if self.index < self.max:
            self.index += 1
            return self.index
        else:
            raise StopIteration


def create_two_dynamic_array(raw, column):
    array = [[0]*column]*raw
    return array


class File(object):
    '''
    enter exit Example
    '''

    def __init__(self, filename, mode):
        '''
        setting filename and mode
        '''
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        '''
        open file
        '''
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, type, value, traceback):
        '''
        close file
        '''
        self.open_file.close()
