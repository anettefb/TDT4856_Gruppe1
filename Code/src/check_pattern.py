def check_pattern(depth):
    threshold = 5
    approved = []
    for item in depth:
        if item > threshold:
            approved.append("Yes")
        else:
            approved.append("No")
    return approved
