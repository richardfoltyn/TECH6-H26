# Installing the Conda Python distribution

- Conda is a package and environment management system that includes both Python and
  packages for scientific computing.
- You should prefer Conda distributions (such as Anaconda or Miniforge) over a "bare minimum"
  Python installer such as the one distributed via [python.org](https://www.python.org/downloads/).
- You should prefer Conda distributions over the Python distribution shipped with
  your operating system (macOS and Linux).

## Installation

### Alternative 1: Anaconda

1. Download the installer from the [Anaconda website](https://www.anaconda.com/download/success).
    - **No registration is required**; skip it if prompted.
    - Choose the installer for your platform.
    - **macOS users**: Anaconda only supports Apple Silicon Macs. If you have an Intel-based Mac, Anaconda is no longer available; use **Alternative 2: Miniforge** instead.
      If you are unsure whether your Mac has Apple Silicon or an Intel processor, consult 
      [this guide](https://support.apple.com/guide/mac-help/get-system-information-about-your-mac-syspr35536/mac).
2. Running the installer should be straightforward, but you can consult
    [this guide](https://docs.anaconda.com/anaconda/install/) 
    if needed.

### Alternative 2: Miniforge (conda-forge)

[Miniforge](https://github.com/conda-forge/miniforge) is a lightweight Conda installer
that configures [conda-forge](https://conda-forge.org/) as its default channel. It does not
include hundreds of pre-installed packages, resulting in a much faster and smaller installation.
**Intel Mac users must use Miniforge**, as Anaconda no longer supports Intel-based Macs.

1. Download the installer for your platform from the [conda-forge download page](https://conda-forge.org/download/):
    - **Windows**: Download and run the `Miniforge3-Windows-x86_64.exe` installer.
    - **macOS**: Download the Graphical Installer (`.pkg`) matching your architecture (*Apple Silicon* / `arm64` or *Intel* / `x86_64`) and follow the installer steps.
    - **Linux**: Download the `.sh` installer script for your architecture and run `bash Miniforge3-Linux-*.sh` in the terminal.
2. Accept the default options during installation.

## Creating a Conda environment

-   The installation comes with a default environment called `base`.
-   You should create a course-specific environment
    from the environment definition file [`environment.yml`](../environment.yml).

    This has the advantage that the Python and package versions you use 
    are the same as those used by the instructor.

To create the environment, you can use *one* of the following alternatives:

1. Creating the environment using the `environment.yml` file on your computer:
    
    -   Open the Anaconda Prompt / Miniforge Prompt (Windows) or the terminal (macOS, Linux)
        and change to the folder where you cloned the course repository 
        (the one that contains `environment.yml`):

        On Windows, use something like:
        ```cmd
        cd "c:\Users\username\path\to\TECH6-H26"
        ```

        On macOS or Linux, use something like:
        ```bash
        cd "/Users/username/path/to/TECH6-H26"
        ```

    -   Run the following command:
        ```bash
        conda env create -f environment.yml
        ```

2.  Creating the environment using the `environment.yml` file from GitHub directly 
    (if you are unsure where `environment.yml` is located on your system):
    
    -   Open the Anaconda Prompt / Miniforge Prompt (Windows) or the terminal (macOS, Linux) and run the following commands:
        ```bash
        curl -O https://raw.githubusercontent.com/richardfoltyn/TECH6-H26/main/environment.yml
        conda env create -f environment.yml
        ```

If everything worked out, you should see the following message at the end of the output:
```bash
# To activate this environment, use
#
#     $ conda activate TECH6
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```