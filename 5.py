def morgens_to_sqm(x):
    return (x / 0.38685)

def create_list(x):
    number_list = []
    for i in range(1,x+8):
        if i % 2 == 0:
             number_list.append(i)
    return number_list

morgens = 17.5
sqm = morgens_to_sqm(morgens)
print(f"{morgens:.2f} Schaumburg's morgens = {sqm:.2f} square meters")


number = 7
even_list = create_list(number)
print(f"{number} even numbers: " + str(even_list))

