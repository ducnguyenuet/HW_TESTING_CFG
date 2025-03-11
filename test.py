def predict(temperature: float, humidity: int) -> str:
    t = temperature
    h = humidity
    
    if t < -20.0 or t > 50.0 or h < 0 or h > 80:  # Fault 1: should be h > 100
        return "Đầu vào không hợp lệ"
    if t >= 20.0:
        return "nắng"
    if h <= 30 and t <= -10.0:
        return "tuyet"  # Fault 2: should be "tuyết"
    return "lạnh"

# Test cases for C2 coverage
test_cases = [
    (19.1, 24, "lạnh"),  
    (7.9, 13, "tuyết"),   
    (30.6, 70, "nắng"),   
    (61.5, -11, "Đầu vào không hợp lệ"),   
]

# Running test cases
for temp, hum, expected in test_cases:
    result = predict(temp, hum)
    print(f"predict({temp}, {hum}) = {result}, expected = {expected}, {'PASS' if result == expected else 'FAIL'}")
