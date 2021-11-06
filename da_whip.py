dream_wheels = {
    "Tony" : ["Aerox custom 1000cc", "Benz s class", "Brio"],
    "Don" : ["Cadillac one", "Sigra", "Avanza"],
    "Joe" : ["Alphard", "Carry pick up","Civic"],
    "Iko" : ["BMW", "The new BMW", "The old BMW"],
    "JJ" : ["Golf", "Camry", "LFA"]
}

for name, wheels in dream_wheels.items():
    print("\n" + name.title() + " Dream wheels is:")
    for wheel in wheels:
        print("- " + wheel.title())