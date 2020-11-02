def calculate(valuelength, unit):
    global finalunit
    global result
    if selection == 0:
        while True:
            try:
                finalunit = input("What unit do you want to convert to? E.g. m for meters. Enter index for an overview of the supported units.\n")
                if finalunit == "m":
                    if unit == "m":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "cm":
                        result = f"{(float(valuelength) / 100)} m"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) / 10)} m"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 1000)} m"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) * 1000)} m"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 1609.34)} m"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) * 0.9144)} m"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) * 0.3048)} m"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) * 0.0254)} m"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "cm":
                    if unit == "cm":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) * 100)} cm"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) * 10)} cm"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 10)} cm"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) * 100000)} cm"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 160934.4)} cm"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) * 91.44)} cm"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) * 30.48)} cm"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) * 2.54)} cm"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "dm":
                    if unit == "dm":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) * 10)} dm"
                        break
                    elif unit == "cm":
                        result = f"{(float(valuelength) / 10)} dm"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 100)} dm"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) * 10000)} dm"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 16093.44)} dm"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) * 9.144)} dm"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) * 3.048)} dm"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) * 0.254)} dm"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "mm":
                    if unit == "mm":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) * 1000)} mm"
                        break
                    elif unit == "cm":
                        result = f"{(float(valuelength) * 10)} mm"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) * 100)} mm"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) * 1000000)} mm"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 1609344)} mm"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) * 914.4)} mm"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) * 304.8)} mm"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) * 25.4)} mm"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "km":
                    if unit == "km":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) / 1000)} km"
                        break
                    elif unit == "cm":
                        result = f"{(float(valuelength) / 100000)} km"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) / 10000)} km"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 1000000)} km"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 1.609344)} km"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) / 1093.6133)} km"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) / 3280.8399)} km"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) / 39370.0787)} km"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "mi":
                    if unit == "mi":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) / 1609.344)} mi"
                        break
                    elif unit == "cm":
                        result = f"{(float(valuelength) / 160934.4)} mi"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) / 16093.44)} mi"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 1609300)} mi"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) / 1.609344)} mi"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) / 1760)} mi"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) / 5280)} mi"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) / 63360)} mi"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "yd":
                    if unit == "yd":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) * 1.0936133)} yd"
                        break
                    elif unit == "cm":
                        result = f"{(float(valuelength) / 91.44)} yd"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) / 9.144)} yd"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 914.4)} yd"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) * 1093.6133)} yd"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 1760)} yd"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) / 3)} yd"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) / 36)} yd"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "ft":
                    if unit == "ft":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) * 3.2808399)} ft"
                        break
                    elif unit == "cm":
                        result = f"{(float(valuelength) / 30.48)} ft"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) / 3.048)} ft"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 304.8)} ft"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) * 3280.8399)} ft"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 5280)} ft"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) * 3)} ft"
                        break
                    elif unit == "in":
                        result = f"{(float(valuelength) / 12)} ft"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "in":
                    if unit == "in":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "m":
                        result = f"{(float(valuelength) * 39.3700787)} in"
                        break
                    elif unit == "cm":
                        result = f"{(float(valuelength) / 2.54)} in"
                        break
                    elif unit == "dm":
                        result = f"{(float(valuelength) * 3.93700787)} in"
                        break
                    elif unit == "mm":
                        result = f"{(float(valuelength) / 25.4)} in"
                        break
                    elif unit == "km":
                        result = f"{(float(valuelength) * 39370.0787)} in"
                        break
                    elif unit == "mi":
                        result = f"{(float(valuelength) * 63360)} in"
                        break
                    elif unit == "yd":
                        result = f"{(float(valuelength) * 36)} in"
                        break
                    elif unit == "ft":
                        result = f"{(float(valuelength) * 12)} in"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                elif finalunit == "index" or unit == "Index":
                    print("""
                    millimeter = mm
                    centimeter = cm
                    decimeter = dm
                    meter = m
                    kilometer = km

                    inch = in
                    foot = ft
                    yard = yd
                    mile = mi
                    """)
            except:
                print("Please enter a valid number and unit.\n")
    elif selection == 1:
            while True:
                try:
                    finalunit = input("What unit do you want to convert to? E.g. m^2 for square meters. Enter index for an overview of the supported units.\n")
                    if finalunit == "mm^2":
                        if unit == "mm^2":
                            print("Thats the same unit. Please select a different one.\n")
                            continue
                        elif unit == "cm^2":
                            result = f"{(float(valuelength) *100)} mm^2"
                            break
                        elif unit == "dm^2":
                            result = f"{(float(valuelength) *10000)} mm^2"
                            break
                        elif unit == "m^2":
                            result = f"{(float(valuelength) *1000000)} mm^2"
                            break
                        elif unit == "a":
                            result = f"{(float(valuelength) * 100000000)} mm^2"
                            break
                        elif unit == "ha":
                            result = f"{(float(valuelength) *10000000000)} mm^2"
                            break
                        elif unit == "km^2":
                            result = f"{(float(valuelength) *1000000000000)} mm^2"
                            break
                        else:
                            print("Select a valid unit.\n")
                            continue
                    if finalunit == "cm^2":
                        if unit == "cm^2":
                            print("Thats the same unit. Please select a different one.\n")
                            continue
                        elif unit == "mm^2":
                            result = f"{(float(valuelength) / 100)} cm^2"
                            break
                        elif unit == "dm^2":
                            result = f"{(float(valuelength) *100)} cm^2"
                            break
                        elif unit == "m^2":
                            result = f"{(float(valuelength) *10000)} cm^2"
                            break
                        elif unit == "a":
                            result = f"{(float(valuelength) * 1000000)} cm^2"
                            break
                        elif unit == "ha":
                            result = f"{(float(valuelength) *100000000)} cm^2"
                            break
                        elif unit == "km^2":
                            result = f"{(float(valuelength) *10000000000)} cm^2"
                            break
                        else:
                            print("Select a valid unit.\n")
                            continue
                    if finalunit == "dm^2":
                        if unit == "dm^2":
                            print("Thats the same unit. Please select a different one.\n")
                            continue
                        elif unit == "mm^2":
                            result = f"{(float(valuelength) / 10000)} dm^2"
                            break
                        elif unit == "cm^2":
                            result = f"{(float(valuelength) / 100)} dm^2"
                            break
                        elif unit == "m^2":
                            result = f"{(float(valuelength) *100)} dm^2"
                            break
                        elif unit == "a":
                            result = f"{(float(valuelength) * 10000)} dm^2"
                            break
                        elif unit == "ha":
                            result = f"{(float(valuelength) *1000000)} dm^2"
                            break
                        elif unit == "km^2":
                            result = f"{(float(valuelength) *100000000)} dm^2"
                            break
                        else:
                            print("Select a valid unit.\n")
                            continue
                    if finalunit == "m^2":
                        if unit == "m^2":
                            print("Thats the same unit. Please select a different one.\n")
                            continue
                        elif unit == "mm^2":
                            result = f"{(float(valuelength) / 1000000)} m^2"
                            break
                        elif unit == "cm^2":
                            result = f"{(float(valuelength) / 10000)} m^2"
                            break
                        elif unit == "dm^2":
                            result = f"{(float(valuelength) / 100)} m^2"
                            break
                        elif unit == "a":
                            result = f"{(float(valuelength) * 100)} m^2"
                            break
                        elif unit == "ha":
                            result = f"{(float(valuelength) *10000)} m^2"
                            break
                        elif unit == "km^2":
                            result = f"{(float(valuelength) *1000000)} m^2"
                            break
                        else:
                            print("Select a valid unit.\n")
                            continue
                    if finalunit == "a":
                        if unit == "a":
                            print("Thats the same unit. Please select a different one.\n")
                            continue
                        elif unit == "mm^2":
                            result = f"{(float(valuelength) / 100000000)} a"
                            break
                        elif unit == "cm^2":
                            result = f"{(float(valuelength) / 1000000)} a"
                            break
                        elif unit == "dm^2":
                            result = f"{(float(valuelength) / 10000)} a"
                            break
                        elif unit == "m^2":
                            result = f"{(float(valuelength) / 100)} a"
                            break
                        elif unit == "ha":
                            result = f"{(float(valuelength) * 100)} a"
                            break
                        elif unit == "km^2":
                            result = f"{(float(valuelength) * 10000)} a"
                            break
                        else:
                            print("Select a valid unit.\n")
                            continue
                    if finalunit == "ha":
                        if unit == "ha":
                            print("Thats the same unit. Please select a different one.\n")
                            continue
                        elif unit == "mm^2":
                            result = f"{(float(valuelength) / 10000000000)} ha"
                            break
                        elif unit == "cm^2":
                            result = f"{(float(valuelength) / 100000000)} ha"
                            break
                        elif unit == "dm^2":
                            result = f"{(float(valuelength) / 1000000)} ha"
                            break
                        elif unit == "m^2":
                            result = f"{(float(valuelength) / 10000)} ha"
                            break
                        elif unit == "a":
                            result = f"{(float(valuelength) / 100)} ha"
                            break
                        elif unit == "km^2":
                            result = f"{(float(valuelength) * 100)} ha"
                            break
                        else:
                            print("Select a valid unit.\n")
                            continue
                    if finalunit == "km^2":
                        if unit == "km^2":
                            print("Thats the same unit. Please select a different one.\n")
                            continue
                        elif unit == "mm^2":
                            result = f"{(float(valuelength) / 1000000000000)} km^2"
                            break
                        elif unit == "cm^2":
                            result = f"{(float(valuelength) / 10000000000)} km^2"
                            break
                        elif unit == "dm^2":
                            result = f"{(float(valuelength) / 100000000)} km^2"
                            break
                        elif unit == "m^2":
                            result = f"{(float(valuelength) / 1000000)} km^2"
                            break
                        elif unit == "a":
                            result = f"{(float(valuelength) / 10000)} km^2"
                            break
                        elif unit == "ha":
                            result = f"{(float(valuelength) / 100)} km^2"
                            break
                        else:
                            print("Select a valid unit.\n")
                            continue
                    elif finalunit == "index" or unit == "Index":
                        print("""
                        square millimeters = mm^2
                        square centimeters = cm^2
                        square decimeters = dm^2
                        square meters = m^2
                        acres = a
                        hectates = ha
                        square kilometers = km^2
                        """)
                except:
                    print("Please enter a valid number and unit.\n")
    elif selection == 2:
        while True:
            try:
                finalunit = input("What unit do you want to convert to? E.g. min for minutes. Enter index for an overview of the supported units.\n")
                if finalunit == "s":
                    if unit == "s":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "min":
                        result = f"{(float(valuelength) * 60)} s"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) *3600)} s"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) * 86400)} s"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) * 604800)} s"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) * 2592000)} s"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) * 31536000)} s"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) *10*31536000)} s"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 100 * 31536000)} s"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "min":
                    if unit == "min":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 60)} min"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) * 60)} min"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) * 1440)} min"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) * 10080)} min"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) * 43800)} min"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) * 525600)} min"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) * 5256000)} min"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 52596000)} min"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "h":
                    if unit == "h":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 3600)} h"
                        break
                    elif unit == "min":
                        result = f"{(float(valuelength) / 60)} h"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) * 24)} h"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) * 168)} h"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) * 730)} h"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) * 8760)} h"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) * 87600)} h"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 876000)} h"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "d":
                    if unit == "d":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 86400)} d"
                        break
                    elif unit == "min":
                        result = f"{(float(valuelength) / 1440)} d"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) / 24)} d"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) * 7)} d"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) * 30)} d"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) * 365)} d"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) * 3650)} d"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 36500)} d"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "w":
                    if unit == "w":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 604800)} w"
                        break
                    elif unit == "min":
                        result = f"{(float(valuelength) / 10080)} w"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) / 168)} w"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) / 7)} w"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) * 4.345)} w"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) * 52.143)} w"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) * 521)} w"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 5214)} w"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "m":
                    if unit == "m":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 2592000)} m"
                        break
                    elif unit == "min":
                        result = f"{(float(valuelength) / 43800)} m"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) / 730)} m"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) / 30.417)} m"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) / 4.345)} m"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) * 12)} m"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) * 120)} m"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 1200)} m"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "y":
                    if unit == "y":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 31556952)} y"
                        break
                    elif unit == "min":
                        result = f"{(float(valuelength) / 525600)} y"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) / 8760)} y"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) / 365)} y"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) / 52.143)} y"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) / 12)} y"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) * 10)} y"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 100)} y"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "dec":
                    if unit == "dec":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 315360000)} dec"
                        break
                    elif unit == "min":
                        result = f"{(float(valuelength) / 5256000)} dec"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) / 87600)} dec"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) / 3650)} dec"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) / 521)} dec"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) / 120)} dec"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) / 10)} dec"
                        break
                    elif unit == "c":
                        result = f"{(float(valuelength) * 10)} dec"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                if finalunit == "c":
                    if unit == "c":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "s":
                        result = f"{(float(valuelength) / 3155673600)} c"
                        break
                    elif unit == "min":
                        result = f"{(float(valuelength) / 52596000)} c"
                        break
                    elif unit == "h":
                        result = f"{(float(valuelength) / 876000)} c"
                        break
                    elif unit == "d":
                        result = f"{(float(valuelength) / 36500)} c"
                        break
                    elif unit == "w":
                        result = f"{(float(valuelength) / 5214)} c"
                        break
                    elif unit == "m":
                        result = f"{(float(valuelength) / 1200)} c"
                        break
                    elif unit == "y":
                        result = f"{(float(valuelength) / 100)} c"
                        break
                    elif unit == "dec":
                        result = f"{(float(valuelength) / 10)} c"
                        break
                    else:
                        print("Select a valid unit.\n")
                        continue
                elif finalunit == "index" or unit == "Index":
                    print("""
                    seconds = s
                    minutes = min
                    hours = h
                    days = d
                    weeks = w
                    months = m
                    years = y
                    decade = dec
                    centuries = c
                    """)
            except:
                print("Please enter a valid number and unit.\n")
    elif selection == 3:
        while True:
            try:
                finalunit = input("What unit do you want to convert to? E.g. kg for kilograms. Enter index for an overview of the supported units.\n")
                if finalunit == "mg":
                    if unit == "mg":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "g":
                        result = f"{(float(valuelength) * 1000)} mg"
                        break
                    elif unit == "kg":
                        result = f"{(float(valuelength) * 1000000)} mg"
                        break
                    elif unit == "t":
                        result = f"{(float(valuelength) * 1000000000)} mg"
                        break
                    elif unit == "lb":
                        result = f"{(float(valuelength) * 453592)} mg"
                        break
                    elif unit == "oz":
                        result = f"{(float(valuelength) * 28350)} mg"
                        break
                    else:
                        print("Select a valid unit. \n")
                        continue
                if finalunit == "g":
                    if unit == "g":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "mg":
                        result = f"{(float(valuelength) / 1000)} g"
                        break
                    elif unit == "kg":
                        result = f"{(float(valuelength) * 1000)} g"
                        break
                    elif unit == "t":
                        result = f"{(float(valuelength) * 1000000)} g"
                        break
                    elif unit == "lb":
                        result = f"{(float(valuelength) * 453.592)} g"
                        break
                    elif unit == "oz":
                        result = f"{(float(valuelength) * 28.3495)} g"
                        break
                    else:
                        print("Select a valid unit. \n")
                        continue
                if finalunit == "kg":
                    if unit == "kg":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "mg":
                        result = f"{(float(valuelength) / 1000000)} kg"
                        break
                    elif unit == "g":
                        result = f"{(float(valuelength) / 1000)} kg"
                        break
                    elif unit == "t":
                        result = f"{(float(valuelength) * 1000)} kg"
                        break
                    elif unit == "lb":
                        result = f"{(float(valuelength) / 2.205)} kg"
                        break
                    elif unit == "oz":
                        result = f"{(float(valuelength) / 35.274)} kg"
                        break
                    else:
                        print("Select a valid unit. \n")
                        continue
                if finalunit == "t":
                    if unit == "t":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "mg":
                        result = f"{(float(valuelength) / 1000000000)} t"
                        break
                    elif unit == "g":
                        result = f"{(float(valuelength) / 1000000)} t"
                        break
                    elif unit == "kg":
                        result = f"{(float(valuelength) / 1000)} t"
                        break
                    elif unit == "lb":
                        result = f"{(float(valuelength) / 2205)} t"
                        break
                    elif unit == "oz":
                        result = f"{(float(valuelength) / 35274)} t"
                        break
                    else:
                        print("Select a valid unit. \n")
                        continue
                if finalunit == "lb":
                    if unit == "lb":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "mg":
                        result = f"{(float(valuelength) / 453592)} lb"
                        break
                    elif unit == "g":
                        result = f"{(float(valuelength) / 454)} lb"
                        break
                    elif unit == "kg":
                        result = f"{(float(valuelength) * 2.205)} lb"
                        break
                    elif unit == "t":
                        result = f"{(float(valuelength) * 2205)} lb"
                        break
                    elif unit == "oz":
                        result = f"{(float(valuelength) / 16)} lb"
                        break
                    else:
                        print("Select a valid unit. \n")
                        continue
                if finalunit == "oz":
                    if unit == "oz":
                        print("Thats the same unit. Please select a different one.\n")
                        continue
                    elif unit == "mg":
                        result = f"{(float(valuelength) / 28350)} oz"
                        break
                    elif unit == "g":
                        result = f"{(float(valuelength) / 28.35)} oz"
                        break
                    elif unit == "kg":
                        result = f"{(float(valuelength) * 35.274)} oz"
                        break
                    elif unit == "t":
                        result = f"{(float(valuelength) * 35274)} oz"
                        break
                    elif unit == "lb":
                        result = f"{(float(valuelength) * 16)} oz"
                        break
                    else:
                        print("Select a valid unit. \n")
                        continue
                elif finalunit == "index" or unit == "Index":
                    print("""
                    milligrams = mg
                    grams = g
                    kilograms = kg
                    tonnes = t
                    pounds = lb
                    ounces = oz
                    """)
            except:
                print("Please enter a valid number and unit.\n")

def convertlength():
    global valuelength
    global unit
    while True:
        try:
            unit = input("What unit are you currently using? E.g. m for meters. Enter index for an overview of the supported units.\n")
            if unit == "m":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 m\n"))
                return valuelength
            elif unit == "cm":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 cm\n"))
                return valuelength
            elif unit == "dm":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 dm\n"))
                return valuelength
            elif unit == "mm":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 mm\n"))
                return valuelength
            elif unit == "km":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 km\n"))
                return valuelength
            elif unit == "mi":
                valuelength= float(input("Enter the value. E.g. 16 if you want to convert 16 mi\n"))
                return valuelength
            elif unit == "yd":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 yd\n"))
                return valuelength
            elif unit == "ft":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 ft\n"))
                return valuelength
            elif unit == "in":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 in\n"))
                return valuelength
            elif unit == "index" or unit == "Index":
                print("""
                millimeter = mm
                centimeter = cm
                decimeter = dm
                meter = m
                kilometer = km

                inch = in
                foot = ft
                yard = yd
                mile = mi
                """)
            else:
                print("Please enter a valid unit")
                continue
        except:
            print("Enter a valid number.")
            continue

def convertsurface():
    global valuelength
    global unit
    while True:
        try:
            unit = input("What unit are you currently using? E.g. m^2 for square meters. Enter index for an overview of the supported units.\n")
            if unit == "mm^2":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 mm^2\n"))
                return valuelength
            elif unit == "cm^2":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 cm^2\n"))
                return valuelength
            elif unit == "dm^2":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 dm^2\n"))
                return valuelength
            elif unit == "m^2":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 m^2\n"))
                return valuelength
            elif unit == "a":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 a\n"))
                return valuelength
            elif unit == "ha":
                valuelength= float(input("Enter the value. E.g. 16 if you want to convert 16 ha\n"))
                return valuelength
            elif unit == "km^2":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 km^2\n"))
                return valuelength
            elif unit == "index" or unit == "Index":
                print("""
                square millimeters = mm^2
                square centimeters = cm^2
                square decimeters = dm^2
                square meters = m^2
                acres = a
                hectates = ha
                square kilometers = km^2
                """)
            else:
                print("Please enter a valid unit")
                continue
        except:
            print("Enter a valid number.")
            continue

def converttime():
    global valuelength
    global unit
    while True:
        try:
            unit = input("What unit are you currently using? E.g. min for minutes. Enter index for an overview of the supported units.\n")
            if unit == "s":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 seconds\n"))
                return valuelength
            elif unit == "min":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 minutes\n"))
                return valuelength
            elif unit == "h":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 hours\n"))
                return valuelength
            elif unit == "d":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 days\n"))
                return valuelength
            elif unit == "w":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 weeks\n"))
                return valuelength
            elif unit == "m":
                valuelength= float(input("Enter the value. E.g. 16 if you want to convert 16 months\n"))
                return valuelength
            elif unit == "y":
                valuelength= float(input("Enter the value. E.g. 16 if you want to convert 16 years\n"))
                return valuelength
            elif unit == "dec":
                valuelength= float(input("Enter the value. E.g. 16 if you want to convert 16 decades\n"))
                return valuelength
            elif unit == "c":
                valuelength= float(input("Enter the value. E.g. 16 if you want to convert 16 centuries\n"))
                return valuelength
            elif unit == "index" or unit == "Index":
                print("""
                seconds = s
                minutes = min
                hours = h
                days = d
                weeks = w
                months = m
                years = y
                decade = dec
                centuries = c
                """)
            else:
                print("Please enter a valid unit")
                continue
        except:
            print("Enter a valid number.")
            continue

def convertweight():
    global valuelength
    global unit
    while True:
        try:
            unit = input("What unit are you currently using? E.g. kg for kilograms. Enter index for an overview of the supported units.\n")
            if unit == "mg":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 milligrams\n"))
                return valuelength
            elif unit == "g":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 grams\n"))
                return valuelength
            elif unit == "kg":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 kilograms\n"))
                return valuelength
            elif unit == "t":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 tonnes\n"))
                return valuelength
            elif unit == "lb":
                valuelength = float(input("Enter the value. E.g. 16 if you want to convert 16 pounds\n"))
                return valuelength
            elif unit == "oz":
                valuelength= float(input("Enter the value. E.g. 16 if you want to convert 16 ounces\n"))
                return valuelength
            elif unit == "index" or unit == "Index":
                print("""
                milligrams = mg
                grams = g
                kilograms = kg
                tonnes = t
                pounds = lb
                ounces = oz
                """)
            else:
                print("Please enter a valid unit")
                continue
        except:
            print("Enter a valid number.")
            continue

leave = False
def leave():
    if selection == 4:
        return True

def welcome():
    print("""Welcome to kellekerell's conversion tool\n

                          ____        ____     _
  _________  ____ _   ___/_/ /_____  / / /__  | |
 / ___/ __ \/ __ \ | / / // //_/ _ \/ / / _ \ / /
/ /__/ /_/ / / / / |/ / // ,< /  __/ / /  __// /
\___/\____/_/ /_/|___/ //_/|_|\___/_/_/\___//_/
                     |_|                  /_/    Version 1.0\n
By ᴋᴇʟʟᴇᴋᴇʀᴇʟʟ & toblohrone 2020
    """)

def mainselection():
    """
    Lets the user select the unit he wants to convert.
    0 = length
    1 = surface
    2 = time
    """
    global selection
    while True:
        try:
            request = input("What do you want to convert? Length, Surface, Time or Weight?\n")
            if request == "l" or request == "L" or request == "length" or request == "Length":
                selection = 0
            elif request == "s" or request == "S" or request == "surface" or request == "Surface":
                selection = 1
            elif request == "t" or request == "T" or request == "time" or request == "Time":
                selection = 2
            elif request == "w" or request == "W" or request == "weight" or request == "Weight":
                selection = 3
            elif request == "quit" or request == "Quit" or request == "exit" or request == "Exit":
                selection = 4
            else:
                print("Please enter a valid unit to convert.\n")
                continue
            break
        except:
            print("Please enter a valid unit to convert.\n")
            continue

while True:
    welcome()
    mainselection()
    if selection == 0:
        convertlength()
        calculate(valuelength,unit)
    if selection == 1:
        convertsurface()
        calculate(valuelength,unit)
    if selection == 2:
        converttime()
        calculate(valuelength,unit)
    if selection == 3:
        convertweight()
        calculate(valuelength, unit)
    if selection == 4:
        leave()
    if leave() == True:
        quit()
    print(f"Result: >> {result}\n\nPress Enter to continue")
    input()
