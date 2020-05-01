##########################################
# Email configurations:
# First argument specifies type of email template
# Second and third arguments are presenters which fill in the template blanks
# 
# Number of arguments, 'to' field, 'subject' field, and templates can all be altered here.
#
# Also required is credentials.json and pip install the gmail api. In order to start,
# visit the following site and follow Step1 and Step2: https://developers.google.com/gmail/api/quickstart/python
# Users must have an authorized Gmail account. Add credentials.json into the folder containing this code
#
# E.g. code implementation:
# Type in console
# `python send_email.py breadth 'Morgan Oneka' 'Santhoshi Krishnan'
#########################################

from sys import argv

presenter1 = argv[2]
presenter2 = argv[3]
to = 'youremail@umich.edu'
subject = 'Lab Meeting Today at 12:30'

email_templates = {
	'depth' : 'Hi all,\n\nAs a reminder, we will have a lab meeting today at 12:30pm. Presenting today will be %s on current research in the lab\
 and %s on a Journal Club paper. Our lab meeting link is here:\n\nhttps://umich.bluejeans.com/yourlink\n\n \
Kind Regards\n' % (presenter1,presenter2),

    'breadth' : 'Hi all:\n\nAs a reminder, we will have a lab meeting today at 12:30pm. Presenting today will be %s and %s on a few journal papers.\
  Our lab meeting link is here:\n\
  https://umich.bluejeans.com/yourlink\n\n\
Kind Regards' % (presenter1, presenter2)

}