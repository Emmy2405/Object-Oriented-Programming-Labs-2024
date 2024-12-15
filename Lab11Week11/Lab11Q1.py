class TestClass(object):


  def __init__(self,param_str=''):
    self.the_str=''
    for c in param_str:
      if c.isalpha():
        self.the_str += c


  def __add__(self,param):
    if type(param)==TestClass:
      the_str = self.the_str + param.the_str
      return TestClass(the_str)
    else:
      return self


  def __str__(self):
    return 'Value: {}'.format(self.the_str)


inst1 = TestClass('abc')
inst2 = TestClass('123ijk')
sumInst1 = inst1 + inst2
sumInst2 = inst1 + 'xyz'
print(inst1) # Line 1
print(sumInst1) # Line 2
print(sumInst2) # Line 3
print(isinstance(sumInst2,TestClass)) # Line 4


#(a) What output is produced by # Line 1 of the above program?
#(b) What output is produced by # Line 2 of the above program?
#(c) What output is produced by # Line 3 of the above program?
#(d) What output is produced by # Line 4 of the above program?
