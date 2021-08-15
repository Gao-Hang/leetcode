# 多个装饰器的装饰过程就是：离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程
# https://www.runoob.com/w3cnote/python-func-decorators.html
from functools import wraps


# 可调用对象 __call__



class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass


@logit()
def myfunc1():
    pass


# 现在，我们给logit创建子类，来添加email的功能(虽然email这个话题不会在这里展开)。

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass


@email_logit()
def myfunc1():
    pass

# 从现在起，@email_logit将会和 @ logit产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。


# 简单点
def decorator(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        log_string = func.__name__ + " was called"
        print(log_string)
        return func(*args, **kwargs)

    return wrapped_function
