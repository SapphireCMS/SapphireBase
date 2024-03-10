import config
from sapphirecms import html
import glob, importlib.util, pathlib
import config, importlib

class Theme:
    name = "Theme"
    description = "This is the base theme. Inherit from this class to create your own theme."
    keywords = "theme"
    logo = "https://via.placeholder.com/256"
    favicon = "https://via.placeholder.com/32"
    author = "Author"
    author_email = "author@provider.xyz"
    author_website = "https://www.author.xyz"
    author_website_name = "Author Site"
    license = "MIT"
    license_url = "https://opensource.org/licenses/MIT"
    version = "0.0.0"
    config = config.active
    
def get_active_theme():
    return importlib.import_module(config.active.theme)
    
def get_themes(context):
    themes = []
    for file in glob.glob(f"{context}/*/__init__.py"):
        if open(file).read().startswith("# Type: Theme"):
            module_path = '.'.join(pathlib.Path(pathlib.Path(file).parent.name).parts)
            if module_path != "themes.theme":
                spec = importlib.util.spec_from_file_location(module_path, file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                themes.append(module.THEME)
            else:
                themes.append(importlib.import_module(module_path).Theme)
    return themes