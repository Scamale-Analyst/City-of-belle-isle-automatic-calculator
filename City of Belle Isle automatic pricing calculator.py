#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
DOCSTRING
City of Belle Isle automatic pricing calculator.py

----------------------------------------------------------------------------------------------------------------
(THIS IS NOT A REAL DOCSTRING SINCE IT WOULD REVEAL SENSITIVE INFORMATION ABOUT THE COMPANY)
----------------------------------------------------------------------------------------------------------------

This Python script calculates the pricing for construction permits based on specific criteria and regulations. It takes into account various factors such as project size, location, and permit type to determine the total cost of obtaining a construction permit.

Usage:
1. Ensure you have the necessary input data available.
2. Import this script into your project.
3. function with the required parameters to get the permit pricing.

Functions:
- calculate_permit_price(project_size: int, location: str, permit_type: str) -> float:
  Calculates the total cost of a construction permit based on the provided parameters.

Parameters:
- project_size (int): The size or scope of the construction project.
- location (str): The location where the construction project will take place.
- permit_type (str): The type of permit required for the construction project.

Returns:
- float: The total cost of the construction permit.

Note:
- Make sure to consult local regulations and pricing structures to ensure accurate results.
- This script serves as a general tool and may need customization based on specific local requirements.

Example:
```python
permit_cost = calculate_permit_price(project_size=10000, location="CityA", permit_type="Building")
print(f"The construction permit cost is: ${permit_cost}")"""


from msvcrt import getch   # for Windows
from os import system

def set_console_size(width, height):
    system(f"mode con: cols={width} lines={height}")
    
def get_key():
    return getch().decode('utf-8')

def calculator():
    
    set_console_size(120, 40)  # Adjust width and height as needed

    while True:
        try:
            print("""
            City of Belle Isle automatic pricing calculator.""")
            print("""
            Please only type the code of the permit type you want to price.""")
            print("""
                R = New Roof
                RE = Re-Roof
                B = Building
                M = Mechanical
                E = Electrical
                PV = Photo Voltaic
                BD = Boat Dock
                P = Plumbing
                RP = Re-pipe
                WH = Water Heater
                WD = Window-Door
                GD = Garage Door
                G = Gas
                PO = Pool
                PE = Pool Electrical
                PP = Pool Plumbing
                D = Demo
                PA = Paver
                S = Seawall
                LV = Low Voltage
                TU = Tug
                TP = T-Pole
                ES = Early Start
                FD = Foundation
                CB = Commercial Building
                CR = Commercial New Roof
                CRE = Commercial Re-Roof
                """ )

            permit_codes = {
                'R': 'New Roof',
                'RE': 'Re-Roof',
                'B': 'Building',
                'M': 'Mechanical',
                'E': 'Electrical',
                'BD': 'Boat Dock',
                'P': 'Plumbing',
                'RP': 'Re-pipe',
                'WH': 'Water Heater',
                'WD': 'Window Door',
                'PV': 'Photo Voltaic',
                'G': 'Gas',
                'PO': 'Pool',
                'PE': 'Pool Electrical',
                'PP': 'Pool Plumbing',
                'D': 'Demo',
                'PA': 'Paver',
                'S': 'Seawall',
                'LV': 'Low Voltage',
                'ES': 'Early Start',
                'TU': 'Tug',
                'TP': 'T-Pole',
                'FD': 'Foundation',
                'CB': 'Commercial Building',
                'CR': 'Commercial New Roof',
                'CRE': 'Commercial Re-Roof',
                'GD': 'Garage Door'
            }
            while True:
                permit_code = input('What type of permit is this?: ').upper()
                if permit_code in permit_codes:
                    permit_type = permit_codes[permit_code]
                    print(f'The type of permit selected is: {permit_type}')
                    break
                else:
                    print(f'{permit_code} Is not a valid permit code, please try again:')

            while True:
                if permit_code == 'M':
                    try:
                        tons = float(input("How many tons in total does the system use?: "))
                        break  # Exit the loop if a valid numeric value is entered
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                elif permit_code == 'P':
                    try:
                        fixture = float(input("How many fixtures does this permit contain?: "))
                        break  # Exit the loop if a valid numeric value is entered
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                elif permit_code == 'RP':
                    try:
                        bath = float(input("How many bathrooms does this property have?: "))
                        break  # Exit the loop if a valid numeric value is entered
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                elif permit_code == 'WH':
                    print("The permit fee is: 50.00")
                    print("The review fee is: 25.00")
                    print("The 1% fee is: 2.00")
                    print("The 1.5% fee is: 2.00")
                    print("The total price is: 79.00")
                    break #Exit the loop when is water heater

                elif permit_code == 'PE':
                    print("The permit fee is: 65.00")
                    print("The review fee is: 32.50")
                    print("The 1% fee is: 2.00")
                    print("The 1.5% fee is: 2.00")
                    print("The total price is: 101.50")
                    break #Exit the loop when is pool electrical

                elif permit_code == 'PP':
                    print("The permit fee is: 70.00")
                    print("The review fee is: 35.00")
                    print("The 1% fee is: 2.00")
                    print("The 1.5% fee is: 2.00")
                    print("The total price is: 109.00")
                    break #Exit the loop when is pool plumbing

                elif permit_code == 'TU':
                    print("The permit fee is: 120.00")
                    print("The review fee is: 60.00")
                    print("The 1% fee is: 2.00")
                    print("The 1.5% fee is: 2.70")
                    print("The total price is: 184.70")
                    break #Exit the loop when is TUG

                elif permit_code == 'ES':
                    print("The permit fee is: 125.00")
                    print("The 1% fee is: 2.00")
                    print("The 1.5% fee is: 2.00")
                    print("The total price is: 129.00")
                    break #Exit the loop when is Early Start

                elif permit_code == 'TP':
                    print("The permit fee is: 50.00")
                    print("The review fee is: 25.00")
                    print("The 1% fee is: 2.00")
                    print("The 1.5% fee is: 2.00")
                    print("The total price is: 79.00")
                    break #Exit the loop when is T-Pole

                else:
                    try:
                        valuation = float(input("How much is the job valuation?: "))
                        print("Job valuation:", valuation)
                        break  # Exit the loop if a valid numeric value is entered
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")




            #                                             CODE FOR NEW ROOF

            if permit_code == 'R':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                            CODE FOR RE ROOF

            elif permit_code == 'RE':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                percent_1 = pfee * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = pfee * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + percent_1 + percent_15,2)
                print("The permit fee is:", pfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                           CODE FOR BUILDING

            elif permit_code == 'B':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                zoning = float(input("How much is the zoning fee? If the permit does not require it please input 0: "))
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + zoning + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The zoning fee is:", zoning)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                          CODE FOR MECHANICAL

            elif permit_code == 'M':
                pfee = round((tons * 7) + 50, 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                        CODE FOR ELECTRICAL

            elif permit_code == 'E':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 12
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                           CODE FOR PHOTO VOLTAIC

            elif permit_code == 'PV':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 6
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                         CODE FOR BOAT DOCK

            elif permit_code == 'BD':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                zoning = 175.00
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + zoning + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The zoning fee is:", zoning)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                    CODE FOR PLUMBING

            elif permit_code == 'P':
                pfee = round((fixture * 7) + 50, 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                     CODE FOR RE-PIPE

            elif permit_code == 'RP':
                pfee = round(bath * 50, 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                           CODE FOR WINDOW-DOOR
            elif permit_code == 'WD':
                def calculate_charge(valuation):
                    base_charge = 30
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                                CODE FOR GAS

            elif permit_code == 'G':
                def calculate_charge(valuation):
                    base_charge = 75
                    additional_charge_rate = 10
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                               CODE FOR POOL

            elif permit_code == 'PO':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                zoning = 175.00
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + zoning + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The zoning fee is:", zoning)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                                 CODE FOR DEMOLITION

            elif permit_code == 'D':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                zoning = 50.00
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + zoning + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The zoning fee is:", zoning)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                           CODE FOR PAVERS

            elif permit_code == 'PA':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                zoning = 50.00
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + zoning + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The zoning fee is:", zoning)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                                CODE FOR SEAWALL

            elif permit_code == 'S':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                            CODE FOR LOW VOLTAGE

            elif permit_code == 'LV':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 6
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                         CODE FOR FOUNDATION

            elif permit_code == 'FD':
                def calculate_charge(valuation):
                    base_charge = 50
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                              CODE FOR COMMERICAL BUILDING

            elif permit_code == 'CB':
                def calculate_charge(valuation):
                    base_charge = 100
                    additional_charge_rate = 6
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                zoning = float(input("How much is the zoning fee? If the permit does not require it please input 0: "))
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + zoning + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The zoning fee is:", zoning)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                             CODE FOR COMMERCIAL NEW ROOF

            if permit_code == 'CR':
                def calculate_charge(valuation):
                    base_charge = 100
                    additional_charge_rate = 6
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                           CODE FOR COMMERCIAL RE-ROOF

            elif permit_code == 'CRE':
                def calculate_charge(valuation):
                    base_charge = 100
                    additional_charge_rate = 6
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                percent_1 = pfee * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = pfee * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + percent_1 + percent_15,2)
                print("The permit fee is:", pfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)

            #                                              CODE FOR GARAGE DOOR

            if permit_code == 'GD':
                def calculate_charge(valuation):
                    base_charge = 100
                    additional_charge_rate = 5
                    threshold = 1000

                    if valuation <= threshold:
                        return base_charge
                    else:
                        additional_amount = valuation - threshold
                        additional_charge = ((additional_amount - 1) // threshold + 1) * additional_charge_rate
                        return base_charge + additional_charge
                pfee = round(calculate_charge(valuation), 2)
                rfee = round(pfee / 2, 2)
                bfee = round(pfee + rfee,2)
                percent_1 = (pfee + rfee) * 0.01
                if percent_1 < 1.99:
                    percent_1 = 2.00
                else: 
                    percent_1 = round(percent_1, 2)
                percent_15 = (pfee + rfee) * 0.015
                if percent_15 < 1.99:
                    percent_15 = 2.00
                else:
                    percent_15 = round(percent_15, 2)
                total_charge = round(pfee + rfee + percent_1 + percent_15, 2)
                print("The permit fee is:", pfee)
                print("The review fee is:", rfee)
                print("The price before fees is:", bfee)
                print("The 1% fee is:", percent_1)
                print("The 1.5% fee is:", percent_15)
                print("The total price is:", total_charge)
            print("----------------------------------------------------------------------")
            print("If you want to reset the program to price a different permit please PRESS R")
            print("If you want to close the program please PRESS ESC")
            key = get_key()
            if key.upper() == 'R':
                continue
            elif key == '\x1b':  # ASCII code for Esc
                break
            else:
                pass  # Do nothing for other keys
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
if __name__ == "__main__":
    calculator()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




