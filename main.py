from package1.hello import hello_from_package1
from package2.hello import hello_from_package2
from package2.hello import hello_with_name_package1


if __name__ == "__main__":
	hello_from_package1()
	hello_from_package2()
	hello_with_name_package1()