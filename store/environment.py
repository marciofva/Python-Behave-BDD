from pageObjects.basePageElement import BasePageElement

def before_all(context):
  context.driver = BasePageElement().select_browser('chrome')

def after_scenario(context, args):
    context.driver.quit()