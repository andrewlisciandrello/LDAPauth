#!/usr/bin/python
import ldap

def check_credentials(username, password):
#def check_credentials():
   """Verifies credentials for username and password.
   Returns None on success or a string describing the error on failure
   """
#   username='SSO_USER'
#   password='LOL_NOPE_LOL'

   LDAP_SERVER = 'ldaps://auth.edir.rackspace.com'
   LDAP_USERNAME = '%s' % username
   LDAP_PASSWORD = password
   base_dn = 'cn=%s,ou=Users,o=rackspace' % username

   try:
       # build a client
       ldap_client = ldap.initialize(LDAP_SERVER)
       # We have to pull the results now, before we auth
       results = ldap_client.search_s("cn=devnull,ou=POSIXGroups,o=rackspace", ldap.SCOPE_SUBTREE)
       # setting options for LDAP, frankly I don't know what these do
       ldap_client.set_option(ldap.OPT_REFERRALS,0)
       # bind to LDAP with user/pass
       ldap_client.simple_bind_s(base_dn, LDAP_PASSWORD)
   except ldap.INVALID_CREDENTIALS:
       # will return false if user can't bind to ldap with their credentials
       ldap_client.unbind()
       return False
   except ldap.SERVER_DOWN:
       # Kinda obvious, if LDAP is down we can't auth
       return False
   for i in results:

      # Is my user in the results variable?
      for member in i[1]['uniqueMember']:
         if username in member:
         # If it is, they can auth
            return true

   ldap_client.unbind()

#check_credentials()
