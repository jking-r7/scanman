#!/usr/bin/env python3

import subprocess
import logging


class Nmapper:
	''' Nmap base class wrapper '''

	def __init__(self, nsescript, ports, inputlist, xmlfile):
		''' Init arg(s)nsescript:str, ports:lst/str, inputlist:str, xmlfile:str '''
		
		self.nsescript = nsescript
		self.ports = ports
		self.inputlist = inputlist
		self.xmlfile = xmlfile
		self.cmd = \
		f"nmap -Pn --script {self.nsescript} -p {self.ports} -iL {self.inputlist} -oX {self.xmlfile}"


	def parse_ports(self, ports):
		''' 
		Scrub ports convert lst to str(if needed), remove any whitespaces
		arg(s)ports:lst/str 
		'''
		# FEATURE - support multiple ports.
		p = ','.join(ports.split(',')).replace(' ','')
		parsed_ports = p.replace(',',', ')
		
		# # Convert lst to str.
		# portsstr = ''.join(ports)
		# # Remove white-space between ports and convert lst to str.
		# parsed_ports = str(portsstr.replace(' ','') )

		return parsed_ports


	def run_scan(self):
		''' 
		Launch Nmap scan via subprocess wrapper.
		'''
		
		# FEATURE - support multiple ports.
		# Scrub ports from any potential user input error.
		# parsed_ports = self.parse_ports(ports)

		# Nmap command.
		cmdlst = self.cmd.split(' ')

		try:
			proc = subprocess.run(cmdlst, 
				shell=False,
				check=False,
				capture_output=True,
				text=True)
		except Exception as e:
			# Set check=True for the exception to catch.
			logging.exception(e)
			pass
		else:
			# Debug print only.
			logging.debug(f'STDOUT: {proc.stdout}')
			logging.debug(f'STDERR: {proc.stderr}')