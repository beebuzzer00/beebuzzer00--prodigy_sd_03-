scales = {
    "C": {"name": "Celsius", "formula": lambda t: (t - 273.15) * 9/5 + 32},
    "F": {"name": "Fahrenheit", "formula": lambda t: (t - 32) * 5/9 + 273.15},
    "K": {"name": "Kelvin", "formula": lambda t: t},
    "Ra": {"name": "Rankine", "formula": lambda t: t * 9/5},
    "Re": {"name": "Réaumur", "formula": lambda t: (t - 32) * 4/9},
}

# Main loop
while True:
    # Input temperature and scales
    temp = float(input("Enter temperature: "))
    in_scale = input("Input scale (C/F/K/Ra/Re): ").upper()
    out_scale = input("Output scale (C/F/K/Ra/Re): ").upper()

    # Validate input
    if in_scale not in scales or out_scale not in scales:
        print("Invalid scale identifier. Please try again.")
        continue

    # Perform conversion
    converted_temp = scales[out_scale]["formula"](scales[in_scale]["formula"](temp))

    # Output result
    print(f"{temp:.2f}{scales[in_scale]['name']} is equal to {converted_temp:.2f}{scales[out_scale]['name']}")

    # Continue or exit
    choice = input("Continue (y/n)? ").lower()
    if choice not in ("y", "yes"):
        break

print("Exiting...")