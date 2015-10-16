
import gettext
gettext.bindtextdomain('internacional', './po')
gettext.textdomain('internacional')

_ = gettext.gettext

print gettext.find('internacional')
print _('Hello World')
