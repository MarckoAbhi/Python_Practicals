

class MyNumbers:
  def __iter__(self):
    self.a = 7
    return self

  def __next__(self):
    x = self.a
    self.a += 7
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))