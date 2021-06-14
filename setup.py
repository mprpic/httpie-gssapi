from setuptools import setup


with open("README.rst", "r") as f:
    description = f.read()

requires = [
    "httpie>=0.9.7",
    "requests-gssapi>=1.0.0",
]

setup(
    name="httpie-gssapi",
    description="GSSAPI authentication plug-in for HTTPie",
    long_description=description,
    version="1.0.2",
    author="Martin Prpic",
    author_email="martin@nil.bz",
    license="MIT",
    url="https://github.com/mprpic/httpie-gssapi",
    download_url="https://github.com/mprpic/httpie-gssapi",
    py_modules=["httpie_gssapi"],
    zip_safe=False,
    entry_points={"httpie.plugins.auth.v1": ["httpie_gssapi = httpie_gssapi:GSSAPIAuthPlugin"]},
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
    ],
    keywords="httpie gssapi kerberos",
)
