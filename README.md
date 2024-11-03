# WORDS TO NUMBER CONVERTER

This package allows you to convert sentences containing numbers written in words in multiple languages (French, English, Spanish) into numeric values (integers or floats).

## Supported Languages

- **English**
- **French**
- **Spanish**

Feel free to contribute and add more languages.

## Installation

To use this package, make sure you have Python installed on your machine. No external dependencies are required for this package.

## Usage

The main function of this package is `convert(sentence, decimal_part=False)`.

### Arguments

- **sentence** (str): A string containing numbers written in words.
- **decimal_part** (bool): Optional. Allows a recursive call of the function for the decimal part; do not change this value.

### Return

- Returns an integer or a float corresponding to the provided phrase.

## Examples

```python
>>> convert("one")
1
>>> convert("ten thousand two hundred forty-seven")
10247
>>> convert("four point five")
4.5
```

## Notes

- The function supports numbers in words up to several billion and handles decimal values with words like "point", "virgule", or "punto" depending on the language.
- Make sure the provided string is well-formed to avoid conversion errors.

## Authors

This package was developed by Benjamin Bonneton. For any questions or contributions, feel free to reach out!

## License

This project is licensed under the GPLv3 License. See the LICENSE file for more details.
