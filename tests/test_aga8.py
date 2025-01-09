import pyaga8


def gerg2008_calc_density():
    composition = pyaga8.Composition()
    composition.methane = 0.778_24
    composition.nitrogen = 0.02
    composition.carbon_dioxide = 0.06
    composition.ethane = 0.08
    composition.propane = 0.03
    composition.isobutane = 0.001_5
    composition.n_butane = 0.003
    composition.isopentane = 0.000_5
    composition.n_pentane = 0.001_65
    composition.hexane = 0.002_15
    composition.heptane = 0.000_88
    composition.octane = 0.000_24
    composition.nonane = 0.000_15
    composition.decane = 0.000_09
    composition.hydrogen = 0.004
    composition.oxygen = 0.005
    composition.carbon_monoxide = 0.002
    composition.water = 0.000_1
    composition.hydrogen_sulfide = 0.002_5
    composition.helium = 0.007
    composition.argon = 0.001

    gerg = pyaga8.Gerg2008()
    gerg.set_composition(composition)
    gerg.temperature = 400.0
    gerg.pressure = 50_000.0

    gerg.calc_density(0)
    assert abs(gerg.d - 12.798_286_260_820_62) < 1.0e-10
