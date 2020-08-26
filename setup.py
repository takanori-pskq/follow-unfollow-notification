import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="follow-unfollow-notification",
    version="1.0.0",
    author="Takanori H.",
    author_email="takanori17h@gmail.com",
    description="A script for listing users who followed and unfollowed the account",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takanori-pskq/follow-unfollow-notification",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "fun_initialize=follow_unfollow_notification.follow_unfollow_notification:fun_initialize",
            "fun_notify=follow_unfollow_notification.follow_unfollow_notification:fun_notify",
        ]
    },
    python_requires=">=3.6.0",
)
