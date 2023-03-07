from django.test import TestCase
from .models import WelcomeText

class welcomeTests(TestCase):
    def RefferenceIsIncorrect(self):
        def itExists():
            if(WelcomeText.welcome_text):
                return True
        self.assertIs(itExists(),False)
