def determine_insurance_plan():
    print("Welcome to the Insurance Plan Selector!")
    
    # Get user inputs
    age = int(input("Enter your age: "))
    income = float(input("Enter your annual income: "))
    marital_status = input("Are you single or married? (Enter 'single' or 'married'): ").lower()
    has_children = input("Do you have children? (yes/no): ").lower()
    health_level = input("Do you visit the doctor a lot or have any chronic illness? (yes/no): ").lower()

    # Plan details
    plans = {
        "High-Deductible A": {"deductible": "3500/person, 7500/family", "coverage": "80% after deductible", "cost": "1100/month individual, 2300/month family"},
        "High-Deductible B": {"deductible": "4500/person, 9500/family", "coverage": "80% after deductible", "cost": "800/month individual, 1800/month family"},
        "Regular Plan A": {"deductible": "1500/person, 3500/family", "coverage": "80% after deductible", "cost": "2800/month individual, 3800/month family"},
        "Regular Plan B": {"deductible": "1500/person, 3500/family", "coverage": "90% after deductible", "cost": "3500/month individual, 4800/month family"},
        "Low Income Plan": {"deductible": "No deductible", "coverage": "90% coverage", "cost": "1000/month individual, 2000/month family"}
    }

    # Determine plan using badly nested if statements
    if age <= 18:
        print("Sorry, you do not qualify for any plans.")
        return 
    if(marital_status == "single" and income < 35000):
        if health_level == "no":
            print("\nRecommended Plan: Low Income Plan (Individual)")
            print_plan_details("Low Income Plan", plans)
            print("\nAlternate Plan: High-Deductible B (Individual)")
            print_plan_details("High-Deductible B", plans)
        else:
            print("\nRecommended Plan: Low Income Plan (Individual)")
            print_plan_details("Low Income Plan", plans)
            print("\nAlternate Plan: Regular Plan A (Individual)")
            print_plan_details("Regular Plan A", plans)
    elif(marital_status == "single" and income > 50000):
        if health_level == "no":
            print("\nRecommended Plan: High-Deductible B (Individual)")
            print_plan_details("High-Deductible B", plans)
            print("\nAlternate Plan: High-Deductible A (Individual)")
            print_plan_details("High-Deductible A", plans)
        else:
            print("\nRecommended Plan: Regular Plan B (Individual)")
            print_plan_details("Regular Plan B", plans)
            print("\nAlternate Plan: High-Deductible A (Individual)")
            print_plan_details("High-Deductible A", plans)
    elif(marital_status == "single"):#other incomes
        if health_level == "no":
            print("\nRecommended Plan: High-Deductible A (Individual)")
            print_plan_details("High-Deductible A", plans)
            print("\nAlternate Plan: Regular Plan A (Individual)")
            print_plan_details("Regular Plan A", plans)
        else:
            print("\nRecommended Plan: Regular Plan B (Individual)")
            print_plan_details("Regular Plan B", plans)
            print("\nAlternate Plan: High-Deductible A (Individual)")
            print_plan_details("High-Deductible A", plans)
    if(has_children == "yes" and health_level == "no"):
        if income < 65000:
            if income > 50000:
                print("\nRecommended Plan: High-Deductible A (Family)")
                print_plan_details("High-Deductible A", plans)
                print("\nAlternate Plan: High-Deductible B (Family)")
                print_plan_details("High-Deductible B", plans)
            else:
                print("\nRecommended Plan: Low Income Plan (Family)")
                print_plan_details("Low Income Plan", plans)
                print("\nAlternate Plan: High-Deductible A (Family)")
                print_plan_details("High-Deductible A", plans)
    elif(has_children == "yes"):
        if income < 65000:
            if income > 50000:
                print("\nRecommended Plan: High-Deductible B (Family)")
                print_plan_details("High-Deductible B", plans)
                print("\nAlternate Plan: Regular Plan A (Family)")
                print_plan_details("Regular Plan A", plans)
            else:
                print("\nRecommended Plan: Low Income Plan (Family)")
                print_plan_details("Low Income Plan", plans)
                print("\nAlternate Plan: Regular Plan A (Family)")
                print_plan_details("Regular Plan A", plans)
    else:
        if income > 50000:
            if health_level == "no":
                print("\nRecommended Plan: High-Deductible A (Individual)")
                print_plan_details("High-Deductible A", plans)
                print("\nAlternate Plan: High-Deductible B (Individual)")
                print_plan_details("High-Deductible B", plans)
            else:
                print("\nRecommended Plan: Regular Plan B (Individual)")
                print_plan_details("Regular Plan B", plans)
                print("\nAlternate Plan: Regular Plan A (Individual)")
                print_plan_details("Regular Plan A", plans)
        else:
            if health_level == "no":
                print("\nRecommended Plan: High-Deductible B (Individual)")
                print_plan_details("High-Deductible B", plans)
                print("\nAlternate Plan: High-Deductible A (Individual)")
                print_plan_details("High-Deductible A", plans)
            else:
                print("\nRecommended Plan: Regular Plan A (Individual)")
                print_plan_details("Regular Plan A", plans)
                print("\nAlternate Plan: Regular Plan B (Individual)")
                print_plan_details("Regular Plan B", plans)
                


def print_plan_details(plan_name, plans):
    """Print details of a given insurance plan."""
    print(f"\nPlan: {plan_name}")
    print(f"  Deductible: {plans[plan_name]['deductible']}")
    print(f"  Coverage: {plans[plan_name]['coverage']}")
    print(f"  Cost: {plans[plan_name]['cost']}")

# Run the program
determine_insurance_plan()
