from linklist import DoublyLinkedList

station = DoublyLinkedList()


print("------- Welcome to train management system, Choose on option below -------")
choice = int(input("1. Add urgent arrivals\n2. Add Normal scheduling\n3. Remove train\n4. Quit\nEnter your choice: "))

while choice != 4:
    if choice == 1:
        number = station.add_first(int(input("Input train's ID: ")))
        if station.search(number):
            print("Repeated Train, Try Again")
        else:
            print("Add train complete, Here the updated schedule.")
            station.traversal_forward()
    elif choice == 2:
        number = station.add_last(int(input("Input train's ID: ")))
        if station.search(number):
            print("Repeated Train, Try Again")
        else:
            print("Add train complete, Here the updated schedule.")
            station.traversal_forward()
    elif choice == 3:
        if station.size == 0:
            print("Add the train to schedule first.")
        else:
            number = station.remove_node(int(input("Input train's ID: ")))
            if number:
                print("Remove train complete, Here the updated schedule.\n")
                station.traversal_forward()
            else:
                print("Train's ID not found, Try Again.")

    else:
        print("error\n")
        break
    print("------- Welcome to train management system, Choose on option below -------")
    choice = int(input("1. Add urgent arrivals\n2. Add Normal scheduling\n3. Remove train\n4. Quit\nEnter your choice: "))



if station.size == 0:
    print("Don't have schedule yet.")
else:
    print("Here's the final schedule.")
    station.traversal_forward()

print("Thank you for using train management system.")
    





