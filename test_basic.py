
from calendar import c
import unittest
import basic
import os
import classdemo
import sys

'''
python3 -m unittest -v test_basic.py
don't show docstring:
unittest.TestCase.shortDescription = lambda x: None
'''

unittest.TestCase.shortDescription = lambda x: None

variable = 5


class TestBasic(unittest.TestCase):

    def test_while(self):
        while False:
            self.fail("Should not happened")

    def test_if_else(self):
        if False:
            self.fail("Should not happened")
        elif False:
            self.fail("Should not happened")
        else:
            pass

    def test_variable_memoey_comparsion(self):
        list_float = [0.0]*1000
        list_int = [0]*1000
        tuple = (0)*1000
        string = ""*1000
        self.assertEqual(sys.getsizeof(list_float), 8056)
        self.assertEqual(sys.getsizeof(list_int), 8056)
        self.assertEqual(sys.getsizeof(string), 49)
        self.assertEqual(sys.getsizeof(tuple), 24)

    def test_regular_expression(self):  # unfinished
        ''' statement '''
        pass

    def test_boolean(self):
        '''
        isinstance: check instance
        '''
        self.assertEqual(bool("Hello"), True)
        self.assertEqual(bool(15), True)
        self.assertEqual(10 > 9, True)
        self.assertEqual(bool(False), False)
        x = 100
        self.assertEqual(isinstance(x, int), True)

    def test_casting(self):
        ''' type translation '''
        self.assertEqual(int(2.8), 2)
        self.assertEqual(int("3"), 3)
        self.assertEqual(float(3), 3.0)
        self.assertEqual(float("3.2"), 3.2)
        self.assertEqual(str(3.2), "3.2")

    def test_scope_nonlocal_variable(self):
        ''' nonlocal: let inner function to use outer local variable '''
        variable = 10

        def inner_function():
            variable = 20
            return variable+1

        def second_inner_function():
            nonlocal variable
            variable = 12
            return variable+1

        def third_inner_function():
            global variable
            return variable+1

        ''' case 1
        global = 5
        local = 10
        local > global, output 10 
        '''
        self.assertEqual(variable, 10)

        ''' case 2
        global = 5
        local = 10
        inner = 20, then inner function end, inner is recycled
        local > global, output 10 
        '''

        self.assertEqual(inner_function(), 21)
        self.assertEqual(variable, 10)

        ''' case 3
        global = 5
        local = 12
        keyword nonlocal: let inner inherit local, so inner = local = 12
        then: innert = local = 12 > global 
        '''
        self.assertEqual(second_inner_function(), 13)
        self.assertEqual(variable, 12)
        ''' case 4
        global = 5
        local = 20 (update by the case 3)
        keyword global: let inner inherit global, so inner = global = 5
        inner = local = 12 > global, output 20
        '''
        self.assertEqual(third_inner_function(), 6)
        self.assertEqual(variable, 12)

    def test_check_variable_scope(self):
        variable = 10

        def get_result():
            b = 5

            def return_c():
                c = 1
                return b+c
            return variable+return_c()
        self.assertEqual(get_result(), 16)
        self.assertEqual('variable' in globals(), True)
        self.assertEqual('variable' in locals(), True)

    def test_lazy_binding(self):
        ''' Issue: closure return a funtion'''
        def return_print_function():
            result = []
            for i in range(3):
                ''' 
                because python closure is using lazy binding,
                result should be [fx+0(),fx+1(),fx+2()] 
                but result = [fx+2(),fx+2(),fx+2()] 
                '''
                result.append(lambda x: x+i)
            return result

        for f in return_print_function():
            self.assertEqual(f(2), 4)

        ''' solution 1: Factory Template '''
        def add_n(n):
            return lambda x: x+n

        def get_add_n_list():
            '''
            result=[add_0(),add_1(),add_2()]
            '''
            result = []
            for i in range(3):
                result.append(add_n(i))
            return result

        i = 0
        for f in get_add_n_list():
            '''
            loop 1: add_0(1), answer=1+0
            loop 2: add_1(1), answer=1+1
            loop 3: add_2(1), answer=1+2
            '''
            self.assertEqual(f(1), 1+i)
            i += 1

        ''' solution 2: Update lambda argument (demo only) 
        def generate_funcs():
            funcs = []
            for i in range(5):
                funcs.append(lambda i=i: print(i))
            return funcs
            
        for f in generate_funcs():
            f()
        '''

        ''' solution 3: Yeild'''
        def get_add_n_list_thrid():
            for n in range(3):
                yield lambda x: x+n
        i = 0
        for f in get_add_n_list_thrid():
            self.assertEqual(f(1), 1+i)
            i += 1

    def test_lambda(self):
        self.assertEqual((lambda x, y: x*y)(4, 2), 8)
        self.assertEqual((lambda x: x)(4), 4)

    def test_closure(self):
        ''' anonymous function '''

        ''' fundamental '''
        def two_sum(a, b): return a + b
        self.assertEqual(two_sum(5, 6), 11)
        def three_sum(a, b, c): return a + b + c
        self.assertEqual(three_sum(1, 2, 3), 6)

        ''' lazy binding and closure '''
        def add_n(n):
            return lambda input: input + n
        add_3 = add_n(3)
        self.assertEqual(add_3(1), 4)
        add_5 = add_n(5)
        self.assertEqual(add_5(1), 6)

    def test_operator(self):
        ''' ~ not, inverse bits '''
        self.assertEqual(~8, -9)

        ''' binary operator '''
        self.assertEqual(3+2, 5)
        self.assertEqual(3-2, 1)
        self.assertEqual(3*2, 6)
        self.assertEqual(3/2, 1.5)
        self.assertEqual(33 % 2, 1)
        ''' exponentiation '''
        self.assertEqual(3**2, 9)
        '''	floor division'''
        self.assertEqual(3//2, 1)
        ''' & and'''
        self.assertEqual(3 & 3, 3)
        ''' | or'''
        self.assertEqual(3 | 3, 3)
        ''' ^ xor'''
        self.assertEqual(3 ^ 3, 0)
        self.assertEqual(5 == 5, True)
        self.assertEqual(5 != 5, False)
        self.assertEqual(not 5 == 5, False)
        self.assertEqual(5 >= 5, True)
        self.assertEqual(6 > 5, True)
        self.assertEqual(6 < 5, False)
        self.assertEqual(6 in [4, 5], False)
        self.assertEqual(6 not in [4, 5], True)
        self.assertEqual(True and True, True)
        self.assertEqual(True and False, False)
        self.assertEqual(not False, True)
        self.assertEqual(True or False, True)
        self.assertEqual(5 > 4 > 3, True)

        '''
        x>>1 is equal x*2
        x<<1 is equal x/2
        13<<1 is equal x//2
        '''
        self.assertEqual(6 >> 1, 3)
        self.assertEqual(6 >> 2, 1)
        self.assertEqual(13 >> 1, 6)
        self.assertEqual(13 >> 2, 3)
        self.assertEqual(6 << 1, 12)
        self.assertEqual(6 << 2, 24)

        '''x+=1, x=x+1'''
        x = 3
        x += 1
        self.assertEqual(x, 4)
        x = 5
        x -= 2
        self.assertEqual(x, 3)
        x = 5
        x *= 2
        self.assertEqual(x, 10)
        x = 50
        x /= 2
        self.assertEqual(x, 25)
        x = 5
        x %= 2
        self.assertEqual(x, 1)
        x = 5
        x **= 2
        self.assertEqual(x, 25)
        x = 52
        x //= 5
        self.assertEqual(x, 10)
        x = 5
        x &= 5
        self.assertEqual(x, 5)
        x = 5
        x ^= 5

        ''' ternary conditional operator '''
        status = True
        flag = True if status else False
        self.assertEqual(flag, True)

    def test_get_reminder(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat([5, 3], 2))
        cases.append(TestFormat([15, 3], 0))
        cases.append(TestFormat([52, 3], 1))
        cases.append(TestFormat([535, 7], 3))

        for case in cases:
            result = basic.get_reminder(case.args[0], case.args[1])
            self.assertEqual(result, case.wants)

    def test_show_xor_example(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat([3, 0], 3))
        cases.append(TestFormat([3, 3], 0))
        cases.append(TestFormat([15, 3], 12))
        cases.append(TestFormat([52, 3], 55))
        cases.append(TestFormat([535, 7], 528))

        for case in cases:
            result = basic.show_xor_example(case.args[0], case.args[1])
            self.assertEqual(result, case.wants)

    def test_show_xor_example(self):
        '''
        class property - encapsulation
        '''
        handler = basic.PropertyExampler('abc@yahoo.com')
        self.assertEqual(handler.email_special_api, 'abc@yahoo.com')
        handler.email_special_api = 'hello@world.com'
        self.assertEqual(handler.email_special_api, 'hello@world.com')
        del handler.email_special_api
        try:
            handler.email_special_api
        except:
            self.assertTrue(True)

    def test_dynamic_check_id(self):
        '''
        dynamic check attribute
        extension management
        '''
        handler = basic.CheckDataExampler(
            '123456', basic.CheckDataExampler.check_id)
        self.assertEqual(handler.update_id('123'), False)
        self.assertEqual(handler.update_id('666666'), True)

    def test_unittest_fail(self):
        """
        unittest
        fail
        shouldn't happen
        """
        try:
            pass
        except:
            self.fail("shouldn't happen")

    def test_two_dynamic_array(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat([5, 3], [5, 3]))
        cases.append(TestFormat([6, 2], [6, 2]))

        for case in cases:
            result = basic.create_two_dynamic_array(case.args[0], case.args[1])
            self.assertEqual(len(result), case.wants[0])
            for row in result:
                self.assertEqual(len(row), case.wants[1])

    def test_string_format(self):
        ''' multiple values '''
        string = "{} {}".format('Hello', 'World')
        self.assertEqual(string, "Hello World")

        ''' named index'''
        string = "{first}{second}".format(first='1', second='2')
        self.assertEqual(string, "12")

        string = "The price is {:.2f} dollars".format(50)
        self.assertEqual(string, "The price is 50.00 dollars")

        ''' index numbers '''
        string = "His name is {1}. {1} is {0} years old.".format(
            20, "John")
        self.assertEqual(string, "His name is John. John is 20 years old.")

    def test_raw_string(self):
        '''
        raw string
        let string will not be effected with an escape character '\'
        '''
        string = 'Hi\nHello'
        raw_string = r'Hi\nHello'
        self.assertNotEqual(string, raw_string)

    def test_read_file(self):
        '''
        read file
        '''
        filename = "file.txt"
        write_data = "Hello, world."
        import_date = None
        with basic.File(filename, "w") as f:
            f.write(write_data)

        with basic.File(filename, 'r') as f:
            import_date = f.read()

        self.assertEqual(import_date, write_data)
        os.remove(filename)

    def test_map(self):
        def square(x):
            return x*x
        self.assertEqual(square(2),  4)
        self.assertEqual(list(map(square, [1, 2, 3])), [1, 4, 9])

        ''' with lambda'''
        self.assertEqual(list(map(lambda x: x ** 2, [1, 2, 3])), [1, 4, 9])

    def test_yield(self):  # unfinished
        ''' basic '''
        def countdown(n):
            i = 0
            while i < n:
                i += 1
                yield i
        counter = countdown(5)
        self.assertEqual(next(counter), 1)
        self.assertEqual(next(counter), 2)

    ''' os serial '''

    def test_run_os_remove(self):
        ''' remove file '''
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")
        else:
            pass

        ''' remove direct '''
        if os.path.exists("myfolder"):
            os.rmdir("myfolder")
        else:
            pass

    ''' datatype '''

    def test_set(self):
        '''
        Unordered
        Unchangeable
        Duplicates Not Allow
        '''

        data = set({"a", "a", "b", "b", "c", "c"})
        self.assertEqual("c" in data, True)
        self.assertEqual(len(data), 3)
        data.add("d")
        self.assertEqual(len(data), 4)
        data.clear()
        self.assertEqual(len(data), 0)

        ''' unordered '''
        flag = True
        try:
            self.assertEqual(data[0], 3)
            flag = False
        except:
            pass
        if not flag:
            self.fail("shouldn't happen")

        ''' not allow duplicate '''
        pass

        ''' Intersection '''
        result = {"a", "b"} & {"b", "c"}
        self.assertEqual(result, {"b"})

        ''' Union '''
        result = {"a", "b"} | {"b", "c"}
        self.assertEqual(result, {"a", "b", "c"})

        ''' Difference '''
        result = {"a", "b"} - {"b", "c"}
        self.assertEqual(result, {"a"})
        x = {"a", "b"}
        y = {"b", "c"}
        result = x.difference(y)
        self.assertEqual(result, {"a"})

    def test_tuple(self):
        '''
        Orderd
        Immutable
        Allow Duplicates
        '''
        tup = tuple([1, 5, 7, 9, 3])
        self.assertEqual(tup[0], 1)
        try:
            tup[0] = 1
            self.fail("shouldn't happen")
        except:
            pass

    def test_list(self):  # unfinished
        self.assertEqual(all([True, True, True]), True)
        self.assertEqual(all([True, True, False]), False)

    def test_dictionary(self):
        table = dict()
        table['name'] = 'ken'
        table['age'] = 29
        table['email'] = 'hello@word.com'

        self.assertEqual(len(table), 3)
        self.assertEqual(len(table.keys()), 3)
        self.assertEqual(len(table.values()), 3)
        self.assertEqual('name' in table.keys(), True)
        self.assertEqual('ken' in table.values(), True)
        self.assertEqual(table['name'], 'ken')

        table['name'] = 'may'
        self.assertEqual(table['name'], 'may')

        table.update({'name': 'wen'})
        self.assertEqual(table['name'], 'wen')

        table = {
            'name': 'ken'
        }
        self.assertEqual('ken' in table.values(), True)

    ''' class '''

    def test_inheritance_private(self):
        '''
        private method and attribute can not be inheritance
        '''
        b = classdemo.B()
        self.assertEqual(b.message, ['A.private()', 'B.public()'])

    ''' class __ serial '''

    def test_show_docstring(self):
        '''
        Function: basic.get_reminder.__doc__
        Mehtod: basic.People.__doc__
        '''
        pass

    def test_enter_and_exit_example(self):
        """
        __enter__ and __exit__
        with >> init >> enter >> do something >> exit
        """

        with basic.EnterExitExampler() as handler:
            handler.message.append("do_something")

        self.assertEqual(
            handler.message,
            ['__init__', '__enter__', 'do_something', '__exit__'])

    def test_call_example(self):
        """
        __call__
        """
        handler = basic.CallExampler()
        self.assertEqual(handler(), True)

    def test_get_attributes(self):
        """
        __iter__
        check all of __ type attributes
        Method 1:
        handler = basic.EnterExitExampler()
        print(dir(handler))
        Method 2:
        print(hasattr(handler, '__iter__'))
        """
        pass

    def test_iterator(self):  # unfinished
        '''
        next, iter
        iterator and iterable are not the same
        '''
        pass

    def test_annotations(self):
        """
        __annotations__
        basic.get_reminder.__annotations__
        """
        pass

    def test_structure_and_destructure(self): #unfinished
        ''' callback and factory template example '''

        ''' first trial '''
        def callback(data):
            self.assertEqual(data, "__del__")
        test = classdemo.StructureDemo(callback)
        self.assertEqual(test(), "__call__")
        del test

        ''' second trial '''
        def callbacl_init(data):
            self.assertEqual(data, "__init__")

        def callbacl_new(data):
            self.assertEqual(data, "__new__")

        def callbacl_del(data):
            self.assertEqual(data, "__del__")

        handler = classdemo.DemoClass(
            callbacl_init, callbacl_new, callbacl_del)
        # self.assertEqual(handler(), "__call__")
        del handler


if __name__ == '__main__':
    unittest.main()
