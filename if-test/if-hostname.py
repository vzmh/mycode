#!/usr/bin/env python3

## Ask user for a hostname
hostname = input('what is the host name? ')
print('host name you entered:', hostname)

## check hostname against expected configuration
if hostname.upper() == 'MTG':
    print('hostname matches expected config')

## wrap up
print('Exiting the script.')
