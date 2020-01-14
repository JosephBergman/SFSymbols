#
# generate.py
#
# Created by Joseph Bergman
# Copyright © 2020 Joseph Bergman. All rights reserved.

from bs4 import BeautifulSoup
import requests

head = """//
//  SFSymbols.swift
//  SFSymbols
//
//  Created by Joseph Bergman
//  Copyright © 2020 Joseph Bergman. All rights reserved.
//

public enum SFSymbol: String, CaseIterable {
"""

mark = """

    // MARK: {}
"""

special = set(['return', 'repeat'])


if __name__ == '__main__':
	# Download the Symbols
	page = requests.get('https://sfsymbols.com/')
	soup = BeautifulSoup(page.text)

	# Get the symbols
	symbols = [p.string for p in soup.find_all('p')]

	# Convert the symbols to Swift names
	names = {}
	for symbol in symbols:
		if symbol[0].isdigit():
			name = 'number.' + symbol
		else:
			name = symbol
		name = name.replace('.', ' ')
		name = name.title()
		name = name[0].lower() + name[1:]
		name = name.replace(' ', '')
		if name in special:
			name += 'Symbol'
		names[name] = symbol

	# Generate enum cases
	enum = []
	previous = None
	for k in sorted(names.keys()):
		if not previous or previous[0] != k[0]:
			enum.append(mark.format('Symbols - ' + k[0].upper()))
		case = 'case {} = "{}"'
		enum.append(case.format(k, names[k]))
		previous = k

	# Create the file
	with open('SFSymbols.swift', 'w') as file:
		file.write(head)
		previous = None
		for case in enum:
			file.write('    ' + case + '\n')
		file.write('}')
