from setuptools import setup


def version() -> str:
    with open('./stable_whisper/_version.py') as f:
        return f.read().split('=')[-1].strip().strip('"').strip("'")


def read_me() -> str:
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name="stable-ts-con",
    version=version(),
    description="Timestamps and confidence score for words of OpenAI's Whisper outputs down to word-level.",
    long_description=read_me(),
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
    author="Vit",
    url="https://github.com/Anoncheg1/stable-ts-con",
    license="MIT",
    packages=['stable_whisper'],
    install_requires=[
      "whisper @ git+https://github.com/openai/whisper.git"
    ],
    include_package_data=False
)
