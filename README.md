# LDAP-auth

This will need work, as anon access ot LDAP is now restricted, should be a good base if you are solving for this problem tho 

Python Module that checks a given user/pass against Rackspace's LDAP servers, and Returns True if able to bind and user is part of /dev/null. If user not part of /dev/null and/or the user can't bind to LDAP, then it Returns False.

For example:
>>> import LDAPauth
>>> LDAPauth.check_credentials('SSO_USER', 'SSO_PASS')
True
