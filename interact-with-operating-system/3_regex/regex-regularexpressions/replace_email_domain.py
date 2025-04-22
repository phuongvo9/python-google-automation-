#!/usr/bin/env python3

# Replacing the old domain name (abc.edu) with a new domain name (xyz.edu)
# Storing all domain names, including the updated ones, in a new file

import re
import csv

def contains_domain(address, domain):
    """Returns True if the email address contains the given domain in the domain position, False otherwise."""
    domain_pattern = r'[\w\.-]+@' + re.escape(domain) + r'$'
    return re.match(domain_pattern, address) is not None

def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""
    old_domain_pattern = re.escape(old_domain) + r'$'
    return re.sub(old_domain_pattern, new_domain, address)

def main():
    """Processes the list of emails, replacing any instances of the old domain with the new domain."""
    old_domain = 'abc.edu'
    new_domain = 'xyz.edu'
    csv_file_location = '/home/[virtual_machine_username]/data/user_emails.csv'
    report_file = '/home/[virtual_machine_username]/data/updated_user_emails.csv'

    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    # Read the CSV file
    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]  # Extract email addresses

        # Process email addresses
        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)

        # Update the email addresses in the user data
        email_index = user_data_list[0].index('Email Address')
        for user in user_data_list[1:]:
            if user[email_index] in old_domain_email_list:
                user[email_index] = new_domain_email_list[old_domain_email_list.index(user[email_index])]

    # Write the updated data to the report file
    with open(report_file, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)

if __name__ == "__main__":
    main()