str=input("enter a string:")
if len(str)<2:
    print("empty string")
else:
    print(str[:2]+str[-2:])