import unittest
import basic

unittest.TestCase.shortDescription = lambda x: None  # don't show docstring


class TestBasic(unittest.TestCase):
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

    def test_show_docstring(self):
        '''
        Function: basic.get_reminder.__doc__
        Mehtod: basic.People.__doc__
        '''
        pass

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

    def test_exnter_and_exit_example(self):
        """
        __enter__ and __exit__
        with >> enter >> do something >> exit
        """

        with basic.EnterExitExampler() as handler:
            print("do_something")

    def test_call_example(self):
        """
        __call__ and __exit__
        """
        handler = basic.CallExampler()
        self.assertEqual(handler(), True)

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

    def test_annotations(self):
        """
        __annotations__
        basic.get_reminder.__annotations__
        """
        pass

    def test_get_attributes(self):
        """
        check all of __ type attributes
        Method 1:
        handler = basic.EnterExitExampler()
        print(dir(handler))
        Method 2:
        print(hasattr(handler, '__iter__'))
        """
        pass

    def test_get_attributes(self):
        """
        check all of __ type attributes
        Method 1:
        handler = basic.EnterExitExampler()
        print(dir(handler))
        Method 2:
        print(hasattr(handler, '__iter__'))
        """
        pass

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


if __name__ == '__main__':
    unittest.main()
