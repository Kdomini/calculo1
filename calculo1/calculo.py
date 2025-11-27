from sympy import (
    symbols, diff, limit, integrate, sin, cos, tan, cot, sec,
    asin, sqrt, ln, exp, Pow, oo
)

# ================================
# Funções de formatação 
# ================================
def formatar(expr):
    s = str(expr)
    s = s.replace('**', '^')
    s = s.replace('*', '·')
    s = s.replace('5·t', '5t').replace('2·t', '2t').replace('3·t', '3t')
    return s


# ================================
# Variáveis simbólicas
# ================================
t, x = symbols('t x')


# ================================
# CÁLCULO DE LIMITES
# ================================
print("\n===== CÁLCULO DE LIMITES =====\n")

limites = {
    "a) lim(t→3) (3(t-6))/(t-6)": limit((3*(t - 6))/(t - 6), t, 3),
    "b) lim(t→0) (√(t+4) − 2)/t": limit((sqrt(t+4) - 2)/t, t, 0),
    "c) lim(t→0) ln(t+1)/t": limit(ln(t+1)/t, t, 0),
    "d) lim(t→0⁻) ln(t+1)/t": limit(ln(t+1)/t, t, 0, dir='-'),
    "e) lim(x→∞) (7x³−4x²+6)/(3x³+9x−2)": limit((7*x**3 - 4*x**2 + 6)/(3*x**3 + 9*x - 2), x, oo),
    "f) lim(t→−∞) (2t²−1)/(t²+5)": limit((2*t**2 - 1)/(t**2 + 5), t, -oo),
    "g) lim(t→4) (t² + 2t)": limit(t**2 + 2*t, t, 4),
    "h) lim(t→2⁻) (t²−4)/(t−2)": limit((t**2 - 4)/(t - 2), t, 2, dir='-'),
    "i) lim(t→2⁺) (t²−4)/(t−2)": limit((t**2 - 4)/(t - 2), t, 2, dir='+'),
    "j) lim(t→∞) (5t³−1)/(2t³+t)": limit((5*t**3 - 1)/(2*t**3 + t), t, oo),
    "k) lim(t→0⁺) t·ln(t)": limit(t*ln(t), t, 0, dir='+'),
    "l) lim(t→0⁺) (1+t)^t": limit((1+t)**t, t, 0, dir='+'),
    "m) lim(t→∞) (1+1/t)^t": limit((1 + 1/t)**t, t, oo),
    "n) lim(t→0⁺) t^(−t)": limit(t**(-t), t, 0, dir='+'),
    "o) lim(t→0) (1+t)^t": limit((1+t)**t, t, 0)
}

for desc, resultado in limites.items():
    print(f"{desc} = {resultado}")


# ================================
# CÁLCULO DE DERIVADAS
# ================================
print("\n===== CÁLCULO DAS DERIVADAS =====\n")

derivadas = {
    "a) s(t) = t⁵": diff(t**5, t),
    "b) F(t) = t²(3t + 1)": diff(t**2 * (3*t + 1), t),
    "c) v(t) = (t² + 1)/(t − 1)": diff((t**2 + 1)/(t - 1), t),
    "d) y = 4^(3x²+9x)": diff(4**(3*x**2 + 9*x), x),
    "d) s(t) = e^(2t)": diff(exp(2*t), t),
    "e) y = e^(x⁷ − 3x + 8)": diff(exp(x**7 - 3*x + 8), x),
    "e) v(t) = ln(3t+2)": diff(ln(3*t + 2), t),
    "f) s(t) = cos(4t)": diff(cos(4*t), t),
    "g) s(t) = sin(5t)": diff(sin(5*t), t),
    "h) s(t) = tan(t)": diff(tan(t), t),
    "i) v(t) = cot(t)": diff(cot(t), t),
    "j) s(t) = sec(t)": diff(sec(t), t),
    "k) s(t) = arcsin(t/4)": diff(asin(t/4), t),
    "l) s(t) = √(4t²+1)": diff(sqrt(4*t**2 + 1), t),
    "m) x(t) = cos(3t²)": diff(cos(3*t**2), t),
    "n) s(t) = t·sin(t²)": diff(t*sin(t**2), t),
    "o) f(x)= x·sin(2x)·cos(3x)": diff(x*sin(2*x)*cos(3*x), x)
}

for desc, expr in derivadas.items():
    print(f"{desc} → {formatar(expr)}")


# ================================
# CÁLCULO DE INTEGRAIS
# ================================
print("\n===== CÁLCULO DAS INTEGRAIS =====\n")

integrais = {
    "a) ∫ (3t²+2t+1) dt": integrate(3*t**2 + 2*t + 1, t),
    "b) ∫ 2t/√(t²+1) dt": integrate(2*t / sqrt(t**2 + 1), t),
    "c) ∫ t·e^t dt": integrate(t*exp(t), t)
}

for desc, expr in integrais.items():
    print(f"{desc} = {formatar(expr)} + C")