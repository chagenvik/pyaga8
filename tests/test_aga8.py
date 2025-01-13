import pyaga8
from pytest import approx, raises


gerg = pyaga8.Gerg2008()

FULL_COMPOSITION = pyaga8.Composition()
FULL_COMPOSITION.methane = 0.778_24
FULL_COMPOSITION.nitrogen = 0.02
FULL_COMPOSITION.carbon_dioxide = 0.06
FULL_COMPOSITION.ethane = 0.08
FULL_COMPOSITION.propane = 0.03
FULL_COMPOSITION.isobutane = 0.001_5
FULL_COMPOSITION.n_butane = 0.003
FULL_COMPOSITION.isopentane = 0.000_5
FULL_COMPOSITION.n_pentane = 0.001_65
FULL_COMPOSITION.hexane = 0.002_15
FULL_COMPOSITION.heptane = 0.000_88
FULL_COMPOSITION.octane = 0.000_24
FULL_COMPOSITION.nonane = 0.000_15
FULL_COMPOSITION.decane = 0.000_09
FULL_COMPOSITION.hydrogen = 0.004
FULL_COMPOSITION.oxygen = 0.005
FULL_COMPOSITION.carbon_monoxide = 0.002
FULL_COMPOSITION.water = 0.000_1
FULL_COMPOSITION.hydrogen_sulfide = 0.002_5
FULL_COMPOSITION.helium = 0.007
FULL_COMPOSITION.argon = 0.001

def test_gerg2008_set_composition():
    gerg.set_composition(FULL_COMPOSITION)

    # TODO: Map Rust Errors Empty and BadSum to python Exceptions
    invalid = pyaga8.Composition()
    with raises(BaseException):
        gerg.set_composition(invalid)

    invalid.ethane = 0.3
    with raises(BaseException):
        gerg.set_composition(invalid)

def test_gerg2008_calc_density():
    gerg.set_composition(FULL_COMPOSITION)
    gerg.temperature = 400.0
    gerg.pressure = 50_000.0

    gerg.calc_density(0)
    assert gerg.d == approx(12.798_286_260_820_62)

def test_gerg2008_calc_pressure():
    gerg.set_composition(FULL_COMPOSITION)
    gerg.temperature = 18.0 + 273.15
    gerg.d = 7.558_334

    assert gerg.calc_pressure() == approx(13_050.037_472_144)

def test_gerg2008_calc_properties():
    gerg.set_composition(FULL_COMPOSITION)
    gerg.temperature = 400.0
    gerg.pressure = 50_000.0

    gerg.calc_density(0)
    gerg.calc_properties()

    assert gerg.d == approx(12.798_286_260_820_62)
    assert gerg.mm == approx(20.542_744_501_6)
    assert gerg.z == approx(1.174_690_666_383_717)
    assert gerg.dp_dd == approx(7_000.694_030_193_327)
    assert gerg.d2p_dd2 == approx(1_129.526_655_214_841)
    assert gerg.dp_dt == approx(235.983_229_259_309_6)
    assert gerg.u == approx(-2_746.492_901_212_53)
    assert gerg.h == approx(1_160.280_160_510_973)
    assert gerg.s == approx(-38.575_903_924_090_89)
    assert gerg.cv == approx(39.029_482_181_563_72)
    assert gerg.cp == approx(58.455_220_510_003_66)
    assert gerg.w == approx(714.424_884_059_602_4)
    assert gerg.g == approx(16_590.641_730_147_33)
    assert gerg.jt == approx(7.155_629_581_480_913E-5)
    assert gerg.kappa == approx(2.683_820_255_058_032)

def test_gerg2008_calc_molar_mass():
    gerg.set_composition(FULL_COMPOSITION)
    gerg.calc_molar_mass()

    assert gerg.mm == approx(20.542_744_501_6)

def test_gerg2008_set_pressure():
    gerg.pressure = 42.14
    assert gerg.pressure == approx(42.14)

    with raises(TypeError):
        gerg.pressure = 'spam'

def test_gerg2008_set_temperature():
    gerg.temperature = 42.14
    assert gerg.temperature == approx(42.14)

    with raises(TypeError):
        gerg.temperature = 'spam'

def test_gerg2008_set_d():
    gerg.d = 6.42
    assert gerg.d == approx(6.42)

    with raises(TypeError):
        gerg.d = 'spam'
