import setuptools

__version__ = '0.1.1.1'

REPO_NAME = "brain_tumor_detection"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "tumorDetection"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"

setuptools.setup(
      name="tumorDetection",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End CNN Transfer Learning implementation for Brain Tumor Detection",
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
      },
      package_dir={"": "src"},
      packages=setuptools.find_packages(where='src')
)