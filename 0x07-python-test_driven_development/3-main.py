#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
say_my_name()
say_my_name(6, "Stone")
say_my_name("John", {4, 5, 7})
say_my_name([4,5], "Anaya")
say_my_name(None)
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)