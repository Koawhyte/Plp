def fileCreation():
    myDairy = input("Please Enter Your Filename")

    try:
        with open("myDairy.txt", "r") as file:
            contents = file.read()

        
            newContent = contents.upper()

        with open("Dairy.txt", "w") as file:
            file.write(newContent)
            print("file modified successfully.")

    except FileNotFoundError:
        print(f"sorry the file {myDairy} does not exist")

    except PermissionError:
        print(f"sorry you do not have the permission to view {myDairy}")

    except Exception as e:
        print(f"An error occurred {e}")             
            
fileCreation()