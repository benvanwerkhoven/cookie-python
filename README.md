# Netherlands eScience Center Python Template

Spend less time setting up and configuring your new Python packages and comply with the
[Netherlands eScience Center Software Development Guide](https://guide.esciencecenter.nl/)
from the start.

## Badges

| fair-software.nl recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/nlesc/python-template) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/nlesc/python-template)](https://github.com/nlesc/python-template) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-python--template-00a3e3.svg)](https://research-software.nl/software/nlesc-python-template) |
| (4/5) citation                     | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1310751.svg)](https://doi.org/10.5281/zenodo.1310751) |
| (5/5) checklist                    | &nbsp; |
| overall                            | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| Appveyor                           | [![Appveyor Build Status](https://ci.appveyor.com/api/projects/status/a99ph5fv1carejrr/branch/main?svg=true)](https://ci.appveyor.com/project/jvdzwaan/python-template/branch/main)
| **GitHub Actions**                 | &nbsp; |
| MarkDown link checker              | [![workflow mlc badge](https://github.com/nlesc/python-template/workflows/markdown-link-checker/badge.svg)](https://github.com/nlesc/python-template/actions?query=workflow%3A%22markdown-link-checker%22) |
| Citation metadata consistency      | [![workflow cffconvert badge](https://github.com/nlesc/python-template/workflows/cffconvert/badge.svg)](https://github.com/nlesc/python-template/actions?query=workflow%3A%22cffconvert%22) |
| Unit tests                         | [![workflow tests badge](https://github.com/nlesc/python-template/workflows/tests/badge.svg)](https://github.com/nlesc/python-template/actions?query=workflow%3Atests) |

Use this [Cookiecutter](https://cookiecutter.readthedocs.io) template to generate
an empty Python package. Features include:

- Boilerplate tests and documentation,
- [Python setup configuration]({{cookiecutter.project_slug}}/setup.py),
- Open source software license,
- [Default Github actions]({{cookiecutter.project_slug}}/.github/workflows) for building, testing and deployment
- Code style checking,
- [Editorconfig]({{cookiecutter.project_slug}}/.editorconfig),
- Miscellaneous files, such as [Change log]({{cookiecutter.project_slug}}/CHANGELOG.rst), [Code of Conduct]({{cookiecutter.project_slug}}/CODE_OF_CONDUCT.rst), and [Contributing guidelines]({{cookiecutter.project_slug}}/CONTRIBUTING.rst),
- A [README]({{cookiecutter.project_slug}}/README.rst) and [a separate document]({{cookiecutter.project_slug}}/project_setup.rst) with extensive documentation about project setup.

The file structure of the generated package looks like:

```bash
path/to/package/
├── .editorconfig
└── .github/
    └── workflows
        ├── build.yml
        └── pypi_deploy.yml
├── .gitignore
├── .prospector.yml
├── CHANGELOG.rst
├── CODE_OF_CONDUCT.rst
├── CONTRIBUTING.rst
├── docs
│   ├── conf.py
│   ├── index.rst
│   └── ...
├── LICENSE
├── MANIFEST.in
├── NOTICE
├── package
│   ├── __init__.py
│   ├── __version__.py
│   └── package.py
├── README.rst
├── project_setup.rst
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    ├── test_lint.py
    └── test_package.py
```

* Code (existing or new) should be placed in `path/to/package/package/` (please choose a better name for your software!).
* Add documentation by editing `path/to/package/docs/index.rst`
* Tests go in the `path/to/package/tests/` directory
* The generated [project setup document]({{cookiecutter.project_slug}}/project_setup.rst) contains extensive documentation about the project setup and provides further instructions on what to do.

## How to use

We recommend developing your software in an isolated Python environment and
assume you are familiar with either **virtualenv + pip3** or **conda** (check the
[guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=dependencies-and-package-management)
if you are not).

### Step 1: Install `cookiecutter`

We recommend installing cookiecutter outside the virtual environment you will
be using for developing your software. This way, you don't have to install
cookiecutter for every new project.

* If you are using **virtualenv + pip3**:
	```bash
	pip3 install --user cookiecutter
	```


* If you are using **conda**:
	```bash
	conda install -c conda-forge cookiecutter
	```

### Step 2: Generate the files and directory structure

To create a new package, type:
```bash
cookiecutter https://github.com/nlesc/python-template.git
```

You will be asked to supply the following information:

| Name                      | Default value | Explanation |
| ------------------------- | ------------- | ----------- |
| project_name              | My Python Project  | Full project/package name.  |
| project_slug              | my_python_project  | This will be the name of the directory to be created and the git repository. It is safest not to use dashes (-) or spaces in this name. |
| project_short_description |   | The information that you enter here will end up in the README, documentation, license, and setup.py, so it may be a good idea to prepare something in advance. |
| version                   | 0.1.0  |   |
| github_organization       |   | GitHub organization that will contain this project's repository. This can also be your github user name. |
| open_source_license       | Apache 2.0 (1)  | The software license under which the code is made available.  |
| apidoc                    | no (1)  | Add support for automatically generating a module index from the `docstrings` in your Python package (look at the [scriptcwl package](http://scriptcwl.readthedocs.io/en/latest/apidocs/scriptcwl.html) for an example).
| full_name                 | John Smith  | Your full name, e.g. _John Smith_.   |
| email                     | yourname@esciencecenter.nl | Your (work) email address  |
| tweet_releases            | no (1) | Enable GitHub Action to tweet new releases of your package. |
| copyright_holder          |   | Name(s) of the organization(s) or person(s) who hold the copyright of the software (e.g., Netherlands eScience Center).  |
| code_of_conduct_email     | yourname@esciencecenter.nl | Email address of the person who should be contacted in case of violations of the Code of Conduct.  |

### Step 3: Create and activate a Python environment

* If you are using **virtualenv + pip3**, do:
	 ```bash
	 $ virtualenv -p python3 env
	 $ . env/bin/activate
	 ```
* If you are using **conda**, type:
	```bash
	$ conda create -n env python=3
	$ source activate env
	```
	(On windows use `activate env` to activate the conda environment.)

## Continuous integration with Github Actions

The template has two Ci workflows. They can be found in **.github/workflows** folder.

1. **build.yml**

This workflow install the dependencies, builds the package and runs tests.

2. **pypi.yml**

This workflow pushes the package to [PYPI](https://pypi.org/). This action will require PYPI token to be stored as [Github secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets). The workflow uses secret with a name of `PYPI_TOKEN`.

You can learn more about Python packaging at [this link](https://packaging.python.org/tutorials/packaging-projects/).


## How to contribute

Suggestions/improvements/edits are most welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before creating an issue or a pull request.
