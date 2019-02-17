def shut_down(s):
    if s == "yes" or s == "Yes":
        print("Shutting down")
    elif s == "no" or s == "No":
        print("Shutdown aborted")
    else:
        print("Sorry")


s = input("Shut Down:")
shut_down(s)

