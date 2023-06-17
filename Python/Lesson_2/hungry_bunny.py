hungry = True
carrots_eaten =0

while hungry:
    #carrots_eaten = carrots_eaten +2
    #print(f"Carrots estean! Total carrots eaten: {carrots_eaten}")

    if carrots_eaten >100000:
        print("oh no! Thats too much!")
        hungry = False
    carrots_eaten = carrots_eaten +1000
    print(f"Carrots estean! Total carrots eaten: {carrots_eaten}")
