#Weight Unit
#is dic main hum saare weight ko phelai kg main convert karengai phr target value
# Convert Everything to Kilograms First
weight_to_kg = {
    "Kilograms (kg)": 1, "Grams (g)": 0.001, "Milligrams (mg)": 1e-6, "Metric Tons (t)": 1000,
    "Pounds (lb)": 0.453592, "Ounces (oz)": 0.0283495, "Stones (st)": 6.35029,
    "Tons (US)": 907.184, "Tons (UK)": 1016, "Micrograms (µg)": 1e-9, "Nanograms (ng)": 1e-12,
    "Earth Mass (M⊕)": 5.972e24, "Solar Mass (M☉)": 1.989e30
}

#Conversion Function
def convert_weight(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value, "No conversion needed"

    # Step 1: Convert to Kilograms First
    value_in_kg = value * weight_to_kg[from_unit]

    # Step 2: Convert to Target Unit
    converted_value = value_in_kg / weight_to_kg[to_unit]

    # Step 3: Formula Explanation
    formula = f"({value} × {weight_to_kg[from_unit]}) ÷ {weight_to_kg[to_unit]}"

    return converted_value, formula
