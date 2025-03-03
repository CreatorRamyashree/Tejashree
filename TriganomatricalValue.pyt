import math

def calculate_trig_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)
    return sine_value, cosine_value, tangent_value

angle = float(input("Enter the angle in degrees: "))
sin_val, cos_val, tan_val = calculate_trig_values(angle)

print(f"sin({angle}) = {sin_val}")
print(f"cos({angle}) = {cos_val}")
print(f"tan({angle}) = {tan_val}")
