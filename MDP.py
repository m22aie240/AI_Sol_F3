def expected_cost(p1, p2):
    # Costs of actions
    c_a = 10
    c_b = 15
    c_d = 8

    # Probabilities for action a
    q1 = 1 - p1

    # Probabilities for action b
    q2 = 1 - p2

    # Calculate expected cost for taking action a at state P
    expected_cost_a = c_a + (p1 * c_d) + (q1 * c_d)

    # Calculate expected cost for taking action b at state P
    expected_cost_b = c_b + (p2 * c_d) + (q2 * c_d)

    return expected_cost_a, expected_cost_b


def main():
    # Get the values of p1 and p2 from the user
    p1 = float(input("Enter the value of p1: "))
    p2 = float(input("Enter the value of p2: "))

    # Calculate the expected costs of actions a and b
    cost_a, cost_b = expected_cost(p1, p2)

    # Determine the best action based on the costs
    if cost_a < cost_b:
        best_action = "a"
        justification = f"Expected cost of action a: {cost_a}, Expected cost of action b: {cost_b}"
    else:
        best_action = "b"
        justification = f"Expected cost of action a: {cost_a}, Expected cost of action b: {cost_b}"

    print(f"The best action to take at state P is action {best_action}.")
    print(f"Reason: {justification}")


if __name__ == "__main__":
    main()
