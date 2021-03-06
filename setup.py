import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == "__main__":
    setup(name="eht-dmc",
          version = "0.2dev",
          author = "Dom Pesce",
          author_email = "dpesce@cfa.harvard.edu",
          description = ("Python code to perform radio interferometric imaging and "+
                         "modeling within a Bayesian framework in both "+
                         "total intensity and polarization."),
          license = "GPLv3",
          keywords = "radio interferometry VLBI",
          url = "https://github.com/dpesce/DMC",
          packages = ["dmc"],
          long_description=read('README.md'),
          install_requires=["ehtim",
                            "pymc3",
                            "future",
                            "matplotlib",
                            "numpy",
                            "scipy",
                            "corner",
                            "ehtplot"]
    )
