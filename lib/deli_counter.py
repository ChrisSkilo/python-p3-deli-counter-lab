def take_a_number(katz_deli, person):
    katz_deli.append(person)
    position = len(katz_deli)
    print(f"Welcome, {person}. You are number {position} in line.")

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
        for i, person in enumerate(katz_deli, start=1):
            line_message += f" {i}. {person}"
        print(line_message)

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")

    
    
    

