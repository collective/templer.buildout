from templer.core.base import BaseTemplate

class BasicBuildout(BaseTemplate):
    _template_dir = 'templates/basic_buildout'
    summary = "A basic buildout skeleton"
    help = """
This creates a basic skeleton for a buildout.
"""
    category = "Buildout"
    required_templates = []
    required_structures = ['bootstrap',]
    use_cheetah = True

    