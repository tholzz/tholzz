vehicles=["bike","car","van"]
charges=[300,1000,1500]
availble=[True,True,True]


customer=""
vehicle_name=""
days=0
amount=0

while True:
    print("\n1.Display vehicles")
    print("2.rent vehicle")
    print("3.return vehicle")
    print("4.view rent details")
    print("5.exit")

    choice=int(input("enter choice:"))

    if choice==1:
        print("\navailable vehicles:")
        for i in range(len(vehicles)):
            if available[i]:
                print(vehicles[i],"rs.",charges[i],"perday")

    elif choice==2:
        customer=input("enter customer name:")
        vehicle_name=input("enter vehicles(bike\car\van):")

        if vehicle_name in vehicles:
           i=vehicles.index(vehicle_name)

           if available[i]:
               days=int(input("enter number of days:"))
               amount=days*charges[i]
               available[i]=false
               print("vehicle rented successfully")
               print("rental charge =rs.",amount)
           else:
              print("vehicle not available")
        else:
              print("invalid vehicle")
            

    elif choice==3:
        vehicle_name=input("enter vehicle name to return:")
        if vehicle_name in vehicles:
          i=vehicle.index(vehicle_name)
          available[i]=True
          print("vehicle returned successfully")
        else:
          print("invalid vehicle") 
    elif choice==4:
        print("\nrental details")
        print("days:",days)
        print("total amount :Rs",amount)

    elif choice==5:
        print("thank you")
        break
    else:
        print("valid choice")
