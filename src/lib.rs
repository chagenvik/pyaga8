use aga8::*;
use pyo3::prelude::*;

#[pyclass]
struct Gerg2008 {
    inner: gerg2008::Gerg2008,
}

#[pymethods]
impl Gerg2008 {
    #[new]
    fn new() -> Self {
        Gerg2008 {
            inner: gerg2008::Gerg2008::new(),
        }
    }

    #[setter]
    fn set_pressure(&mut self, pressure: f64) -> PyResult<()> {
        println!("{}", pressure);
        self.inner.p = pressure;
        Ok(())
    }

    #[getter]
    fn get_pressure(&self) -> PyResult<f64> {
        Ok(self.inner.p)
    }

    #[setter]
    fn set_temperature(&mut self, tempreature: f64) -> PyResult<()> {
        println!("{}", tempreature);
        self.inner.t = tempreature;
        Ok(())
    }

    #[getter]
    fn get_tempreature(&self) -> PyResult<f64> {
        Ok(self.inner.t)
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn aga8eos(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Gerg2008>()?;
    Ok(())
}