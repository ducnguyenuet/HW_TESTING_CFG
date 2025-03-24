def predict(t: float, h: int) -> str:
    if t < -20.0 or t > 50.0 or h < 0 or h > 80:  # Fault 1: should be h > 100
        return "Đầu vào không hợp lệ"
    if t >= 20.0:
        return "nắng"
    if h <= 30 and t <= -10.0:
        return "tuyet"  # Fault 2: should be "tuyết"
    return "lạnh"

# Test cases từ ảnh kèm expected output
test_cases = [
    (15.0, 20, "lạnh"),             
    (14.0, 20, "lạnh"),            
    (13.0, 20, "lạnh"),             
    (10.0, -5, "Đầu vào không hợp lệ"),  
    (30.0, 30, "nắng"),            
    (-14.0, 20, "tuyết"),         
    (15.0, 20, "lạnh"),           
    (15.0, 20, "lạnh"),            
    (10.0, -2, "Đầu vào không hợp lệ"), 
    (-14.0, 20, "tuyết"),         
]

# Thực thi test case
for temp, hum, expected in test_cases:
    result = predict(temp, hum)
    print(f"predict({temp}, {hum}) = {result}, expected = {expected}, {'PASS' if result == expected else 'FAIL'}")
