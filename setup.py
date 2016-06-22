from distutils.core import setup

files = ["*.css"]


setup(
    name="junit2html",
    version="001",
    description="Generate HTML reports from Junit results",
    author="Ian Norton",
    author_email="ian.norton@thales-esecurity.com",
    url="",
    packages=["junit2htmlreport"],
    package_data={"junit2htmlreport": files},
    scripts=["junit2html"],
    long_description="Genearate a single file HTML report from a Junit XML file"
)