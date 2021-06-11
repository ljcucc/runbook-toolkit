def brew_install(package_list):
	print(f"brew: installing {', '.join(list(package_list))}")

def brew_cask_install(package_list):
	print(f"brew cask: installing {', '.join(list(package_list))}")