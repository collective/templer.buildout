from templer.core.base import BaseTemplate

class BasicBuildout(BaseTemplate):
    _template_dir = 'templates/basic_buildout'
    summary = "A basic buildout skeleton"
    ndots = 1
    help = """
This creates a Python project without any Zope or Plone features.
"""
    category = "Buildout"
    required_templates = []
    required_structures = ['bootstrap',]
    use_cheetah = True
    
    
    