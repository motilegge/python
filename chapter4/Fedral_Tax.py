stat= (float(input(" please input filling status. For single type 1 For Mairried type 2 For devorced type 3: ")))
inc= (float(input("please input taxable income: ")))

if stat== 1 :
    tax=0
    if inc<=8350:
        tax=(float(inc*0.1))
    elif inc>8350 or inc<33950:
        tax=(inc*0.15)
    elif inc>33_950 or inc<50_000:
        tax=(inc*0.15)
    elif inc>100000 or inc<150_000:
        tax=(inc*0.28)
    elif inc>150_000 or inc<350_000:
        tax=(inc*0.33)
    elif inc>350_000:
        tax=(inc*0.35)
if stat== 2 :
    tax=0
    if inc<=8350:
        tax=(float(inc*0.1))
    elif inc>8350 or inc<39950:
        tax=(inc*0.15)
    elif inc>39_950 or inc<80_000:
        tax=(inc*0.25)
    elif inc>150000 or inc<180_000:
        tax=(inc*0.28)
    elif inc>180_000 or inc<380_000:
        tax=(inc*0.33)
    elif inc>380_000:
        tax=(inc*0.35)
if stat== 3 :
    tax=0
    if inc<=8350:
        tax=(float(inc*0.1))
    elif inc>8350 or inc<35950:
        tax=(inc*0.15)
    elif inc>35_950 or inc<50_000:
        tax=(inc*0.15)
    elif inc>120000 or inc<170_000:
        tax=(inc*0.15)
    elif inc>170_000 or inc<350_000:
        tax=(inc*0.15)
    elif inc>370_000:
        tax=(inc*0.35)
    
print("Tax is", (tax))


