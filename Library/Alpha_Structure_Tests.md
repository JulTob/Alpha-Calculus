```py
Exp = AlphaStructure("exp", math.exp, math.log)
TestAlpha(Exp)
```
```
--- Base Elements ---
x: exp⟨val: 2.0000, coord: 0.6931⟩
y: exp⟨val: 3.0000, coord: 1.0986⟩
z: exp⟨val: 4.0000, coord: 1.3863⟩

--- Arithmetic Operations ---
x + y = exp⟨val: 6.0000, coord: 1.7918⟩  (Expected coordinate: 0.6931 + 1.0986 = 1.7918)
x - y = exp⟨val: 0.6667, coord: -0.4055⟩  (Expected coordinate: 0.6931 - 1.0986 = -0.4055)
x * y = exp⟨val: 2.1415, coord: 0.7615⟩  (Expected coordinate: 0.6931 * 1.0986 = 0.7615)
x / y = exp⟨val: 1.8794, coord: 0.6309⟩  (Expected coordinate: 0.6931 / 1.0986 = 0.6309)

--- Absolute Value Operation ---
neg_elem: exp⟨val: 0.3333, coord: -1.0986⟩
abs(neg_elem): exp⟨val: 3.0000, coord: 1.0986⟩  (Expected coordinate: 1.0986)

--- Triple Associativity & Distributivity Checks ---
(x + y) + z: exp⟨val: 24.0000, coord: 3.1781⟩
x + (y + z): exp⟨val: 24.0000, coord: 3.1781⟩
Addition Associative Match? True
(x * y) * z: exp⟨val: 2.8739, coord: 1.0557⟩
x * (y * z): exp⟨val: 2.8739, coord: 1.0557⟩
Multiplication Associative Match? True
```
```py
# Create a new alpha structure where value = 1 / coordinate (and coordinate = 1 / value)
# Note: This represents a reciprocal mapping system.
Reciprocal = AlphaStructure("reciprocal", lambda u: 1.0 / u, lambda v: 1.0 / v)

# Run the unified test function to verify coordinate operations, abs, and associativity
TestAlpha(Reciprocal)
```
```
--- Base Elements ---
x: reciprocal⟨val: 2.0000, coord: 0.5000⟩
y: reciprocal⟨val: 3.0000, coord: 0.3333⟩
z: reciprocal⟨val: 4.0000, coord: 0.2500⟩

--- Arithmetic Operations ---
x + y = reciprocal⟨val: 1.2000, coord: 0.8333⟩  (Expected coordinate: 0.5000 + 0.3333 = 0.8333)
x - y = reciprocal⟨val: 6.0000, coord: 0.1667⟩  (Expected coordinate: 0.5000 - 0.3333 = 0.1667)
x * y = reciprocal⟨val: 6.0000, coord: 0.1667⟩  (Expected coordinate: 0.5000 * 0.3333 = 0.1667)
x / y = reciprocal⟨val: 0.6667, coord: 1.5000⟩  (Expected coordinate: 0.5000 / 0.3333 = 1.5000)

--- Absolute Value Operation ---
neg_elem: reciprocal⟨val: -3.0000, coord: -0.3333⟩
abs(neg_elem): reciprocal⟨val: 3.0000, coord: 0.3333⟩  (Expected coordinate: 0.3333)

--- Triple Associativity & Distributivity Checks ---
(x + y) + z: reciprocal⟨val: 0.9231, coord: 1.0833⟩
x + (y + z): reciprocal⟨val: 0.9231, coord: 1.0833⟩
Addition Associative Match? True
(x * y) * z: reciprocal⟨val: 24.0000, coord: 0.0417⟩
x * (y * z): reciprocal⟨val: 24.0000, coord: 0.0417⟩
Multiplication Associative Match? True
```
```py
# Create a new alpha structure where value = coordinate + 5 (and coordinate = value - 5)
Shift = AlphaStructure("shift", lambda u: u + 5.0, lambda v: v - 5.0)

# Run the unified test function to verify coordinate operations, abs, and associativity
TestAlpha(Shift)
```
```
--- Base Elements ---
x: shift⟨val: 2.0000, coord: -3.0000⟩
y: shift⟨val: 3.0000, coord: -2.0000⟩
z: shift⟨val: 4.0000, coord: -1.0000⟩

--- Arithmetic Operations ---
x + y = shift⟨val: 0.0000, coord: -5.0000⟩  (Expected coordinate: -3.0000 + -2.0000 = -5.0000)
x - y = shift⟨val: 4.0000, coord: -1.0000⟩  (Expected coordinate: -3.0000 - -2.0000 = -1.0000)
x * y = shift⟨val: 11.0000, coord: 6.0000⟩  (Expected coordinate: -3.0000 * -2.0000 = 6.0000)
x / y = shift⟨val: 6.5000, coord: 1.5000⟩  (Expected coordinate: -3.0000 / -2.0000 = 1.5000)

--- Absolute Value Operation ---
neg_elem: shift⟨val: 7.0000, coord: 2.0000⟩
abs(neg_elem): shift⟨val: 7.0000, coord: 2.0000⟩  (Expected coordinate: 2.0000)

--- Triple Associativity & Distributivity Checks ---
(x + y) + z: shift⟨val: -1.0000, coord: -6.0000⟩
x + (y + z): shift⟨val: -1.0000, coord: -6.0000⟩
Addition Associative Match? True
(x * y) * z: shift⟨val: -1.0000, coord: -6.0000⟩
x * (y * z): shift⟨val: -1.0000, coord: -6.0000⟩
Multiplication Associative Match? True
```
```py
# Create a new alpha structure where value = tanh(coordinate) and coordinate = arctanh(value)
# This is defined for values in the range (-1, 1).
Tanh = AlphaStructure("tanh", math.tanh, math.atanh)

# Run the updated TestAlpha with scaled inputs fitting the arctanh domain
TestAlpha(Tanh, x=0.2, y=0.5, z=0.8)
```
```
--- Base Elements ---
x: tanh⟨val: 0.2000, coord: 0.2027⟩
y: tanh⟨val: 0.5000, coord: 0.5493⟩
z: tanh⟨val: 0.8000, coord: 1.0986⟩

--- Arithmetic Operations ---
x + y = tanh⟨val: 0.6364, coord: 0.7520⟩  (Expected coordinate: 0.2027 + 0.5493 = 0.7520)
x - y = tanh⟨val: -0.3333, coord: -0.3466⟩  (Expected coordinate: 0.2027 - 0.5493 = -0.3466)
x * y = tanh⟨val: 0.1109, coord: 0.1114⟩  (Expected coordinate: 0.2027 * 0.5493 = 0.1114)
x / y = tanh⟨val: 0.3532, coord: 0.3691⟩  (Expected coordinate: 0.2027 / 0.5493 = 0.3691)

--- Absolute Value Operation ---
neg_elem: tanh⟨val: -0.5000, coord: -0.5493⟩
abs(neg_elem): tanh⟨val: 0.5000, coord: 0.5493⟩  (Expected coordinate: 0.5493)

--- Triple Associativity & Distributivity Checks ---
(x + y) + z: tanh⟨val: 0.9518, coord: 1.8507⟩
x + (y + z): tanh⟨val: 0.9518, coord: 1.8507⟩
Addition Associative Match? True
(x * y) * z: tanh⟨val: 0.1217, coord: 0.1223⟩
x * (y * z): tanh⟨val: 0.1217, coord: 0.1223⟩
Multiplication Associative Match? True

```
```py
# Test Tanh with values close to its domain boundaries (-1, 1)
# Using y=0.0001 instead of 0.0 to avoid ZeroDivisionError during coordinate division (x / y)
print("=== Testing Tanh near Boundary Limits ===")
TestAlpha(Tanh, x=0.0, y=-0.9999, z=0.9999)
```
```
=== Testing Tanh near Boundary Limits ===
--- Base Elements ---
x: tanh⟨val: 0.0000, coord: 0.0000⟩
y: tanh⟨val: -0.9999, coord: -4.9517⟩
z: tanh⟨val: 0.9999, coord: 4.9517⟩

--- Arithmetic Operations ---
x + y = tanh⟨val: -0.9999, coord: -4.9517⟩  (Expected coordinate: 0.0000 + -4.9517 = -4.9517)
x - y = tanh⟨val: 0.9999, coord: 4.9517⟩  (Expected coordinate: 0.0000 - -4.9517 = 4.9517)
x * y = tanh⟨val: -0.0000, coord: -0.0000⟩  (Expected coordinate: 0.0000 * -4.9517 = -0.0000)
x / y = tanh⟨val: -0.0000, coord: -0.0000⟩  (Expected coordinate: 0.0000 / -4.9517 = -0.0000)

--- Absolute Value Operation ---
neg_elem: tanh⟨val: 0.9999, coord: 4.9517⟩
abs(neg_elem): tanh⟨val: 0.9999, coord: 4.9517⟩  (Expected coordinate: 4.9517)

--- Triple Associativity & Distributivity Checks ---
(x + y) + z: tanh⟨val: 0.0000, coord: 0.0000⟩
x + (y + z): tanh⟨val: 0.0000, coord: 0.0000⟩
Addition Associative Match? True
(x * y) * z: tanh⟨val: -0.0000, coord: -0.0000⟩
x * (y * z): tanh⟨val: -0.0000, coord: -0.0000⟩
Multiplication Associative Match? True

```
```py
# Define standard logistic sigmoid function and its inverse (the logit function)
def sigmoid(u):
    return 1.0 / (1.0 + math.exp(-u))

def logit(v):
    # Defined for v in (0, 1)
    return math.log(v / (1.0 - v))

# Instantiate the Sigmoid AlphaStructure
Sigmoid = AlphaStructure("sigmoid", sigmoid, logit)

# Run the unified tests using boundary-proximate values within the (0, 1) interval
# Using y=0.5001 to avoid a coordinate value of 0.0 and prevent ZeroDivisionError on x / y
print("=== Testing Sigmoid near Boundary Limits ===")
TestAlpha(Sigmoid, x=0.5, y=0.0001, z=0.9999)
```
```
=== Testing Sigmoid near Boundary Limits ===
--- Base Elements ---
x: sigmoid⟨val: 0.5000, coord: 0.0000⟩
y: sigmoid⟨val: 0.0001, coord: -9.2102⟩
z: sigmoid⟨val: 0.9999, coord: 9.2102⟩

--- Arithmetic Operations ---
x + y = sigmoid⟨val: 0.0001, coord: -9.2102⟩  (Expected coordinate: 0.0000 + -9.2102 = -9.2102)
x - y = sigmoid⟨val: 0.9999, coord: 9.2102⟩  (Expected coordinate: 0.0000 - -9.2102 = 9.2102)
x * y = sigmoid⟨val: 0.5000, coord: -0.0000⟩  (Expected coordinate: 0.0000 * -9.2102 = -0.0000)
x / y = sigmoid⟨val: 0.5000, coord: -0.0000⟩  (Expected coordinate: 0.0000 / -9.2102 = -0.0000)

--- Absolute Value Operation ---
neg_elem: sigmoid⟨val: 0.9999, coord: 9.2102⟩
abs(neg_elem): sigmoid⟨val: 0.9999, coord: 9.2102⟩  (Expected coordinate: 9.2102)

--- Triple Associativity & Distributivity Checks ---
(x + y) + z: sigmoid⟨val: 0.5000, coord: 0.0000⟩
x + (y + z): sigmoid⟨val: 0.5000, coord: 0.0000⟩
Addition Associative Match? True
(x * y) * z: sigmoid⟨val: 0.5000, coord: -0.0000⟩
x * (y * z): sigmoid⟨val: 0.5000, coord: -0.0000⟩
Multiplication Associative Match? True
```
