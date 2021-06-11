import tools.macos as macos # import(using) macos support

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
macos.brew_install(brew_package)
macos.brew_cask_install(cask_install)