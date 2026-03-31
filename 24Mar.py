"""
def get_name() -> str:
    name = input("Enter your name: ")
    return name

def get_home() -> str:
    home = input ("Where are you from: ")
    return home

  #  print (f"Hello {name}!")

 #greet()   
def greet(name: str, home: str="the moon"):
#def greet(name, home="the moon"):
    print(f"Hello {name}! I´ve never been to {home}.")

username = get_name()
userhome = get_home()
#userhome ="" - None and empty value considered as a true value
#greet(username, userhome)
#greet(name=username, home=userhome)
#greet(name=username, home=userhome)
greet(2026, 14.76)
#set_values(age=30, height=176, weight=87)
"""


def avg_temp(*args: float, id: str)-> float:
    print(type(args))
    total = 0.0

    for item in args:
        total +=item
    print (f"Accumulative temps for {id}:{total}")    

    average = total / len(args)
    return average
#print(avg_temp( 12.5, 34.8, 27.3245, id="February Temps"))   
#print(avg_temp(14.87, 0, -2.7, 9.7485, 34.8898, 13.748, id="March Temps"))   
"""
def configure_laptop(**kwargs:dict):
    print(type(kwargs))

    print("\nYour laptop configuration will be:\n")

    for k, v in kwargs.items():
        print(f"         {k}: {v}")

configure_laptop (Manufacturer ="Asus", Size ="17", processor="Intel core 13", Memory ="24GB")        
configure_laptop (Storage ="SSD", Color ="Blue", Manufacturer ="Apple", Memory ="16GB")        
"""

"""
def fn(a, /, b, c=3, *pc, e=4, **kc):
    print(f"a={a}, b={b}, c={c}, pc={pc}, e={e},kc={kc}")
fn (0, 1, 2, 3, 4, e=5, f=6, g=7)
"""     
