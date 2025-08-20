def document():
    myDiary = input("please enter your filename:")
    try:
        with open(myDiary, "r") as file:
          content = file.read()

        NewContent = content.upper()

        Diaries = f"{NewContent}"
        with open(Diaries, "w") as Newfile:
          Newfile.write(NewContent)
        print(f"file modified successfully. new file saved as{Diaries}")

    except FileNotFoundError:
      print(f"sorry the file {myDiary} does not exist")
    except PermissionError:
      print(f"sorry you do not have permission to read the file{myDiary}")
    except Exception as e :
      print(f"An error occurred:{e}")

document()