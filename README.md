# Robot Framework with Sauce Bindings - Example

# Background

Hello. If you're reading this, you are interested in using Robot Framework with Sauce Labs! In particular, you're interested in using the [Sauce Bindings](https://saucebindings.github.io/) with Robot.

Here I have a simplistic proof-of-concept of how this might work.

*Idea*: Write keyword libraries in pure Python for Robot using the Python Sauce Bindings.

There are two files to look at: `SauceLabs.py` and `open_page.robot`. The first is a rough Python-based Robot library that makes use of the Sauce Bindings to perform simple actions. The second is a Robot test case using the keywords defined in `SauceLabs.py`.

There are currently other files for trying to construct page objects and write Robot test cases with them. These are current a Work-in-Process.

# Installation

To install, simply use

```python
pip install -r requirements.txt
```

# Run The Test(s)!

This is what we're all here to see. To run the tests, use

```python
robot open_page.robot
```

or

```python
robot login_tests.robot
```

or even

```python
robot *.robot
```
