def Weight():
    weight_on_earth = int(input("Enter your wieght on Earth : "))
    weight_on_moon = (weight_on_earth/9.81)*1.622
    weight_on_mercury = (weight_on_earth/9.81)*3.7
    weight_on_venus = (weight_on_earth/9.81)*8.87
    weight_on_mars = (weight_on_earth/9.81)*3.711
    weight_on_jupiter = (weight_on_earth/9.81)*24.79
    weight_on_saturn = (weight_on_earth/9.81)*10.44
    weight_on_uranus  = (weight_on_earth/9.81)*8.69
    weight_on_neptune = (weight_on_earth/9.81)*11.15
    weight_on_sun = weight_on_earth*28
    
    print(f"Your weight on sun will be : {weight_on_sun}")
    print(f"Your weight on moon will be : {weight_on_moon}")
    print(f"Your weight on moon will be : {weight_on_moon}")
    print(f"Your weight on mercury will be : {weight_on_mercury}")
    print(f"Your weight on venus will be : {weight_on_venus}")
    print(f"Your weight on mars will be : {weight_on_mars}")
    print(f"Your weight on jupiter will be : {weight_on_jupiter}")
    print(f"Your weight on saturn will be : {weight_on_saturn}")
    print(f"Your weight on uranus will be : {weight_on_uranus}")
    print(f"Your weight on neptune will be : {weight_on_neptune}")
    

Weight()