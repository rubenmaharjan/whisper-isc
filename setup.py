from setuptools import setup


def version() -> str:
    with open('./isc_whisper/_version.py') as f:
        return f.read().split('=')[-1].strip().strip('"').strip("'")


def read_me() -> str:
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name="whisper-isc",
    version=version(),
    description="Timestamps and confidence score for words of OpenAI's Whisper outputs down to word-level.",
    long_description=read_me(),
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
    author="ruben",
    url="https://github.com/rubenmaharjan/whisper-isc",
    license="MIT",
    packages=['isc_whisper'],
    install_requires=[
        "openai-whisper @ git+https://github.com/openai/whisper.git"
    ],
    entry_points={
        'console_scripts': [
            'whisper-isc = isc_whisper.evaluate:cli'
        ]
    },
    include_package_data=False
)
