
def TestAlpha(Alpha, x = 2, y = 3, z = 4):
    x = Alpha(x)
    y = Alpha(y)
    z = Alpha(z)

    print("--- Base Elements ---")
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")

    print("\n--- Arithmetic Operations ---")
    # Addition: coordinate(x + y) = coordinate(x) + coordinate(y)
    add_xy = x + y
    print(f"x + y = {add_xy}  (Expected coordinate: {x[:]:.4f} + {y[:]:.4f} = {x[:] + y[:]:.4f})")

    # Subtraction: coordinate(x - y) = coordinate(x) - coordinate(y)
    sub_xy = x - y
    print(f"x - y = {sub_xy}  (Expected coordinate: {x[:]:.4f} - {y[:]:.4f} = {x[:] - y[:]:.4f})")

    # Multiplication: coordinate(x * y) = coordinate(x) * coordinate(y)
    mul_xy = x * y
    print(f"x * y = {mul_xy}  (Expected coordinate: {x[:]:.4f} * {y[:]:.4f} = {x[:] * y[:]:.4f})")

    # Division: coordinate(x / y) = coordinate(x) / coordinate(y)
    div_xy = x / y
    print(f"x / y = {div_xy}  (Expected coordinate: {x[:]:.4f} / {y[:]:.4f} = {x[:] / y[:]:.4f})")

    print("\n--- Absolute Value Operation ---")
    # Absolute coordinate check on a negative-coordinate element (e.g., x - y)
    neg_elem = x[0] - y
    abs_elem = abs(neg_elem)
    print(f"neg_elem: {neg_elem}")
    print(f"abs(neg_elem): {abs_elem}  (Expected coordinate: {abs(neg_elem[:]):.4f})")

    print("\n--- Triple Associativity & Distributivity Checks ---")
    # Associativity of Addition
    assoc_add_left = (x + y) + z
    assoc_add_right = x + (y + z)
    print(f"(x + y) + z: {assoc_add_left}")
    print(f"x + (y + z): {assoc_add_right}")
    print(f"Addition Associative Match? {abs(assoc_add_left[:] - assoc_add_right[:]) < 1e-9}")

    # Associativity of Multiplication
    assoc_mul_left = (x * y) * z
    assoc_mul_right = x * (y * z)
    print(f"(x * y) * z: {assoc_mul_left}")
    print(f"x * (y * z): {assoc_mul_right}")
    print(f"Multiplication Associative Match? {abs(assoc_mul_left[:] - assoc_mul_right[:]) < 1e-9}")
