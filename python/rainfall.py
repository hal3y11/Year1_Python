months = ("Jan", "Feb", "Mar", "Apr","May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec")
 
raindata = []
for month in months:
    rainfall = float(input(f"Enter rainfall for {month} (in mm): "))
    raindata.append((month, rainfall))
 
maxrain = 0
for r, rainfall in raindata:
    if rainfall > maxrain:
        maxrain = rainfall
 
for d in range(int(maxrain), 0, -1):
    for month, rainfall in raindata:
        line = 'X' if int(rainfall) >= d else ' '
        print(f"{line:2}  ", end="")
    print()
 
for month, r in raindata:
    print(f"{month:2} ", end="")
print()