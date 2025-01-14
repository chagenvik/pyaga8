# pyaga8
Python package for calculating gas properties using the AGA8 equations GERG-2008 and DETAIL, utilizing the Rust port of NIST's AGA8 code (https://crates.io/crates/aga8).

## Description

`pyaga8` is a Python package that provides bindings for the AGA8 algorithm (GERG-2008 and DETAIL equations). The core functionality is implemented in Rust for performance, and it is exposed to Python using the `pyo3` library.

## Installation

You can install the package using `pip`:

```sh
pip install pyaga8
