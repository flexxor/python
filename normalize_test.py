input = 20

def normalize(value_to_normalize, max_value = 40, min_value = 0, target_max = 255, target_min = 0):
    if value_to_normalize > max_value:
        value_to_normalize = max_value
    if value_to_normalize < min_value:
        value_to_normalize = 0

    quotient = value_to_normalize / max_value

    target_value = (int) (target_max * quotient)
    print(f"Result: {target_value}")


normalize(20)