def generate_simple_od_profile(part_diameter: float, length: float):
    r = part_diameter / 2.0
    return [
        (0.0, 0.0),
        (0.0, r),
        (length, r),
        (length, 0.0),
    ]
