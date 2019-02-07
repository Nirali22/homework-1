from task11 import fib
import task12
def test_11():
  assert fib(2)==1
  assert fib(12)==144
def test_12a():
  assert task12.inp.shape[0]==225
  assert task12.inp.shape[1]==31 
def test_12b():
  assert round(task12.pop_2010.sum(),0)==7065
