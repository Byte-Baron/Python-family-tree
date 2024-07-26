family_info = {}

family_name = input("\nEnter the name of the family: ")
family_info["Family"] = family_name

father_name = input("\nEnter the name of the father: "+"")
mother_name = input("\nEnter the name of the mother: ")
family_info["Father"] = father_name
family_info["Mother"] = mother_name

# Ask if they have any children
have_children = input("\nDo they have any children? (yes/no): ")
if have_children in ("YES","Yes",'yes',"y"):
    num_children = int(input("\nHow many children do they have? "))
    children_names = []
    spouses = []
    grandchildren_names = []
    for i in range(num_children):
        child_name = input(f"\nEnter the name of child {i+1}: ")
        children_names.append(child_name)
        
        # Ask each child if they have a spouse or not
        has_spouse = input(f"\nDoes {child_name} have a spouse? (yes/no): ")
        if has_spouse in ("YES","Yes",'yes',"y"):
            spouse_name = input(f"\nEnter the name of {child_name}'s spouse: ")
            spouses.append((child_name, spouse_name))

        # Ask each if they have any children (grandchildren)
        has_grandchildren = input(f"\nDoes {child_name} have any children? (yes/no): ")
        if has_grandchildren in("YES","Yes",'yes',"y"):
            num_grandchildren = int(input(f"\nHow many children does {child_name} have? "))
            for j in range(num_grandchildren):
                grandchild_name = input(f"\nEnter the name of child {j+1} of {child_name}: ")
                grandchildren_names.append(grandchild_name)

    family_info["Children"] = children_names
    family_info["Spouses"] = spouses
    family_info["Grandchildren"] = grandchildren_names

print("\n" * 40)
print("------------------------------------------------------------------------")
for key, value in family_info.items():
    print(f"                                {key}: {value}\n")
print("------------------------------------------------------------------------")

if have_children in ("NO","No",'no',"n"):
        print(f"\n                         {family_name}'s family tree \n")
        print(f"                              {family_info['Father']}----{family_info['Mother']} ")
