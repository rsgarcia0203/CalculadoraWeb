from src import calculadora as c


def test_suma():
    assert c.suma(1, 2) == 3


def test_resta():
    assert c.resta(1, 2) == -1


def test_multiplicacion():
    assert c.multiplicacion(1, 2) == 2


def test_division():
    assert c.division(1, 2) == 0.5


def test_modulo():
    assert c.modulo(1, 2) == 1


def test_potencia():
    assert c.potencia(1, 2) == 1


def test_raiz():
    assert c.raiz(4) == 2


def test_raiz_de_M():
    assert c.raiz_de_M(4, 2) == 2


def test_factorial():
    assert c.factorial(4) == 24


def test_combinaciones():
    assert c.combinaciones(4, 2) == 12


def test_permutaciones():
    assert c.permutaciones(4, 2) == 24


def test_binomial():
    assert c.binomial(4, 2) == 6


def test_binomial_inverso():
    assert c.binomial_inverso(4, 2) == 6


def test_coseno():
    assert c.coseno(1) == 0.5440211678894844


def test_seno():
    assert c.seno(1) == 0.8414709848078965


def test_tangente():
    assert c.tangente(1) == 1.5574077246549023


def test_coseno_inverso():
    assert c.coseno_inverso(1) == 1.5574077246549023


def test_seno_inverso():
    assert c.seno_inverso(1) == 1.5574077246549023


def test_tangente_inverso():
    assert c.tangente_inverso(1) == 1.5574077246549023


def test_logaritmo():
    assert c.logaritmo(1) == 0.0


def test_logaritmo_base():
    assert c.logaritmo_base(1, 2) == 0.6931471805599453


def test_exponencial():
    assert c.exponencial(1) == 2.718281828459045


def test_seno_grados():
    assert c.seno_grados(1) == 0.01745240643728351


def test_coseno_grados():
    assert c.coseno_grados(1) == 0.01745240643728351


def test_tangente_grados():
    assert c.tangente_grados(1) == 0.01745240643728351


def test_seno_grados_inverso():
    assert c.seno_grados_inverso(1) == 0.01745240643728351


def test_coseno_grados_inverso():
    assert c.coseno_grados_inverso(1) == 0.01745240643728351


def test_tangente_grados_inverso():
    assert c.tangente_grados_inverso(1) == 0.01745240643728351


def test_sumatoria():
    assert c.sumatoria(1) == 1


def test_sumatoria_inverso():
    assert c.sumatoria_inverso(1) == 1

    