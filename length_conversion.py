#(Everything to Meters First)
#ye aik dic hai jo hr value ka meter 
length_to_meters = {
    "Yoctometers (ym)": 1e-24, "Zeptometers (zm)": 1e-21, "Attometers (am)": 1e-18,
    "Femtometers (fm)": 1e-15, "Picometers (pm)": 1e-12, "Nanometers (nm)": 1e-9,
    "Micrometers (µm)": 1e-6, "Millimeters (mm)": 1e-3, "Centimeters (cm)": 1e-2,
    "Decimeters (dm)": 1e-1, "Meters (m)": 1, "Decameters (dam)": 10, "Hectometers (hm)": 100,
    "Kilometers (km)": 1000, "Megameters (Mm)": 1e6, "Gigameters (Gm)": 1e9,
    "Inches (in)": 0.0254, "Feet (ft)": 0.3048, "Yards (yd)": 0.9144,
    "Miles (mi)": 1609.344, "Nautical Miles (nmi)": 1852, "Astronomical Units (AU)": 149597870700,
    "Light Years (ly)": 9.461e15, "Parsecs (pc)": 3.086e16
}

# ✅ Convert Function
def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value, "No conversion needed"
    
    # Step 1: Convert from given unit to meters
    value_in_meters = value * length_to_meters[from_unit]
    
    # Step 2: Convert from meters to target unit
    converted_value = value_in_meters / length_to_meters[to_unit]
    
    # Step 3: Formula explanation
    formula = f"({value} × {length_to_meters[from_unit]}) ÷ {length_to_meters[to_unit]}"
    
    return converted_value, formula
