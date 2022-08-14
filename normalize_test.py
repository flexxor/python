input = 20

def normalize(value_to_normalize, max_value = 40, min_value = 0, target_max = 255, target_min = 0):
    value_to_normalize = min(value_to_normalize, max_value)
    value_to_normalize = max(value_to_normalize, min_value)

    quotient = value_to_normalize / max_value

    target_value = (int) (target_max * quotient)
    target_value = max(target_value, target_min)
    print(f"Result: {target_value}")

normalize(20)