import tools.macos as macos # import(using) macos support
import tools.toolkit as toolkit

brew_package = [  # Package install
    "git",
    "wget",
    "curl",
    "ranger",
    "pip",
    "pip3"
]
cask_install = [  # Cask package install
    "google-chrome"
]

# Run config variable
@toolkit.setup
def setup():
	macos.brew_install(brew_package)
	macos.brew_cask_install(cask_install)