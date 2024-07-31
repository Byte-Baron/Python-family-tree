father = input("Enter the name of family father : ")

father0 = input(f"Enter the name of {father}'s father : ")
father1 = input(f"Enter the name of {father}'s mother: ")

mother = input("Enter the name of family mother : ")

mother0 = input(f"Enter the name of {mother}'s father : ")
mother1 = input(f"Enter the name of {mother}'s mother : ")

child1 = input("Enter the name of child number 1 : ")
child2 = input("Enter the name of child number 2 : ")
child3 = input("Enter the name of child number 3 : ")

f = open("Test.txt", "w")

f.write(f"                                            {father0}-----{father1}                            {mother0}-----{mother1}\n")
f.write("\n")
f.write(f"                                               {father} ---------------------------------- {mother}\n")
f.write("                                                                  |\n")
f.write("                                                                  |\n")
f.write("                                                                  |\n")
f.write("                                                                  |\n")
f.write("                                                                  |\n")
f.write("                                                  .--------------------------------.\n")
f.write("                                                  |               |                |\n")
f.write("                                                  |               |                |\n")
f.write(f"                                                 {child1}              {child2}               {child3}\n")

f.close()
