from package1.hello import hello_with_name


def hello_from_package2():
  print("Hello from package-2!")


def hello_with_name_package1():
  hello_with_name(name = "Python")