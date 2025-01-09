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

def test_gerg2008_calc_density():
    gerg.set_composition(FULL_COMPOSITION)
    gerg.temperature = 400.0
    gerg.pressure = 50_000.0

    gerg.calc_density(0)
    assert gerg.d == approx(12.798_286_260_820_62)

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
