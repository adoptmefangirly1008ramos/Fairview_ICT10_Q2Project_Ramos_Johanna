from pyscript import document,display

#Homepage: Club Member Checker

#list of ICT club members.
names = ['Enzo Ruiz', 'Logan Anaque', 'Johanna Ramos', 'Joshua Ortiz', 'Renn Santos', 'Jhoana Evangelista'] 

def check_name(e):
    
    document.getElementById("output1").innerHTML = " " #clears previous output

    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    full_name = f"{first_name.strip()} {last_name.strip()}".title() 
    #combines the first and last names into one full name
    #removes extra spaces and standardize capitalization

    is_name = full_name in names #checks whether the full name is in the names list

    #results: shows whether the person is part of the ICT club.
    message = {
        True: "Congratulations " + full_name + "! You are now part of the ICT club.",
        False: "Sorry " + full_name+ ", your name is not on the list."
    } 

    #displays membership verification results
    display(message[is_name], target="output1") 


#School Club Members

def check_nam(e):

    # members of each grade
    grade_7 = {"James Anderson", "Daithi Lynch", "Darragh Kelly", "Olivia Harris","William Carter" }
    grade_8 = {"Jaja Godino", "Julienne Miranda", "Chloe Almiron","Jacob Minguillo", "Shari Cruz"
    }
    grade_9 = {"Bob Brown","Johnny Mendoza",  "Emma Flores","Alice Palace","Megan Gacita"
    }
    grade_10 = {"Enzo Ruiz", "Logan Anaque","Johanna Ramos","Hope Benitez", "Cedric Velasco"
    }

    # to get the values of members
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value
    full_name = first_name + " " + last_name + '(The newest member)'

    #combines all members together
    all_members = grade_7 | grade_8 | grade_9 | grade_10
    
    # add the new member
    all_members.add(full_name)

    # count the total number of members
    total_members = len(all_members)
    
    #organize the members alphabetically
    members_list = "<br>".join(sorted(all_members))

    document.getElementById("output1").innerHTML = (
    f"All members: <br> {members_list} <br>"
    f"Total members: {total_members}"
    )


# ELEMENTS
# dictionary containing element information 
nonmetals= {"H" : ("Hydrogen", 1, 1.008), #all non metal elements
                #    1       2    3
            "h" : ("Hydrogen", 1, 1.008),
            "He" : ("Helium", 2, 4.0026),
            "he" : ("Helium", 2, 4.0026),
            "C" : ("Carbon", 6, 12.011),
            "c" : ("Carbon", 6, 12.011),            
            "N" : ("Nitrogen", 7, 14.007),
            "n" : ("Nitrogen", 7, 14.007),
            "O" : ("Oxygen", 8, 15.999),
            "o" : ("Oxygen", 8, 15.999),
            "F" : ("Flourine", 9, 18.998),
            "f" : ("Flourine", 9, 18.998),
            "Ne" : ("Neon", 10, 20.180),
            "ne" : ("Neon", 10, 20.180),            
            "P" : ("Phosphorus", 15, 30.974),
            "p" : ("Phosphorus", 15, 30.974),
            "S" : ("Sulfur", 16, 32.06),
            "s" : ("Sulfur", 16, 32.06),
            "Cl" : ("Chlorine", 17, 35.45),
            "cl" : ("Chlorine", 17, 35.45),
            "Ar" : ("Argon", 18, 39.948),
            "ar" : ("Argon", 18, 39.948),
            "Se" : ("Selenium", 34, 78.971),
            "se" : ("Selenium", 34, 78.971),
            "Br" : ("Bromine", 35, 79.904),
            "br" : ("Bromine", 35, 79.904),
            "Kr" : ("Krypton", 36, 83.798),
            "kr" : ("Krypton", 36, 83.798),
            "I" : ("Iodine", 53, 126.90),
            "i" : ("Iodine", 53, 126.90),
            "Xe" : ("Xenon", 54, 131.29),
            "xe" : ("Xenon", 54, 131.29),
            "Rn" : ("Radon", 86, 222),
            "rn" : ("Radon", 86, 222),
        }

# Element Symbol, Element Name, Atomic Number, Atomic Mass

#fuction to search for the element's information
def search_element(e):
    # Get the input from HTML
    Nonmetal1= document.getElementById("element1").value
    #retrieve information from dictionary
    result = nonmetals.get(Nonmetal1, ("Element not found", "-", "-"))  #display the result in html
    # symbol, name, number, mass
    document.getElementById("symbol").innerText = Nonmetal1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]




