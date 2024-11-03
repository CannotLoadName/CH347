from setuptools import setup
setup(
    name="CH347",
    version="1.0.2",
    author="Enbuging",
    author_email="electricfan@yeah.net",
    license="MIT",
    description="A wrapper for CH347DLL.DLL, which can be used to access SPI, JTAG, I2C, UARTs and GPIOs on CH347.",
    keywords=["hardware","interface","CH347","CH347DLL.DLL","CH347DLLA64.DLL"],
    platforms=["Windows"],
    package_data={
        "ch347":["config.json"]
    },
    packages=["ch347"]
)