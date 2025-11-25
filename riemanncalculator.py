import math

a = input("Function: ")

def operation(c):

    val = a.split('!')[1].split('!')[0]
    val = eval(val)
    # --- Number-theoretic and representation functions ---
    if "ceil" in c:
        return math.ceil(val)
    if "floor" in c:
        return math.floor(val)
    if "fabs" in c:
        return math.fabs(val)
    if "factorial" in c:
        # Note: val must be a non-negative integer
        return math.factorial(val)
    if "trunc" in c:
        return math.trunc(val)
    if "isqrt" in c:
        return math.isqrt(val)
    if "frexp" in c:
        # Returns a tuple (mantissa, exponent)
        return math.frexp(val)
    if "modf" in c:
        # Returns a tuple (fractional part, integer part)
        return math.modf(val)
    if "ulp" in c:
        return math.ulp(val)

    # --- Power and logarithmic functions ---
    if "exp" in c:
        return math.exp(val)
    if "expm1" in c:
        return math.expm1(val)
    if "log1p" in c:
        return math.log1p(val)
    if "log2" in c:
        return math.log2(val)
    if "log10" in c:
        return math.log10(val)
    if "sqrt" in c:
        return math.sqrt(val)
    if "cbrt" in c:
        # Added in Python 3.11
        try:
            return math.cbrt(val)
        except AttributeError:
            return "math.cbrt not available in this Python version"

    # 'log' is tricky because "log10" contains "log".
    # We check specific logs first, then generic log (natural log) last.
    # Checks for specific logs are above.
    if "log" in c and "log1" not in c and "log2" not in c:
        return math.log(val)

    # --- Trigonometric functions ---
    if "sin" in c and "asin" not in c and "sinh" not in c:
        return math.sin(val)
    if "cos" in c and "acos" not in c and "cosh" not in c:
        return math.cos(val)
    if "tan" in c and "atan" not in c and "tanh" not in c:
        return math.tan(val)

    if "arcsin" in c or "asin" in c and "asinh" not in c:
        return math.asin(val)
    if "arccos" in c or "acos" in c and "acosh" not in c:
        return math.acos(val)
    if "arctan" in c or "atan" in c and "atanh" not in c:
        return math.atan(val)

    # --- Angular conversion ---
    if "degrees" in c:
        return math.degrees(val)
    if "radians" in c:
        return math.radians(val)

    # --- Hyperbolic functions ---
    if "sinh" in c and "asinh" not in c:
        return math.sinh(val)
    if "cosh" in c and "acosh" not in c:
        return math.cosh(val)
    if "tanh" in c and "atanh" not in c:
        return math.tanh(val)

    if "asinh" in c:
        return math.asinh(val)
    if "acosh" in c:
        return math.acosh(val)
    if "atanh" in c:
        return math.atanh(val)

    # --- Special functions ---
    if "erfc" in c:
        return math.erfc(val)
    if "erf" in c:
        return math.erf(val)
    if "lgamma" in c:
        return math.lgamma(val)
    if "gamma" in c:
        return math.gamma(val)

    # --- Classification checks (return Booleans) ---
    if "isfinite" in c:
        return math.isfinite(val)
    if "isinf" in c:
        return math.isinf(val)
    if "isnan" in c:
        return math.isnan(val)

    else:
        return val


xi = eval(input("Lower bound: "))
xf = eval(input("Upper bound: "))
dx = eval(input("Distance: "))

listx = []
functions = []
areas = []

while xi<=xf:
    listx.append(xi)
    xi = xi + dx


for x in listx:
    functions.append(operation(a))

for y in functions:
    areas.append(y*dx)

ureas = [str(x) for x in areas]
ureas.pop()
ureas = [eval(x) for x in ureas]

print(f"Overestimate: {sum(areas)}"))
print(f"Underestimate: {sum(ureas}"))
print(f"Average: {sum((areas+ureas))/2}")
