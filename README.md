<h1>Gendiff</h1>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/garryfisher/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/garryfisher/python-project-50/actions)
[![Lint status](https://github.com/garryfisher/python-project-50/workflows/make-lint/badge.svg)](https://github.com/garryfisher/python-project-50/actions)

### Codeclimate 
<a href="https://codeclimate.com/github/garryfisher/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/df0c9295986e60cf71d0/maintainability" /></a>
<a href="https://codeclimate.com/github/garryfisher/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/df0c9295986e60cf71d0/test_coverage" /></a>


### Description
This is a learning project from the Python developer track, Hexlet Online School (https://ru.hexlet.io/programs/python).

The program compares two file formats: json, yaml, yml including those with nested structure and outputs the difference.

### Installation
  1. Clone repository : `git clone https://github.com/garryfisher/python-project-50.git`
  2. Go to the python-project-50 directory: `cd python-project-50`
  3. Poetry is needed to build the package: `make build`
  4. To install the package run the `make package-install` command.

### Run
To find the difference between the two files, use the command `gendiff file1 file2`<br>
To get output in formats: <b>stylish</b>, <b>plain</b>, <b>json</b>, specify the format with the <b>-f</b> switch:<br>
`gendiff -f [format] file1 file2`<br>
Если необходима помощь- использейте команду `gendiff -h`

### Demonstration

*Comparison of the two JSON files*
<a href="https://asciinema.org/a/ADM8hqMJkrRP0mfBwIE7xY8bQ" target="_blank"><img src="https://asciinema.org/a/ADM8hqMJkrRP0mfBwIE7xY8bQ.svg" /></a>

*Comparison of the two YAML files*
<a href="https://asciinema.org/a/eLWsw6q7EbAEpqgrNq40OOotc" target="_blank"><img src="https://asciinema.org/a/eLWsw6q7EbAEpqgrNq40OOotc.svg" /></a>

*Comparison of the two JSON files with nested structures*
<a href="https://asciinema.org/a/c5J6eKjTDy9GE7XG82OxqbwI9" target="_blank"><img src="https://asciinema.org/a/c5J6eKjTDy9GE7XG82OxqbwI9.svg" /></a>

*Comparison of the two YAML files with nested structures*
<a href="https://asciinema.org/a/26gy0uxp2vOF9IhTTGIXwjiCr" target="_blank"><img src="https://asciinema.org/a/26gy0uxp2vOF9IhTTGIXwjiCr.svg" /></a>

*Comparison of the two JSON files and output the result in plain format*
<a href="https://asciinema.org/a/JSFe4zihBXmVnZW9U6laaxr6B" target="_blank"><img src="https://asciinema.org/a/JSFe4zihBXmVnZW9U6laaxr6B.svg" /></a>

*Comparison of the two YAML files with nested structure and the result in plain format.</h3>
<a href="https://asciinema.org/a/q93Iz1nDLEhzN7ENfOjgr1zC9" target="_blank"><img src="https://asciinema.org/a/q93Iz1nDLEhzN7ENfOjgr1zC9.svg" /></a>

*Comparison of the two JSON files and output the result in JSON format*
<a href="https://asciinema.org/a/SZYwAolpDYpXwKAU4EiQ3i0qW" target="_blank"><img src="https://asciinema.org/a/SZYwAolpDYpXwKAU4EiQ3i0qW.svg" /></a>

*Comparison of the two YAML files with nested structure and the result JSON format*
<a href="https://asciinema.org/a/68nEJKCvAUXLNlDMO9gfdhanJ" target="_blank"><img src="https://asciinema.org/a/68nEJKCvAUXLNlDMO9gfdhanJ.svg" /></a>
